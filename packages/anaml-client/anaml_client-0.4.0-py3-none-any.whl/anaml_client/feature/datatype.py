#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#
"""Data-types to represent Anaml types."""

from abc import ABC, abstractmethod

from jsonschema import validate

from .schema import data_type_schema


class DataType(ABC):
    def __init__(self):
        pass

    def __repr__(self):
        return "DataType()"

    @abstractmethod
    def to_dict(self):
        pass

    @classmethod
    def from_json(cls, d):
        validate(d, data_type_schema)
        return cls.from_dict(d)

    @classmethod
    def from_dict(cls, d):
        if d["adt_type"] == "int":
            return IntType()
        elif d["adt_type"] == "string":
            return StringType()
        elif d["adt_type"] == "bigint":
            return LongType()
        elif d["adt_type"] == "double":
            return DoubleType()
        elif d["adt_type"] == "float":
            return FloatType()
        elif d["adt_type"] == "date":
            return DateType()
        elif d["adt_type"] == "timestamp":
            return TimestampType()
        else:
            raise ValueError("Bad window specification")


class IntType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "IntType()"

    def to_dict(self):
        return {"adt_type": "int"}


class StringType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "StringType()"

    def to_dict(self):
        return {"adt_type": "string"}


class LongType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "LongType()"

    def to_dict(self):
        return {"adt_type": "bigint"}


class DoubleType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "DoubleType()"

    def to_dict(self):
        return {"adt_type": "double"}


class FloatType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "FloatType()"

    def to_dict(self):
        return {"adt_type": "float"}


class DateType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "DateType()"

    def to_dict(self):
        return {"adt_type": "date"}


class TimestampType(DataType):
    def __init__(self):
        super().__init__()

    def __repr__(self):
        return "TimestampType()"

    def to_dict(self):
        return {"adt_type": "timestamp"}
