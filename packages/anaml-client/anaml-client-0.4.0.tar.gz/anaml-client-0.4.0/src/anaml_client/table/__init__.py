#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Data types for Anaml table definitions."""

from __future__ import annotations

import uuid

from dataclasses import dataclass, field
from typing import ClassVar, Dict, List, Optional

from .schema import table_schema, root_table_schema, view_table_schema, pivot_table_schema
from ..model import (
    AnamlBaseClass, Attribute, EntityId, EntityMappingId, FeatureId, Label, QualityRating, SourceReference
)


#
# These data type declarations must be kept in sync with
# {repo_top}/common/src/main/scala/io/anaml/common/model
#
# Abbreviations for location clues:
#
# REPO = anaml-server/
# COMMON = anaml-server/common
# MODEL = anaml-server/common/src/main/scala/io/anaml/common/model
# PYCLIENT = anaml-server/python-client/src


#
# TableData $MODEL/TableData.scala
#
TableName = str
TableVersionId = uuid.UUID
TableId = int


class InvalidTableException(Exception):
    """Exception raised when an invalid table specification is give."""


class UnknownTableTypeException(Exception):
    """Exception raised when an unknown table type is given."""


# This matches up to the _name_ of the column extracted from a DB, which
# is why it's text rather than a timestamp object
@dataclass(frozen=True)
class TimestampInfo(AnamlBaseClass):
    """Configuration for the source of timestamp information in a table."""

    timestampColumn: str
    timezone: Optional[str]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for timestamp information objects."""
        # TODO: JSON schema for timestamp info.
        return None

    @classmethod
    def from_dict(cls, d: dict) -> TimestampInfo:
        """Parse a timestamp info object from valid JSON data."""
        return TimestampInfo(
            timestampColumn=d["timestampColumn"],
            timezone=d.get("timezone", None)
        )


@dataclass(frozen=True)
class EventDescription(AnamlBaseClass):
    """Event description information for table a definition."""

    entities: Dict[EntityId, str]
    timestampInfo: TimestampInfo

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for event description objects."""
        # TODO: JSON schema for event description.
        return None

    @classmethod
    def from_dict(cls, d: dict) -> EventDescription:
        """Parse an event description from valid JSON data."""
        return EventDescription(
            entities={int(k): str(v) for k, v in d["entities"].items()},
            timestampInfo=TimestampInfo.from_dict(d["timestampInfo"])
        )


@dataclass(frozen=True)
class Table(AnamlBaseClass):
    """Base class for table definitions."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    id: int
    name: TableName
    description: Optional[str]
    qualityRating: Optional[QualityRating]
    version: TableVersionId
    labels: List[Label]
    attributes: List[Attribute]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for table objects."""
        return table_schema

    @classmethod
    def from_dict(cls, d: dict) -> Table:
        """Parse a table from valid JSON data."""
        adt = d.get("adt_type", None)
        for klass in cls.__subclasses__():
            if adt == klass.ADT_TYPE:
                return klass.from_dict(d)
        raise UnknownTableTypeException(f"Table adt_type {adt} unknown")

    @classmethod
    def _base_fields(cls, data: dict) -> dict:
        """Parse common table fields from valid JSON data."""
        id = data.get("id", None)
        if id:
            id = int(id)
        quality_rating = data.get("qualityRating", None)
        if quality_rating:
            quality_rating = QualityRating(quality_rating)
        return dict(
            id=id,
            name=data["name"],
            description=data.get("description", None),
            qualityRating=quality_rating,
            version=uuid.UUID(hex=data["version"]),
            labels=data["labels"],
            attributes=[Attribute.from_dict(a) for a in data["attributes"]]
        )


@dataclass(frozen=True)
class RootTable(Table):
    """Definition of a root table."""

    ADT_TYPE: ClassVar[str] = "root"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    source: SourceReference
    eventDescription: Optional[EventDescription]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for root table objects."""
        return root_table_schema

    @classmethod
    def from_dict(cls, data: dict) -> RootTable:
        """Parse a root table from valid JSON data."""
        # TODO: Refactor to follow new pattern for handling optional fields.
        event_description = data.get('eventDescription', None)
        if event_description:
            event_description = EventDescription.from_dict(event_description)
        return RootTable(
            **Table._base_fields(data),
            source=SourceReference.from_dict(data["source"]),
            eventDescription=event_description
        )


@dataclass(frozen=True)
class ViewTable(Table):
    """Definition of a view table."""

    ADT_TYPE: ClassVar[str] = "view"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    eventDescription: Optional[EventDescription]
    expression: str
    sources: List[TableId]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for view table objects."""
        return view_table_schema

    @classmethod
    def from_dict(cls, data: dict) -> ViewTable:
        """Parse a view table from valid JSON data."""
        # TODO: Refactor to use new pattern for handling optional fields.
        event_description = data.get('eventDescription', None)
        if event_description:
            event_description = EventDescription.from_dict(event_description)

        return ViewTable(
            **Table._base_fields(data),
            eventDescription=event_description,
            expression=data["expression"],
            sources=[int(s) for s in data["sources"]],
        )


@dataclass(frozen=True)
class PivotTable(Table):
    """Definition for pivot tables."""

    ADT_TYPE: ClassVar[str] = "pivot"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    entityMapping: EntityMappingId
    extraFeatures: List[FeatureId]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for pivot table objects."""
        return pivot_table_schema

    @classmethod
    def from_dict(cls, data: dict) -> PivotTable:
        """Parse a pivot table from valid JSON data."""
        return PivotTable(
            **Table._base_fields(data),
            entityMapping=int(data["entityMapping"]),
            extraFeatures=[int(f) for f in data["extraFeatures"]]
        )
