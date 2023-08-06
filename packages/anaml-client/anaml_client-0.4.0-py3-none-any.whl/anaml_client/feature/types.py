#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#

import datetime
import logging

from abc import ABC, abstractmethod
from typing import Optional

from jsonschema import validate
from jsonschema.exceptions import ValidationError

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
    generated_features_schema
)
from .window import Window


logger = logging.getLogger(__name__)


class Feature(ABC):
    def __init__(self, name: str, description: str, id: Optional[int] = None):
        self._id = id
        self._name = name
        self._description = description

    def __repr__(self):
        return """Feature(id={id}, name={name}, description={desc})""".format(
            id=self._id, name=self._name, desc=self._description)

    def __eq__(self, other):
        return NotImplemented

    def __ne__(self, other):
        x = self.__eq__(other)
        if x is not NotImplemented:
            return not x
        else:
            return NotImplemented

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def set_description(self, description):
        self._description = description

    def get_description(self):
        return self._description

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    @abstractmethod
    def isTemplate(self) -> bool:
        pass

    @abstractmethod
    def asTemplate(self) -> bool:
        pass

    @abstractmethod
    def to_dict(self) -> dict:
        pass

    def _toDictionaryCommon(self) -> dict:
        common = {
            "name": self._name,
            "description": self._description,
        }
        if self._id is not None:
            common.update({"id": self._id})
        return common

    @classmethod
    def json_schema(cls):
        pass

    @classmethod
    def from_json(cls, d: dict):
        try:
            validate(d, cls.json_schema())
        except ValidationError:
            logger.error("Unable to validate schema {schema} "
                         "from dict {d}".format(schema=cls.json_schema(), d=d))
            raise
        return cls.from_dict(d)

    @classmethod
    def from_dict(cls, feature_dict: dict):
        pass


class BareFeature(Feature):
    """Feature class"""

    def __init__(self, name, description, template, id: Optional[int] = None):
        super().__init__(name, description, id)
        self._template = template

    def to_dict(self):
        pass

    def isTemplate(self) -> bool:
        return False

    @classmethod
    def json_schema(cls):
        return feature_schema

    @classmethod
    def from_dict(cls, feature_dict: dict) -> Feature:
        if feature_dict.get("adt_type") == "event":
            feature = EventFeature(
                name=feature_dict.get("name"),
                description=feature_dict.get("description"),
                table=feature_dict.get("table"),
                window=Window.from_dict(feature_dict.get("window")),
                select=SelectExpression.from_dict(
                    feature_dict.get("select")),
                filter=FilterExpression.from_dict(
                    feature_dict.get("filter")),
                aggregate=Aggregation.from_dict(
                    feature_dict.get("aggregate")),
                postAggregateExpr=PostAggregateExpression.from_dict(
                    feature_dict.get("postAggregateExpr")),
                template=feature_dict.get("template"),
            )
        elif feature_dict.get("adt_type") == "row":
            feature = RowFeature(
                name=feature_dict.get("name"),
                description=feature_dict.get("description"),
                over=feature_dict.get("over"),
                select=SelectExpression.from_dict(
                    feature_dict.get("select")),
                entityId=feature_dict.get("entityId"),
                template=feature_dict.get("template"),
            )
        else:
            pass

        feature.set_id(feature_dict.get("id"))
        return feature


class FeatureTemplate(Feature):
    def __init__(self, name, description, id: Optional[int] = None):
        super().__init__(name, description, id)

    def to_dict(self):
        pass

    def isTemplate(self) -> bool:
        return True

    @classmethod
    def json_schema(cls):
        return feature_template_schema

    @classmethod
    def from_dict(cls, feature_dict: dict):
        if feature_dict.get("adt_type") == "event":
            feature = EventFeatures(
                name=feature_dict.get("name"),
                description=feature_dict.get("description"),
                table=feature_dict.get("table"),
                window=Window.from_dict(feature_dict.get("window")),
                select=SelectExpression.from_dict(
                    feature_dict.get("select")),
                filter=FilterExpression.from_dict(
                    feature_dict.get("filter")),
                aggregate=Aggregation.from_dict(
                    feature_dict.get("aggregate")),
                postAggregateExpr=PostAggregateExpression.from_dict(
                    feature_dict.get("postAggregateExpr"))
            )

        feature.set_id(feature_dict.get("id"))
        return feature


