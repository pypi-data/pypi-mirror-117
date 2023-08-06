#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""JSON Schemas for Anaml Merge Requests."""

from ..model.schema import timestamp_field

merge_request_schema = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "author": {
            "type": "integer"
        },
        "comment": {
            "type": "string"
        },
        "source": {
            "type": "string"
        },
        "target": {
            "type": "string"
        },
        "status": {
            "type": "string",
            "enum": ["open", "closed", "merged"]
        },
        "mergeCommit": {
            "type": ["string", "null"]
        },
        "created": timestamp_field,
        "modified": timestamp_field
    },
    "required": [
        "name",
        "author",
        "source",
        "target",
        "status"
    ]
}
