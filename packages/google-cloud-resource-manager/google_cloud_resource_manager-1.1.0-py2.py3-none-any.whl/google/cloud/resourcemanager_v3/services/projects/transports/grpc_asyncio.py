# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import warnings
from typing import Awaitable, Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import gapic_v1  # type: ignore
from google.api_core import grpc_helpers_async  # type: ignore
from google.api_core import operations_v1  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore
import packaging.version

import grpc  # type: ignore
from grpc.experimental import aio  # type: ignore

from google.cloud.resourcemanager_v3.types import projects
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from .base import ProjectsTransport, DEFAULT_CLIENT_INFO
from .grpc import ProjectsGrpcTransport


class ProjectsGrpcAsyncIOTransport(ProjectsTransport):
    """gRPC AsyncIO backend transport for Projects.

    Manages Google Cloud Projects.

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _grpc_channel: aio.Channel
    _stubs: Dict[str, Callable] = {}

    @classmethod
    def create_channel(
        cls,
        host: str = "cloudresourcemanager.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> aio.Channel:
        """Create and return a gRPC AsyncIO channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            aio.Channel: A gRPC AsyncIO channel object.
        """

        return grpc_helpers_async.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    def __init__(
        self,
        *,
        host: str = "cloudresourcemanager.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        channel: aio.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id=None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            channel (Optional[aio.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or applicatin default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None
        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                credentials=self._credentials,
                credentials_file=credentials_file,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @property
    def grpc_channel(self) -> aio.Channel:
        """Create the channel designed to connect to this service.

        This property caches on the instance; repeated calls return
        the same channel.
        """
        # Return the channel from cache.
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsAsyncClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Sanity check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsAsyncClient(
                self.grpc_channel
            )

        # Return the client from cache.
        return self._operations_client

    @property
    def get_project(
        self,
    ) -> Callable[[projects.GetProjectRequest], Awaitable[projects.Project]]:
        r"""Return a callable for the get project method over gRPC.

        Retrieves the project identified by the specified ``name`` (for
        example, ``projects/415104041262``).

        The caller must have ``resourcemanager.projects.get`` permission
        for this project.

        Returns:
            Callable[[~.GetProjectRequest],
                    Awaitable[~.Project]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_project" not in self._stubs:
            self._stubs["get_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/GetProject",
                request_serializer=projects.GetProjectRequest.serialize,
                response_deserializer=projects.Project.deserialize,
            )
        return self._stubs["get_project"]

    @property
    def list_projects(
        self,
    ) -> Callable[
        [projects.ListProjectsRequest], Awaitable[projects.ListProjectsResponse]
    ]:
        r"""Return a callable for the list projects method over gRPC.

        Lists projects that are direct children of the specified folder
        or organization resource. ``list()`` provides a strongly
        consistent view of the projects underneath the specified parent
        resource. ``list()`` returns projects sorted based upon the
        (ascending) lexical ordering of their ``display_name``. The
        caller must have ``resourcemanager.projects.list`` permission on
        the identified parent.

        Returns:
            Callable[[~.ListProjectsRequest],
                    Awaitable[~.ListProjectsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_projects" not in self._stubs:
            self._stubs["list_projects"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/ListProjects",
                request_serializer=projects.ListProjectsRequest.serialize,
                response_deserializer=projects.ListProjectsResponse.deserialize,
            )
        return self._stubs["list_projects"]

    @property
    def search_projects(
        self,
    ) -> Callable[
        [projects.SearchProjectsRequest], Awaitable[projects.SearchProjectsResponse]
    ]:
        r"""Return a callable for the search projects method over gRPC.

        Search for projects that the caller has both
        ``resourcemanager.projects.get`` permission on, and also satisfy
        the specified query.

        This method returns projects in an unspecified order.

        This method is eventually consistent with project mutations;
        this means that a newly created project may not appear in the
        results or recent updates to an existing project may not be
        reflected in the results. To retrieve the latest state of a
        project, use the
        [GetProject][google.cloud.resourcemanager.v3.Projects.GetProject]
        method.

        Returns:
            Callable[[~.SearchProjectsRequest],
                    Awaitable[~.SearchProjectsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_projects" not in self._stubs:
            self._stubs["search_projects"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/SearchProjects",
                request_serializer=projects.SearchProjectsRequest.serialize,
                response_deserializer=projects.SearchProjectsResponse.deserialize,
            )
        return self._stubs["search_projects"]

    @property
    def create_project(
        self,
    ) -> Callable[[projects.CreateProjectRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create project method over gRPC.

        Request that a new project be created. The result is an
        ``Operation`` which can be used to track the creation process.
        This process usually takes a few seconds, but can sometimes take
        much longer. The tracking ``Operation`` is automatically deleted
        after a few hours, so there is no need to call
        ``DeleteOperation``.

        Returns:
            Callable[[~.CreateProjectRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_project" not in self._stubs:
            self._stubs["create_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/CreateProject",
                request_serializer=projects.CreateProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_project"]

    @property
    def update_project(
        self,
    ) -> Callable[[projects.UpdateProjectRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update project method over gRPC.

        Updates the ``display_name`` and labels of the project
        identified by the specified ``name`` (for example,
        ``projects/415104041262``). Deleting all labels requires an
        update mask for labels field.

        The caller must have ``resourcemanager.projects.update``
        permission for this project.

        Returns:
            Callable[[~.UpdateProjectRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_project" not in self._stubs:
            self._stubs["update_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/UpdateProject",
                request_serializer=projects.UpdateProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_project"]

    @property
    def move_project(
        self,
    ) -> Callable[[projects.MoveProjectRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the move project method over gRPC.

        Move a project to another place in your resource hierarchy,
        under a new resource parent.

        Returns an operation which can be used to track the process of
        the project move workflow. Upon success, the
        ``Operation.response`` field will be populated with the moved
        project.

        The caller must have ``resourcemanager.projects.update``
        permission on the project and have
        ``resourcemanager.projects.move`` permission on the project's
        current and proposed new parent.

        Returns:
            Callable[[~.MoveProjectRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_project" not in self._stubs:
            self._stubs["move_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/MoveProject",
                request_serializer=projects.MoveProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["move_project"]

    @property
    def delete_project(
        self,
    ) -> Callable[[projects.DeleteProjectRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete project method over gRPC.

        Marks the project identified by the specified ``name`` (for
        example, ``projects/415104041262``) for deletion.

        This method will only affect the project if it has a lifecycle
        state of
        [ACTIVE][google.cloud.resourcemanager.v3.Project.State.ACTIVE].

        This method changes the Project's lifecycle state from
        [ACTIVE][google.cloud.resourcemanager.v3.Project.State.ACTIVE]
        to
        [DELETE_REQUESTED][google.cloud.resourcemanager.v3.Project.State.DELETE_REQUESTED].
        The deletion starts at an unspecified time, at which point the
        Project is no longer accessible.

        Until the deletion completes, you can check the lifecycle state
        checked by retrieving the project with [GetProject]
        [google.cloud.resourcemanager.v3.Projects.GetProject], and the
        project remains visible to [ListProjects]
        [google.cloud.resourcemanager.v3.Projects.ListProjects].
        However, you cannot update the project.

        After the deletion completes, the project is not retrievable by
        the [GetProject]
        [google.cloud.resourcemanager.v3.Projects.GetProject],
        [ListProjects]
        [google.cloud.resourcemanager.v3.Projects.ListProjects], and
        [SearchProjects][google.cloud.resourcemanager.v3.Projects.SearchProjects]
        methods.

        This method behaves idempotently, such that deleting a
        ``DELETE_REQUESTED`` project will not cause an error, but also
        won't do anything.

        The caller must have ``resourcemanager.projects.delete``
        permissions for this project.

        Returns:
            Callable[[~.DeleteProjectRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_project" not in self._stubs:
            self._stubs["delete_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/DeleteProject",
                request_serializer=projects.DeleteProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_project"]

    @property
    def undelete_project(
        self,
    ) -> Callable[
        [projects.UndeleteProjectRequest], Awaitable[operations_pb2.Operation]
    ]:
        r"""Return a callable for the undelete project method over gRPC.

        Restores the project identified by the specified ``name`` (for
        example, ``projects/415104041262``). You can only use this
        method for a project that has a lifecycle state of
        [DELETE_REQUESTED] [Projects.State.DELETE_REQUESTED]. After
        deletion starts, the project cannot be restored.

        The caller must have ``resourcemanager.projects.undelete``
        permission for this project.

        Returns:
            Callable[[~.UndeleteProjectRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_project" not in self._stubs:
            self._stubs["undelete_project"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/UndeleteProject",
                request_serializer=projects.UndeleteProjectRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undelete_project"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the get iam policy method over gRPC.

        Returns the IAM access control policy for the
        specified project. Permission is denied if the policy or
        the resource do not exist.

        Returns:
            Callable[[~.GetIamPolicyRequest],
                    Awaitable[~.Policy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_iam_policy" not in self._stubs:
            self._stubs["get_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the IAM access control policy for the specified project.

        CAUTION: This method will replace the existing policy, and
        cannot be used to append additional IAM settings.

        Note: Removing service accounts from policies or changing their
        roles can render services completely inoperable. It is important
        to understand how the service account is being used before
        removing or updating its roles.

        The following constraints apply when using ``setIamPolicy()``:

        -  Project does not support ``allUsers`` and
           ``allAuthenticatedUsers`` as ``members`` in a ``Binding`` of
           a ``Policy``.

        -  The owner role can be granted to a ``user``,
           ``serviceAccount``, or a group that is part of an
           organization. For example, group@myownpersonaldomain.com
           could be added as an owner to a project in the
           myownpersonaldomain.com organization, but not the
           examplepetstore.com organization.

        -  Service accounts can be made owners of a project directly
           without any restrictions. However, to be added as an owner, a
           user must be invited using the Cloud Platform console and
           must accept the invitation.

        -  A user cannot be granted the owner role using
           ``setIamPolicy()``. The user must be granted the owner role
           using the Cloud Platform Console and must explicitly accept
           the invitation.

        -  Invitations to grant the owner role cannot be sent using
           ``setIamPolicy()``; they must be sent only using the Cloud
           Platform Console.

        -  Membership changes that leave the project without any owners
           that have accepted the Terms of Service (ToS) will be
           rejected.

        -  If the project is not part of an organization, there must be
           at least one owner who has accepted the Terms of Service
           (ToS) agreement in the policy. Calling ``setIamPolicy()`` to
           remove the last ToS-accepted owner from the policy will fail.
           This restriction also applies to legacy projects that no
           longer have owners who have accepted the ToS. Edits to IAM
           policies will be rejected until the lack of a ToS-accepting
           owner is rectified.

        -  Calling this method requires enabling the App Engine Admin
           API.

        Returns:
            Callable[[~.SetIamPolicyRequest],
                    Awaitable[~.Policy]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "set_iam_policy" not in self._stubs:
            self._stubs["set_iam_policy"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/SetIamPolicy",
                request_serializer=iam_policy_pb2.SetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["set_iam_policy"]

    @property
    def test_iam_permissions(
        self,
    ) -> Callable[
        [iam_policy_pb2.TestIamPermissionsRequest],
        Awaitable[iam_policy_pb2.TestIamPermissionsResponse],
    ]:
        r"""Return a callable for the test iam permissions method over gRPC.

        Returns permissions that a caller has on the
        specified project.

        Returns:
            Callable[[~.TestIamPermissionsRequest],
                    Awaitable[~.TestIamPermissionsResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "test_iam_permissions" not in self._stubs:
            self._stubs["test_iam_permissions"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Projects/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]


__all__ = ("ProjectsGrpcAsyncIOTransport",)