class EventFeature(BareFeature):
    def __init__(
        self,
        name: str,
        description: str,
        table: int,
        window: Window,
        select: SelectExpression,
        filter: Optional[FilterExpression],
        aggregate: Aggregation,
        postAggregateExpr: Optional[PostAggregateExpression] = None,
        template: Optional[int] = None,
        id: Optional[int] = None
    ):
        super().__init__(name, description, template, id)
        self._table = table
        self._window = window
        self._select = select
        self._filter = filter
        self._aggregate = aggregate
        self._postAggregateExpr = postAggregateExpr

    def __eq__(self, other):
        if not isinstance(other, EventFeature):
            return NotImplemented
        return (
            self._id,
            self._name,
            self._description,
            self._table,
            self._window,
            self._select,
            self._filter,
            self._aggregate,
            self._template,
            self._postAggregateExpr,
        ) == (
            other._id,
            other._name,
            other._description,
            other._table,
            other._window,
            other._select,
            other._filter,
            other._aggregate,
            other._template,
            other._postAggregateExpr,
        )

    def __repr__(self):
        reprstr = """EventFeature(id={id}, name={name}, description={desc}, """
        reprstr += """table={table}, window={window}, select={select}, """
        reprstr += """filter={filter}, aggregate={aggr}, """
        reprstr += """postAggregateExpr={postaggr}, template={template})"""
        return reprstr.format(id=self._id, name=self._name,
                              desc=self._description, table=self._table,
                              window=self._window, select=self._select,
                              filter=self._filter, aggr=self._aggregate,
                              postaggr=self._postAggregateExpr,
                              template=self._template)

    def to_dict(self):
        common = self._toDictionaryCommon()
        common.update(
            {
                "adt_type": "event",
                "table": self._table,
                "window": self._window.to_json(),
                "select": self._select.to_dict(),
                "filter":
                    None if not self._filter else self._filter.to_dict(),
                "aggregate": self._aggregate.to_dict(),
                "postAggregateExpr":
                    None if not self._postAggregateExpr else
                    self._postAggregateExpr.to_dict(),
                "template": self._template,
            }
        )
        return common

    def asTemplate(self) -> FeatureTemplate:
        feature = EventFeatures(
            name=self.name,
            description=self.description,
            table=self._table,
            window=self._window,
            select=self._select,
            filter=self._filter,
            aggregate=self._aggregate,
            postAggregateExpr=self._postAggregateExpr
        )

        feature.set_id(self._id)
        return feature


class RowFeature(BareFeature):
    def __init__(
        self,
        name: str,
        description: str,
        over: list,
        select: SelectExpression,
        entityId: int,
        template: Optional[int] = None,
        id: Optional[int] = None
    ):
        super().__init__(name, description, template, id)
        self._over = over
        self._select = select
        self._entityId = entityId

    def __eq__(self, other):
        if not isinstance(other, RowFeature):
            return NotImplemented
        return (
            self._id,
            self._name,
            self._description,
            self._over,
            self._select,
            self._entityId,
            self._template,
        ) == (
            other._id,
            other._name,
            other._description,
            other._over,
            other._select,
            other._entityId,
            other._template,
        )

    def __repr__(self):
        reprstr = """RowFeature(id={id}, name={name}, description={desc}, """
        reprstr += """over={over}, select={select}, entityId={entity}, """
        reprstr += """template={template})"""
        return reprstr.format(id=self._id, name=self._name,
                              desc=self._description, over=self._over,
                              select=self._select, entity=self._entityId,
                              template=self._template)

    def to_dict(self):
        common = self._toDictionaryCommon()
        common.update(
            {
                "adt_type": "row",
                "over": self._over,
                "select": self._select.to_dict(),
                "entityId": self._entityId,
                "template": self._template,
            }
        )
        return common

    def asTemplate(self) -> FeatureTemplate:
        raise ValueError("No templates for row features yet")


