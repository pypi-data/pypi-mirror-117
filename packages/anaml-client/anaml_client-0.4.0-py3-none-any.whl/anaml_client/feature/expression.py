#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#
"""Data-types for Anaml SQL expressions."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from .schema import select_schema
from ..model import AnamlBaseClass


@dataclass(frozen=True)
class SelectExpression(AnamlBaseClass):
    """SQL Expression for aggregating the feature data."""

    sql: str

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for SQL expression objects."""
        return select_schema

    @classmethod
    def from_dict(cls, d: dict) -> SelectExpression:
        """Parse an SQL expression from valid JSON data."""
        return cls(d["sql"])


@dataclass(frozen=True)
class FilterExpression(AnamlBaseClass):
    """SQL Expression for filtering the feature data."""

    sql: str

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for SQL expression objects."""
        return select_schema

    @classmethod
    def from_dict(cls, d: dict) -> FilterExpression:
        """Parse an SQL expression from valid JSON data."""
        return cls(d["sql"])


@dataclass(frozen=True)
class PostAggregateExpression(AnamlBaseClass):
    """SQL Expression for aggregating the feature data."""

    sql: str

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for SQL expression objects."""
        return select_schema

    @classmethod
    def from_dict(cls, d: dict) -> PostAggregateExpression:
        """Parse an SQL expression from valid JSON data."""
        return cls(d["sql"])
