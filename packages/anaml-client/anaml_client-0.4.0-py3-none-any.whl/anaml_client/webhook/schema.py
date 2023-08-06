#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""JSON Schema definitions for webhook events."""

run_status_field = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["pending", "running", "completed", "failed"]
        }
    },
    "required": ["adt_type"]
}

feature_store_run_event = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["featurestorerun"]},
        "featureStore": {"type": "integer"},
        "run": {"type": "integer"},
        "status": run_status_field
    },
    "required": ["adt_type", "featureStore", "run", "status"]
}

caching_run_event = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["cachingrun"]},
        "job": {"type": "integer"},
        "run": {"type": "integer"},
        "status": run_status_field
    },
    "required": ["adt_type", "job", "run", "status"]
}

monitoring_run_event = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["monitoringrun"]},
        "job": {"type": "integer"},
        "run": {"type": "integer"},
        "status": run_status_field
    },
    "required": ["adt_type", "job", "run", "status"]
}

merge_request_accepted_event = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["mergerequestaccepted"]},
        "id": {"type": "integer"},
    },
    "required": ["adt_type", "id"]
}

new_commit_event = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["newcommit"]},
        "id": {"type": "string", "format": "uuid"},
        "branch": {"type": ["string", "null"]}
    },
    "required": ["adt_type", "id"]
}

new_merge_request = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["newmergerequest"]},
        "id": {"type": "integer"},
    },
    "required": ["adt_type", "id"]
}

merge_request_comment = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["newmergerequestcomment"]},
        "id": {"type": "integer"},
        "commentId": {"type": "integer"},
    },
    "required": ["adt_type", "id", "commentId"]
}

webhook_event = {
    "anyOf": [
        feature_store_run_event,
        caching_run_event,
        monitoring_run_event,
        merge_request_accepted_event,
        new_commit_event,
        merge_request_comment,
        new_merge_request,
    ]
}