def featuresDecoder(features_dictionary_list):

    try:
        validate(features_dictionary_list, features_schema)
    except ValidationError:
        logger.error("Unable to validate schema {schema} "
                     "for features dictionary {d}".format(
                         schema=features_schema,
                         d=features_dictionary_list))
        raise

    return [
        Feature.from_dict(feature_dict) for feature_dict
        in features_dictionary_list
    ]


class EventFeatures(FeatureTemplate):
    def __init__(
        self,
        name: str,
        description: str,
        table: str,
        window: Window,
        select: SelectExpression,
        filter: Optional[FilterExpression],
        aggregate: Optional[Aggregation],
        postAggregateExpr: Optional[PostAggregateExpression],
        id: Optional[int] = None
    ):
        super().__init__(name, description, id)
        self._table = table
        self._window = window
        self._select = select
        self._filter = filter
        self._aggregate = aggregate
        self._postAggregateExpr = postAggregateExpr

    def __eq__(self, other):
        if not isinstance(other, EventFeatures):
            return NotImplemented
        return (
            self._id,
            self._name,
            self._description,
            self._table,
            self._window,
            self._select,
            self._filter,
            self._aggregate,
            self._postAggregateExpr,
        ) == (
            other._id,
            other._name,
            other._description,
            other._table,
            other._window,
            other._select,
            other._filter,
            other._aggregate,
            other._postAggregateExpr,
        )

    def __repr__(self):
        reprstr = """EventFeatures(id={id}, name={name}, description={desc},"""
        reprstr += """ table={table}, window={window}, select={select}, """
        reprstr += """filter={filter}, aggregate={aggr}, """
        reprstr += """postAggregateExpr={postaggr})"""
        return reprstr.format(id=self._id, name=self._name,
                              desc=self._description, table=self._table,
                              window=self._window, select=self._select,
                              filter=self._filter, aggr=self._aggregate,
                              postaggr=self._postAggregateExpr)

    def to_dict(self):
        common = self._toDictionaryCommon()
        common.update(
            {
                "adt_type": "event",
                "table": self._table,
                "window": self._window.to_json(),
                "select": self._select.to_dict(),
                "filter":
                    None if not self._filter else self._filter.to_dict(),
                "aggregate":
                    None if not self._aggregate
                    else self._aggregate.to_dict(),
                "postAggregateExpr":
                    None if not self._postAggregateExpr
                    else self._postAggregateExpr.to_dict()
            }
        )
        return common

    def asTemplate(self) -> FeatureTemplate:
        return self


class GeneratedFeatures(ABC):
    def __init__(self, id: str, date: datetime.date, features: dict):
        self._id = id
        self._date = date
        self._features = features

    def __eq__(self, other):
        if not isinstance(other, GeneratedFeatures):
            return NotImplemented
        return (
            self._id,
            self._date,
            self._features
        ) == (
            other._id,
            other._date,
            other._features
        )

    def __repr__(self):
        reprstr = """GeneratedFeatures(id={id}, date={date}, """
        reprstr += """features={features})"""
        return reprstr.format(id=self._id, date=self._date,
                              features=self._features)

    def to_dict(self) -> dict:
        return {
            "id": self._id,
            "date": self._date.isoformat(),
            "features": self._features,
        }

    @classmethod
    def schema(cls):
        return generated_features_schema

    @classmethod
    def from_json(cls, d: dict):
        try:
            validate(d, cls.schema())
        except ValidationError:
            logger.error("Unable to validate schema {schema} "
                         "from dict {d}".format(schema=cls.schema(), d=d))
            raise

        return cls.from_dict(d)

    @classmethod
    def from_dict(cls, generated_features_dict: dict):
        return GeneratedFeatures(
            generated_features_dict.get("id"),
            datetime.date.fromisoformat(generated_features_dict.get("date")),
            generated_features_dict.get("features"),
        )
