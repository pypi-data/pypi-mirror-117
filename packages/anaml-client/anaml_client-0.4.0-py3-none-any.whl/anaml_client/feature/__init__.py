#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#
"""Data-types representing Anaml feature definitions."""

from __future__ import annotations

import datetime
import logging

from abc import abstractmethod, ABC
from dataclasses import dataclass, field
from typing import Optional, ClassVar, TypeVar, Type, List

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from ..model import AnamlBaseClass
from .aggregation import Aggregation
from .expression import (
    PostAggregateExpression,
    SelectExpression,
    FilterExpression
)
from .schema import (
    features_schema,
    feature_schema,
    feature_template_schema,
    generated_features_schema, feature_template_schema_event, feature_template_schema_row
)
from .window import Window
from ..utils import map_opt
from ..utils.persistent import persistent

logger = logging.getLogger(__name__)


F = TypeVar('F', bound='BareFeature')
T = TypeVar('T', bound='FeatureTemplate')


@dataclass(frozen=True)
class AbstractFeature(AnamlBaseClass):
    """Abstract base class for Anaml feature definitions."""

    name: str
    description: str
    # TODO: Add labels, attributes, qualityRating

    # This is defined as a property instead of a field due to the ordering
    # imposed by @dataclass on fields with/without default values and the way
    # that requirement interacts with inheritance.
    #
    # Subclasses must declare the corresponding dataclass field as normal.
    @property
    def id(self) -> Optional[int]:
        """Return the unique identifier of this feature."""
        return None

    @abstractmethod
    def is_template(self) -> bool:
        """Determine whether this feature is a template."""

    @abstractmethod
    def as_template(self) -> T:
        """Build a template from this feature."""


@persistent
@dataclass(frozen=True)
class BareFeature(AbstractFeature, ABC):
    """Abstract base class for definitions of bare features."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    def is_template(self) -> bool:
        """Bare features are not templates."""
        return False

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for bare features."""
        return feature_schema

    @classmethod
    def from_dict(cls: Type[F], data: dict) -> F:
        """Parse an event from valid JSON data."""
        adt_type = data.get("adt_type", None)
        for klass in cls.__subclasses__():
            if klass.ADT_TYPE == adt_type:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse feature from JSON: unknown adt_type {adt_type}")


@dataclass(frozen=True)
class FeatureTemplate(AbstractFeature, ABC):
    """Reusable feature definition template."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    def is_template(self) -> bool:
        """Feature templates are, indeed, templates."""
        return True

    def as_template(self) -> T:
        """Feature templates are already templates."""
        return self

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for feature template objects."""
        return feature_template_schema

    @classmethod
    def from_dict(cls, data: dict) -> FeatureTemplate:
        """Parse a feature template from valid JSON data."""
        adt_type = data.get("adt_type", None)
        for klass in cls.__subclasses__():
            if klass.ADT_TYPE == adt_type:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse feature from JSON: unknown adt_type {adt_type}")


@persistent
@dataclass(frozen=True)
class EventFeature(BareFeature):
    """A bare event feature definition."""

    ADT_TYPE = "event"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    table: int
    window: Window
    select: SelectExpression
    filter: Optional[FilterExpression]
    aggregate: Aggregation
    postAggregateExpr: Optional[PostAggregateExpression] = None
    template: Optional[int] = None

    # Override the placeholder property declared in AbstractFeature.
    id: Optional[int] = None

    def as_template(self) -> FeatureTemplate:
        """Build a template from this feature."""
        return EventFeatures(
            id=self.id,
            name=self.name,
            description=self.description,
            table=self.table,
            window=self.window,
            select=self.select,
            filter=self.filter,
            aggregate=self.aggregate,
            postAggregateExpr=self.postAggregateExpr
        )

    @classmethod
    def from_dict(cls, data: dict) -> EventFeature:
        """Parse an event feature from valid JSON data."""
        return EventFeature(
            id=map_opt(data.get("id", None), int),
            name=data["name"],
            description=data["description"],
            table=data["table"],
            window=Window.from_dict(data["window"]),
            select=SelectExpression.from_dict(data["select"]),
            filter=map_opt(data.get("filter", None), FilterExpression.from_dict),
            aggregate=Aggregation.from_json(data["aggregate"]),
            postAggregateExpr=map_opt(data.get("postAggregateExpr", None), PostAggregateExpression.from_dict),
            template=map_opt(data.get("template", None), int),
        )


