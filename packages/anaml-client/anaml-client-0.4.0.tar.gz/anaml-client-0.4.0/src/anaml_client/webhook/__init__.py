#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Webhook notifications from Anaml."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Type, ClassVar, TypeVar
from uuid import UUID

from anaml_client.model import AnamlBaseClass, RunStatus

from . import schema


T = TypeVar('T', bound='WebhookEvent')


@dataclass(frozen=True)
class WebhookEvent(AnamlBaseClass):
    """An event notification received from the Anaml server."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for webhook event objects."""
        return schema.webhook_event

    @classmethod
    def from_dict(cls: Type[WebhookEvent], data: dict) -> WebhookEvent:
        """Parse a webhook event from valid JSON data."""
        adt_type = data['adt_type']
        for klass in cls.__subclasses__():
            if klass.ADT_TYPE == adt_type:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse JSON to WebhookEvent: unknown event type {adt_type}")


@dataclass(frozen=True)
class NewMergeRequestEvent(WebhookEvent):
    """A new merge request has been created."""

    ADT_TYPE: ClassVar[str] = "newmergerequest"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    id: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for new merge request webhook event objects."""
        return schema.new_merge_request

    @classmethod
    def from_dict(cls, data: dict) -> NewMergeRequestEvent:
        """Parse a new merge request webhook event from valid JSON data."""
        return NewMergeRequestEvent(
            id=int(data["id"])
        )


@dataclass(frozen=True)
class MergeRequestCommentEvent(WebhookEvent):
    """A merge request comment has been posted."""

    ADT_TYPE: ClassVar[str] = "newmergerequestcomment"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    id: int
    commentId: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for merge request comment webhook event objects."""
        return schema.merge_request_comment

    @classmethod
    def from_dict(cls, data: dict) -> MergeRequestCommentEvent:
        """Parse a merge request comment webhook event from valid JSON data."""
        return MergeRequestCommentEvent(
            id=int(data['id']),
            commentId=int(data['commentId'])
        )


@dataclass(frozen=True)
class MergeRequestAcceptedEvent(WebhookEvent):
    """A merge request has been accepted."""

    ADT_TYPE: ClassVar[str] = "mergerequestaccepted"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    id: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for merge request accepted webhook event objects."""
        return schema.merge_request_accepted_event

    @classmethod
    def from_dict(cls, data: dict) -> MergeRequestAcceptedEvent:
        """Parse a merge request accepted webhook event from valid JSON data."""
        return MergeRequestAcceptedEvent(
            id=int(data['id'])
        )


@dataclass(frozen=True)
class NewCommitEvent(WebhookEvent):
    """A new commit has been created."""

    ADT_TYPE: ClassVar[str] = "newcommit"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    id: UUID
    branch: Optional[str] = None

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for new commit webhook event objects."""
        return schema.new_commit_event

    @classmethod
    def from_dict(cls, data: dict) -> NewCommitEvent:
        """Parse a new commit webhook event from valid JSON data."""
        return NewCommitEvent(
            id=UUID(hex=data['id']),
            branch=data.get('branch', None)
        )


@dataclass(frozen=True)
class FeatureStoreRunEvent(WebhookEvent):
    """A feature-store job run has started, stopped, etc."""

    ADT_TYPE: ClassVar[str] = "featurestorerun"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    featureStore: int
    run: int
    status: RunStatus

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for feature store run webhook event objects."""
        return schema.feature_store_run_event

    @classmethod
    def from_dict(cls, data: dict) -> FeatureStoreRunEvent:
        """Parse a feature store run webhook event from valid JSON data."""
        return FeatureStoreRunEvent(
            featureStore=int(data['featureStore']),
            run=int(data['run']),
            status=RunStatus.from_dict(data['status'])
        )


@dataclass(frozen=True)
class MonitoringRunEvent(WebhookEvent):
    """A monitoring job run has started, stopped, etc."""

    ADT_TYPE: ClassVar[str] = "monitoringrun"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    job: int
    run: int
    status: RunStatus

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for monitoring run webhook event objects."""
        return schema.monitoring_run_event

    @classmethod
    def from_dict(cls, data: dict) -> MonitoringRunEvent:
        """Parse a monitoring run webhook event from valid JSON data."""
        return MonitoringRunEvent(
            job=int(data['job']),
            run=int(data['run']),
            status=RunStatus.from_dict(data['status'])
        )


@dataclass(frozen=True)
class CachingRunEvent(WebhookEvent):
    """A caching job run has started, stopped, etc."""

    ADT_TYPE: ClassVar[str] = "cachingrun"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    job: int
    run: int
    status: RunStatus

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for caching run webhook event objects."""
        return schema.caching_run_event

    @classmethod
    def from_dict(cls, data: dict) -> CachingRunEvent:
        """Parse a caching run webhook event from valid JSON data."""
        return CachingRunEvent(
            job=int(data['job']),
            run=int(data['run']),
            status=RunStatus.from_dict(data['status'])
        )
