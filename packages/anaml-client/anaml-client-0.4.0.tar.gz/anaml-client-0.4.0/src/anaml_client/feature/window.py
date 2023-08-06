#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#
"""Data-types for Anaml window expressions."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import ClassVar, Optional

from ..model import AnamlBaseClass
from .schema import window_schema


@dataclass(frozen=True)
class Window(AnamlBaseClass):
    """Base class for Anaml feature windows."""

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for window objects."""
        return window_schema

    @classmethod
    def from_dict(cls, d: dict) -> Window:
        """Parse a window from valid JSON data."""
        if d["adt_type"] == "rowwindow":
            return RowWindow(d["rows"])
        elif d["adt_type"] == "daywindow":
            return DayWindow(d["days"])
        elif d["adt_type"] == "openwindow":
            return OpenWindow()
        else:
            raise ValueError("Bad window specification")


@dataclass(frozen=True)
class OpenWindow(Window):
    """An open window."""

    ADT_TYPE: ClassVar[str] = "openwindow"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)


@dataclass(frozen=True)
class RowWindow(Window):
    """Window over a specified number of rows."""

    ADT_TYPE: ClassVar[str] = "rowwindow"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    rows: int


@dataclass(frozen=True)
class DayWindow(Window):
    """Window over a specified number of days."""

    ADT_TYPE: ClassVar[str] = "daywindow"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    days: int
