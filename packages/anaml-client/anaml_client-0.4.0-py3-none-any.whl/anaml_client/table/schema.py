#
#  Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
#  This file is part of Anaml.
#
#  Unauthorized copying and/or distribution of this file, via any medium
#  is strictly prohibited.
#

"""JSON schemas for table objects."""

from anaml_client.model.schema import (
    labels_field, json_optional, attributes_field, quality_rating_field, source_reference_schema
)

root_table_schema = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["root"],
        },
        "source": source_reference_schema,
    },
    "required": ["adt_type", "source"]
}

view_table_schema = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["view"],
        },
    },
    "required": ["adt_type"]
}

pivot_table_schema = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["pivot"],
        },
    },
    "required": ["adt_type"]
}

table_schema = {
    "allOf": [
        {
            "type": "object",
            "properties": {
                "adt_type": {"type": "string"},
                "id": json_optional({"type": "integer"}),
                "name": {"type": "string"},
                "description": json_optional({"type": "string"}),
                "labels": labels_field,
                "attributes": attributes_field,
                "qualityRating": json_optional(quality_rating_field),
                "version": {"type": "string", "format": "uuid"},
            },
            "required": ["adt_type", "name", "labels", "attributes", "version"]
        },
        {
            "oneOf": [
                pivot_table_schema,
                root_table_schema,
                view_table_schema,
            ]
        },
    ],
}
