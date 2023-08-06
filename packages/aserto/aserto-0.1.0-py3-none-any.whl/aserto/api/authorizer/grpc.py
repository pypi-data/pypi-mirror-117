from contextlib import asynccontextmanager
from datetime import datetime, timedelta
from typing import AsyncGenerator, Dict, Mapping, Optional, Sequence, Union, cast
from urllib.parse import urlparse

from aserto_authorizer_grpc.aserto.api.v1 import IdentityContext, IdentityType
from aserto_authorizer_grpc.aserto.api.v1 import PolicyContext as PolicyContextField
from aserto_authorizer_grpc.aserto.authorizer.authorizer.v1 import (
    AuthorizerStub,
    DecisionTreeOptions,
    DecisionTreeResponse,
    PathSeparator,
    Proto,
)
from grpclib.client import Channel
from grpclib.exceptions import StreamTerminatedError
from typing_extensions import Literal

from ..._deadline import monotonic_time_from_deadline
from ..._typing import assert_unreachable
from ...authorizer import Authorizer
from ...identity import Identity
from ...resource_context import ResourceContext
from ._protocol import AuthorizerClientProtocol, DecisionTree


class AuthorizerGrpcClient(AuthorizerClientProtocol):
    def __init__(
        self,
        *,
        tenant_id: str,
        identity: Identity,
        authorizer: Authorizer,
    ):
        self._tenant_id = tenant_id
        self._authorizer = authorizer
        self._identity_context_field = IdentityContext(
            identity=identity.identity_field or "",
            type=cast(IdentityType, IdentityType.from_string(identity.type_field)),
        )

    @property
    def _headers(self) -> Mapping[str, str]:
        headers = {
            "aserto-tenant-id": self._tenant_id,
        }

        if self._authorizer.auth_header is not None:
            headers["authorization"] = self._authorizer.auth_header

        return headers

    @asynccontextmanager  # type: ignore[misc]
    async def _authorizer_client(self, deadline: Optional[Union[datetime, timedelta]]) -> AsyncGenerator[AuthorizerStub, None]:  # type: ignore[misc]
        result = urlparse(self._authorizer.url)

        channel = Channel(
            host=result.hostname,
            port=result.port,
            ssl=self._authorizer.ssl_context or True,
        )

        async with channel as channel:
            yield AuthorizerStub(
                channel,
                metadata=self._headers,
                timeout=(monotonic_time_from_deadline(deadline) if deadline is not None else None),
            )

    @staticmethod
    def _policy_path_separator_field(
        policy_path_separator: Literal["DOT", "SLASH"]
    ) -> PathSeparator:
        if policy_path_separator == "DOT":
            return PathSeparator.PATH_SEPARATOR_DOT
        elif policy_path_separator == "SLASH":
            return PathSeparator.PATH_SEPARATOR_SLASH
        else:
            assert_unreachable(policy_path_separator)

    async def decision_tree(
        self,
        *,
        decisions: Sequence[str],
        policy_id: str,
        policy_path_root: str,
        resource_context: Optional[ResourceContext] = None,
        policy_path_separator: Optional[Literal["DOT", "SLASH"]] = None,
        deadline: Optional[Union[datetime, timedelta]] = None,
    ) -> DecisionTree:
        options = DecisionTreeOptions()
        if policy_path_separator is not None:
            options.path_separator = self._policy_path_separator_field(policy_path_separator)

        try:
            async with self._authorizer_client(deadline=deadline) as client:
                response = await client.decision_tree(
                    policy_context=PolicyContextField(
                        id=policy_id,
                        path=policy_path_root,
                        decisions=list(decisions),
                    ),
                    identity_context=self._identity_context_field,
                    resource_context=Proto.Struct().from_dict(value=(resource_context or {})),
                    options=options,
                )
        except (OSError, StreamTerminatedError) as error:
            raise ConnectionError(*error.args) from error  # type: ignore[misc]

        return self._validate_decision_tree(response)

    @staticmethod
    def _validate_decision_tree(response: DecisionTreeResponse) -> DecisionTree:
        error = TypeError("Received unexpected response data")

        decision_tree: DecisionTree = {}

        for path, decisions in response.path.fields.items():
            if decisions._group_current.get("kind") != "struct_value":
                raise error

            for name, decision in decisions.struct_value.fields.items():
                if decision._group_current.get("kind") != "bool_value":
                    raise error

                decision_tree.setdefault(path, {})[name] = decision.bool_value

        return decision_tree

    async def decisions(
        self,
        *,
        decisions: Sequence[str],
        policy_id: str,
        policy_path: str,
        resource_context: Optional[ResourceContext] = None,
        deadline: Optional[Union[datetime, timedelta]] = None,
    ) -> Dict[str, bool]:
        try:
            async with self._authorizer_client(deadline=deadline) as client:
                response = await client.is_(
                    policy_context=PolicyContextField(
                        id=policy_id,
                        path=policy_path,
                        decisions=list(decisions),
                    ),
                    identity_context=self._identity_context_field,
                    resource_context=Proto.Struct().from_dict(value=(resource_context or {})),
                )
        except (OSError, StreamTerminatedError) as error:
            raise ConnectionError(*error.args) from error  # type: ignore[misc]

        results = {}
        for decision_object in response.decisions:
            results[decision_object.decision] = decision_object.is_

        return results
