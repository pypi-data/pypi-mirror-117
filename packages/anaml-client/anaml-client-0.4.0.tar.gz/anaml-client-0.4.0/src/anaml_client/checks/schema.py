#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""JSON schemas for checks."""

from ..model.schema import instant_field, json_optional

"""JSON Schema for fields containing CheckStatus values."""
check_status_field = {
    "type": "string",
    "enum": ["pending", "running", "completed"]
}

"""JSON Schema for fields containing CheckConclusion values."""
check_conclusion_field = {
    "type": ["string"],
    "enum": ["cancelled", "failure", "success", "skipped", "timedout", None]
}

check_components_schema = check_schema = {
    "type": "object",
    "properties": {
        "key": {
            "type": "string"
        },
        "value": {
            "type": "string"
        }
    }
}

check_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "commit": {
            "type": "string"
        },
        "created_by": {
            "type": "integer"
        },
        "started": instant_field,
        "completed": json_optional(instant_field),
        "status": check_status_field,
        "components": {"type": "array", "items": check_components_schema},
        "conclusion": json_optional(check_conclusion_field),
        "details_url": {
            "type": ["string", "null"]
        }
    },
    "required": [
        "name",
        "commit",
        "created_by",
        "status"
    ]
}
