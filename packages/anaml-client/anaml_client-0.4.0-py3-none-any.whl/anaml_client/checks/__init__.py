#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#

"""Data types for Anaml Check definitions."""

from __future__ import annotations

from datetime import datetime, timezone
from dataclasses import dataclass, field
from typing import Optional, Type, List
import enum
from uuid import UUID

from .schema import check_schema, check_components_schema
from ..utils import map_opt, parse_instant_optional
from ..utils.serialisation import AnamlDirectEnum, AnamlBaseClass, json_safe, INSTANT_FORMAT


@enum.unique
class CheckStatus(AnamlDirectEnum):
    """Enumeration of check statuses."""

    Pending = 'pending'
    Running = 'running'
    Completed = 'completed'


class CheckConclusion(AnamlDirectEnum):
    """Enumeration of check conclusions."""

    Cancelled = 'cancelled'
    Failure = 'failure'
    Success = 'success'
    Skipped = 'skipped'
    TimedOut = 'timedout'


@dataclass(frozen=True)
class CheckComponent(AnamlBaseClass):
    """Result of a check against an individual component in the catalog."""

    key: str
    value: str

    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for check component objects."""
        return check_components_schema

    @classmethod
    def from_dict(cls: Type[CheckComponent], data: dict) -> CheckComponent:
        """Parse valid a check component from valid JSON data."""
        return CheckComponent(
            key=data['key'],
            value=data['value']
        )


@dataclass(frozen=True)
class Check(AnamlBaseClass):
    """Result of running checks against the Anaml catalogue."""

    name: str
    commit: UUID
    status: CheckStatus
    components: List[CheckComponent] = field(default_factory=list)
    created_by: Optional[int] = None
    id: Optional[int] = None
    started: Optional[datetime] = datetime.now().astimezone(timezone.utc)
    completed: Optional[datetime] = None
    conclusion: Optional[CheckStatus] = None
    details_url: Optional[str] = None

    def with_status(self, new_status: CheckStatus) -> Check:
        """Return a new object with the status changed."""
        dict = self.to_dict()
        dict['status'] = new_status
        if (new_status == CheckStatus.Completed):
            dict['completed'] = datetime.now().astimezone(timezone.utc)
        return Check(**dict)

    def with_conclusion(self, new_conclusion: CheckConclusion) -> Check:
        """Return a new object with the conclusion changed."""
        dict = self.to_dict()
        dict['conclusion'] = new_conclusion
        return Check(**dict)

    def with_extra_component(self, new_component: CheckComponent) -> Check:
        """Return a new object with the extra component added."""
        dict = self.to_dict()
        dict['components'].append(new_component.to_json())
        return Check(**dict)

    @classmethod
    def json_schema(cls) -> dict:
        """Return the JSON schema for check objects."""
        return check_schema

    def to_json(self) -> dict:
        """Serialise this check in JSON."""
        return json_safe(
            self.to_dict(),
            datetime_format=INSTANT_FORMAT
        )

    @classmethod
    def from_dict(cls: Type[Check], data: dict) -> Check:
        """Parse a check from valid JSON data."""
        return Check(
            id=data['id'],
            name=data['name'],
            commit=UUID(hex=data['commit']),
            created_by=data['created_by'],
            started=parse_instant_optional(data['started']),
            completed=parse_instant_optional(data['completed']),
            status=CheckStatus(data['status']),
            components=[CheckComponent.from_dict(c) for c in data['components']],
            conclusion=map_opt(data['conclusion'], lambda x: CheckConclusion(x)),
            details_url=data['details_url']
        )