@persistent
@dataclass(frozen=True)
class RowFeature(BareFeature):
    """A bare row feature definition."""

    ADT_TYPE = "row"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    over: list
    select: SelectExpression
    entityId: int
    template: Optional[int] = None

    # Override the placeholder property declared in AbstractFeature.
    id: Optional[int] = None

    def as_template(self) -> FeatureTemplate:
        """Build a template from this feature."""
        return RowFeatures(
            id=self.id,
            name=self.name,
            description=self.description,
            over=self.over,
            select=self.select,
            entityId=self.entityId
        )

    @classmethod
    def from_dict(cls, data: dict) -> BareFeature:
        """Parse a row feature from valid JSON data."""
        return RowFeature(
            id=map_opt(data.get("id", None), int),
            name=data["name"],
            description=data["description"],
            over=data["over"],
            select=SelectExpression.from_dict(data["select"]),
            entityId=data["entityId"],
            template=data.get("template", None),
        )


@persistent
@dataclass(frozen=True)
class EventFeatures(FeatureTemplate):
    """Template for event features."""

    ADT_TYPE = "event"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    table: int
    window: Window
    select: SelectExpression
    filter: Optional[FilterExpression]
    aggregate: Optional[Aggregation]
    postAggregateExpr: Optional[PostAggregateExpression]

    # Override the placeholder property declared in AbstractFeature.
    id: Optional[int] = None

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for event feature templates."""
        return feature_template_schema_event

    @classmethod
    def from_dict(cls, data: dict) -> EventFeatures:
        """Parse event features from valid JSON data."""
        return EventFeatures(
            id=map_opt(data.get("id"), int),
            name=data["name"],
            description=data["description"],
            table=data["table"],
            window=Window.from_dict(data["window"]),
            select=SelectExpression.from_dict(data["select"]),
            filter=map_opt(data.get("filter", None), FilterExpression.from_dict),
            aggregate=map_opt(data.get("aggregate", None), Aggregation.from_dict),
            postAggregateExpr=map_opt(data.get("postAggregateExpr", None), PostAggregateExpression.from_dict)
        )


@persistent
@dataclass(frozen=True)
class RowFeatures(FeatureTemplate):
    """Template for row features."""

    ADT_TYPE = "row"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    over: List[int]
    select: SelectExpression
    entityId: int

    # Override the placeholder property declared in AbstractFeature.
    id: Optional[int] = None

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for row feature templates."""
        return feature_template_schema_row

    @classmethod
    def from_dict(cls, data: dict) -> RowFeatures:
        """Parse a row feature template from valid JSON data."""
        return RowFeatures(
            id=map_opt(data.get("id"), int),
            name=data["name"],
            description=data["description"],
            over=[int(fid) for fid in data["over"]],
            select=SelectExpression.from_dict(data["select"]),
            entityId=int(data['entityId'])
        )


@dataclass(frozen=True)
class GeneratedFeatures(AnamlBaseClass):
    """Collection of generated feature values."""

    id: str
    date: datetime.date
    features: dict

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for generated features objects."""
        return generated_features_schema

    @classmethod
    def from_dict(cls, generated_features_dict: dict) -> GeneratedFeatures:
        """Parse generated features from valid JSON data."""
        return GeneratedFeatures(
            generated_features_dict["id"],
            datetime.date.fromisoformat(generated_features_dict["date"]),
            generated_features_dict["features"],
        )


def decode_features(features_dictionary_list: List[dict]) -> List[BareFeature]:
    """Validate and parse a JSON document containing a list of features."""
    try:
        validate(features_dictionary_list, features_schema)
        return [
            BareFeature.from_dict(feature_dict) for feature_dict
            in features_dictionary_list
        ]
    except ValidationError:
        logger.error("Unable to validate schema {schema} "
                     "for features dictionary {d}".format(
                         schema=features_schema,
                         d=features_dictionary_list))
        raise
