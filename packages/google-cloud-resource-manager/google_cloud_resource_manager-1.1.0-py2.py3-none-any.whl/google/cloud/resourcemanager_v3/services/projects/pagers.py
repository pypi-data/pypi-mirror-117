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
from typing import (
    Any,
    AsyncIterable,
    Awaitable,
    Callable,
    Iterable,
    Sequence,
    Tuple,
    Optional,
)

from google.cloud.resourcemanager_v3.types import projects


class ListProjectsPager:
    """A pager for iterating through ``list_projects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.resourcemanager_v3.types.ListProjectsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``projects`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListProjects`` requests and continue to iterate
    through the ``projects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.resourcemanager_v3.types.ListProjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., projects.ListProjectsResponse],
        request: projects.ListProjectsRequest,
        response: projects.ListProjectsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.resourcemanager_v3.types.ListProjectsRequest):
                The initial request object.
            response (google.cloud.resourcemanager_v3.types.ListProjectsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = projects.ListProjectsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[projects.ListProjectsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[projects.Project]:
        for page in self.pages:
            yield from page.projects

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class ListProjectsAsyncPager:
    """A pager for iterating through ``list_projects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.resourcemanager_v3.types.ListProjectsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``projects`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListProjects`` requests and continue to iterate
    through the ``projects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.resourcemanager_v3.types.ListProjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[projects.ListProjectsResponse]],
        request: projects.ListProjectsRequest,
        response: projects.ListProjectsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.resourcemanager_v3.types.ListProjectsRequest):
                The initial request object.
            response (google.cloud.resourcemanager_v3.types.ListProjectsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = projects.ListProjectsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[projects.ListProjectsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[projects.Project]:
        async def async_generator():
            async for page in self.pages:
                for response in page.projects:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchProjectsPager:
    """A pager for iterating through ``search_projects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.resourcemanager_v3.types.SearchProjectsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``projects`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``SearchProjects`` requests and continue to iterate
    through the ``projects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.resourcemanager_v3.types.SearchProjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., projects.SearchProjectsResponse],
        request: projects.SearchProjectsRequest,
        response: projects.SearchProjectsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.resourcemanager_v3.types.SearchProjectsRequest):
                The initial request object.
            response (google.cloud.resourcemanager_v3.types.SearchProjectsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = projects.SearchProjectsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    def pages(self) -> Iterable[projects.SearchProjectsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = self._method(self._request, metadata=self._metadata)
            yield self._response

    def __iter__(self) -> Iterable[projects.Project]:
        for page in self.pages:
            yield from page.projects

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)


class SearchProjectsAsyncPager:
    """A pager for iterating through ``search_projects`` requests.

    This class thinly wraps an initial
    :class:`google.cloud.resourcemanager_v3.types.SearchProjectsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``projects`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``SearchProjects`` requests and continue to iterate
    through the ``projects`` field on the
    corresponding responses.

    All the usual :class:`google.cloud.resourcemanager_v3.types.SearchProjectsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    """

    def __init__(
        self,
        method: Callable[..., Awaitable[projects.SearchProjectsResponse]],
        request: projects.SearchProjectsRequest,
        response: projects.SearchProjectsResponse,
        *,
        metadata: Sequence[Tuple[str, str]] = ()
    ):
        """Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.cloud.resourcemanager_v3.types.SearchProjectsRequest):
                The initial request object.
            response (google.cloud.resourcemanager_v3.types.SearchProjectsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        self._method = method
        self._request = projects.SearchProjectsRequest(request)
        self._response = response
        self._metadata = metadata

    def __getattr__(self, name: str) -> Any:
        return getattr(self._response, name)

    @property
    async def pages(self) -> AsyncIterable[projects.SearchProjectsResponse]:
        yield self._response
        while self._response.next_page_token:
            self._request.page_token = self._response.next_page_token
            self._response = await self._method(self._request, metadata=self._metadata)
            yield self._response

    def __aiter__(self) -> AsyncIterable[projects.Project]:
        async def async_generator():
            async for page in self.pages:
                for response in page.projects:
                    yield response

        return async_generator()

    def __repr__(self) -> str:
        return "{0}<{1!r}>".format(self.__class__.__name__, self._response)
