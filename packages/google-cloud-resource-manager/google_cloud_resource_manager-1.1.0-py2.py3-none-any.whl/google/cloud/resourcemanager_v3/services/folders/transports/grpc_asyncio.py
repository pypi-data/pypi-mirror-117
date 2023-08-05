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

from google.cloud.resourcemanager_v3.types import folders
from google.iam.v1 import iam_policy_pb2  # type: ignore
from google.iam.v1 import policy_pb2  # type: ignore
from google.longrunning import operations_pb2  # type: ignore
from .base import FoldersTransport, DEFAULT_CLIENT_INFO
from .grpc import FoldersGrpcTransport


class FoldersGrpcAsyncIOTransport(FoldersTransport):
    """gRPC AsyncIO backend transport for Folders.

    Manages Cloud Platform folder resources.
    Folders can be used to organize the resources under an
    organization and to control the policies applied to groups of
    resources.

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
    def get_folder(
        self,
    ) -> Callable[[folders.GetFolderRequest], Awaitable[folders.Folder]]:
        r"""Return a callable for the get folder method over gRPC.

        Retrieves a folder identified by the supplied resource name.
        Valid folder resource names have the format
        ``folders/{folder_id}`` (for example, ``folders/1234``). The
        caller must have ``resourcemanager.folders.get`` permission on
        the identified folder.

        Returns:
            Callable[[~.GetFolderRequest],
                    Awaitable[~.Folder]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_folder" not in self._stubs:
            self._stubs["get_folder"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/GetFolder",
                request_serializer=folders.GetFolderRequest.serialize,
                response_deserializer=folders.Folder.deserialize,
            )
        return self._stubs["get_folder"]

    @property
    def list_folders(
        self,
    ) -> Callable[[folders.ListFoldersRequest], Awaitable[folders.ListFoldersResponse]]:
        r"""Return a callable for the list folders method over gRPC.

        Lists the folders that are direct descendants of supplied parent
        resource. ``list()`` provides a strongly consistent view of the
        folders underneath the specified parent resource. ``list()``
        returns folders sorted based upon the (ascending) lexical
        ordering of their display_name. The caller must have
        ``resourcemanager.folders.list`` permission on the identified
        parent.

        Returns:
            Callable[[~.ListFoldersRequest],
                    Awaitable[~.ListFoldersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_folders" not in self._stubs:
            self._stubs["list_folders"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/ListFolders",
                request_serializer=folders.ListFoldersRequest.serialize,
                response_deserializer=folders.ListFoldersResponse.deserialize,
            )
        return self._stubs["list_folders"]

    @property
    def search_folders(
        self,
    ) -> Callable[
        [folders.SearchFoldersRequest], Awaitable[folders.SearchFoldersResponse]
    ]:
        r"""Return a callable for the search folders method over gRPC.

        Search for folders that match specific filter criteria.
        ``search()`` provides an eventually consistent view of the
        folders a user has access to which meet the specified filter
        criteria.

        This will only return folders on which the caller has the
        permission ``resourcemanager.folders.get``.

        Returns:
            Callable[[~.SearchFoldersRequest],
                    Awaitable[~.SearchFoldersResponse]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "search_folders" not in self._stubs:
            self._stubs["search_folders"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/SearchFolders",
                request_serializer=folders.SearchFoldersRequest.serialize,
                response_deserializer=folders.SearchFoldersResponse.deserialize,
            )
        return self._stubs["search_folders"]

    @property
    def create_folder(
        self,
    ) -> Callable[[folders.CreateFolderRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the create folder method over gRPC.

        Creates a folder in the resource hierarchy. Returns an
        ``Operation`` which can be used to track the progress of the
        folder creation workflow. Upon success, the
        ``Operation.response`` field will be populated with the created
        Folder.

        In order to succeed, the addition of this new folder must not
        violate the folder naming, height, or fanout constraints.

        -  The folder's ``display_name`` must be distinct from all other
           folders that share its parent.
        -  The addition of the folder must not cause the active folder
           hierarchy to exceed a height of 10. Note, the full active +
           deleted folder hierarchy is allowed to reach a height of 20;
           this provides additional headroom when moving folders that
           contain deleted folders.
        -  The addition of the folder must not cause the total number of
           folders under its parent to exceed 300.

        If the operation fails due to a folder constraint violation,
        some errors may be returned by the ``CreateFolder`` request,
        with status code ``FAILED_PRECONDITION`` and an error
        description. Other folder constraint violations will be
        communicated in the ``Operation``, with the specific
        ``PreconditionFailure`` returned in the details list in the
        ``Operation.error`` field.

        The caller must have ``resourcemanager.folders.create``
        permission on the identified parent.

        Returns:
            Callable[[~.CreateFolderRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_folder" not in self._stubs:
            self._stubs["create_folder"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/CreateFolder",
                request_serializer=folders.CreateFolderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["create_folder"]

    @property
    def update_folder(
        self,
    ) -> Callable[[folders.UpdateFolderRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the update folder method over gRPC.

        Updates a folder, changing its ``display_name``. Changes to the
        folder ``display_name`` will be rejected if they violate either
        the ``display_name`` formatting rules or the naming constraints
        described in the
        [CreateFolder][google.cloud.resourcemanager.v3.Folders.CreateFolder]
        documentation.

        The folder's ``display_name`` must start and end with a letter
        or digit, may contain letters, digits, spaces, hyphens and
        underscores and can be between 3 and 30 characters. This is
        captured by the regular expression:
        ``[\p{L}\p{N}][\p{L}\p{N}_- ]{1,28}[\p{L}\p{N}]``. The caller
        must have ``resourcemanager.folders.update`` permission on the
        identified folder.

        If the update fails due to the unique name constraint then a
        ``PreconditionFailure`` explaining this violation will be
        returned in the Status.details field.

        Returns:
            Callable[[~.UpdateFolderRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_folder" not in self._stubs:
            self._stubs["update_folder"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/UpdateFolder",
                request_serializer=folders.UpdateFolderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["update_folder"]

    @property
    def move_folder(
        self,
    ) -> Callable[[folders.MoveFolderRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the move folder method over gRPC.

        Moves a folder under a new resource parent. Returns an
        ``Operation`` which can be used to track the progress of the
        folder move workflow. Upon success, the ``Operation.response``
        field will be populated with the moved folder. Upon failure, a
        ``FolderOperationError`` categorizing the failure cause will be
        returned - if the failure occurs synchronously then the
        ``FolderOperationError`` will be returned in the
        ``Status.details`` field. If it occurs asynchronously, then the
        FolderOperation will be returned in the ``Operation.error``
        field. In addition, the ``Operation.metadata`` field will be
        populated with a ``FolderOperation`` message as an aid to
        stateless clients. Folder moves will be rejected if they violate
        either the naming, height, or fanout constraints described in
        the
        [CreateFolder][google.cloud.resourcemanager.v3.Folders.CreateFolder]
        documentation. The caller must have
        ``resourcemanager.folders.move`` permission on the folder's
        current and proposed new parent.

        Returns:
            Callable[[~.MoveFolderRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "move_folder" not in self._stubs:
            self._stubs["move_folder"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/MoveFolder",
                request_serializer=folders.MoveFolderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["move_folder"]

    @property
    def delete_folder(
        self,
    ) -> Callable[[folders.DeleteFolderRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the delete folder method over gRPC.

        Requests deletion of a folder. The folder is moved into the
        [DELETE_REQUESTED][google.cloud.resourcemanager.v3.Folder.State.DELETE_REQUESTED]
        state immediately, and is deleted approximately 30 days later.
        This method may only be called on an empty folder, where a
        folder is empty if it doesn't contain any folders or projects in
        the
        [ACTIVE][google.cloud.resourcemanager.v3.Folder.State.ACTIVE]
        state. If called on a folder in
        [DELETE_REQUESTED][google.cloud.resourcemanager.v3.Folder.State.DELETE_REQUESTED]
        state the operation will result in a no-op success. The caller
        must have ``resourcemanager.folders.delete`` permission on the
        identified folder.

        Returns:
            Callable[[~.DeleteFolderRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_folder" not in self._stubs:
            self._stubs["delete_folder"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/DeleteFolder",
                request_serializer=folders.DeleteFolderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["delete_folder"]

    @property
    def undelete_folder(
        self,
    ) -> Callable[[folders.UndeleteFolderRequest], Awaitable[operations_pb2.Operation]]:
        r"""Return a callable for the undelete folder method over gRPC.

        Cancels the deletion request for a folder. This method may be
        called on a folder in any state. If the folder is in the
        [ACTIVE][google.cloud.resourcemanager.v3.Folder.State.ACTIVE]
        state the result will be a no-op success. In order to succeed,
        the folder's parent must be in the
        [ACTIVE][google.cloud.resourcemanager.v3.Folder.State.ACTIVE]
        state. In addition, reintroducing the folder into the tree must
        not violate folder naming, height, and fanout constraints
        described in the
        [CreateFolder][google.cloud.resourcemanager.v3.Folders.CreateFolder]
        documentation. The caller must have
        ``resourcemanager.folders.undelete`` permission on the
        identified folder.

        Returns:
            Callable[[~.UndeleteFolderRequest],
                    Awaitable[~.Operation]]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "undelete_folder" not in self._stubs:
            self._stubs["undelete_folder"] = self.grpc_channel.unary_unary(
                "/google.cloud.resourcemanager.v3.Folders/UndeleteFolder",
                request_serializer=folders.UndeleteFolderRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["undelete_folder"]

    @property
    def get_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.GetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the get iam policy method over gRPC.

        Gets the access control policy for a folder. The returned policy
        may be empty if no such policy or resource exists. The
        ``resource`` field should be the folder's resource name, for
        example: "folders/1234". The caller must have
        ``resourcemanager.folders.getIamPolicy`` permission on the
        identified folder.

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
                "/google.cloud.resourcemanager.v3.Folders/GetIamPolicy",
                request_serializer=iam_policy_pb2.GetIamPolicyRequest.SerializeToString,
                response_deserializer=policy_pb2.Policy.FromString,
            )
        return self._stubs["get_iam_policy"]

    @property
    def set_iam_policy(
        self,
    ) -> Callable[[iam_policy_pb2.SetIamPolicyRequest], Awaitable[policy_pb2.Policy]]:
        r"""Return a callable for the set iam policy method over gRPC.

        Sets the access control policy on a folder, replacing any
        existing policy. The ``resource`` field should be the folder's
        resource name, for example: "folders/1234". The caller must have
        ``resourcemanager.folders.setIamPolicy`` permission on the
        identified folder.

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
                "/google.cloud.resourcemanager.v3.Folders/SetIamPolicy",
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

        Returns permissions that a caller has on the specified folder.
        The ``resource`` field should be the folder's resource name, for
        example: "folders/1234".

        There are no permissions required for making this API call.

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
                "/google.cloud.resourcemanager.v3.Folders/TestIamPermissions",
                request_serializer=iam_policy_pb2.TestIamPermissionsRequest.SerializeToString,
                response_deserializer=iam_policy_pb2.TestIamPermissionsResponse.FromString,
            )
        return self._stubs["test_iam_permissions"]


__all__ = ("FoldersGrpcAsyncIOTransport",)
