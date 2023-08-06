#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Data types for Anaml Merge Request definitions."""

from __future__ import annotations

from datetime import datetime
from dataclasses import dataclass
from typing import Optional, Type
import enum
from uuid import UUID

from .schema import merge_request_schema
from ..utils import map_opt
from ..utils.serialisation import AnamlBaseClass, AnamlDirectEnum, json_safe, TIMESTAMP_FORMAT


@enum.unique
class MergeRequestStatus(AnamlDirectEnum):
    """Status of a merge request."""

    Open = 'open'
    Closed = 'closed'
    Merged = 'merged'


@dataclass(frozen=True)
class MergeRequest(AnamlBaseClass):
    """Spark configuration to pass to a cluster."""

    id: int
    name: str
    author: int
    comment: str
    source: str
    target: str
    status: MergeRequestStatus
    mergeCommit: Optional[UUID]
    created: datetime
    modified: datetime

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for merge request objects."""
        return merge_request_schema

    def to_json(self) -> dict:
        """Convert a merge request object into JSON data."""
        return json_safe(
            self.to_dict(),
            datetime_format=TIMESTAMP_FORMAT
        )

    @classmethod
    def from_dict(cls: Type[MergeRequest], data: dict) -> MergeRequest:
        """Parse a merge request object from valid JSON data."""
        return MergeRequest(
            id=data['id'],
            name=data['name'],
            author=data['author'],
            comment=data['comment'],
            source=data['source'],
            target=data['target'],
            status=MergeRequestStatus.from_dict(data['status']),
            mergeCommit=map_opt(data.get('mergeCommit', None), UUID),
            created=datetime.strptime(data['created'], TIMESTAMP_FORMAT),
            modified=datetime.strptime(data['modified'], TIMESTAMP_FORMAT),
        )
