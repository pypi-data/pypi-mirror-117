#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#

"""JSON Schema definitions for feature definitions and related objects."""

from anaml_client.statistics import feature_statistics

data_type_schema = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["int", "string", "bigint", "double", "float",
                     "date", "timestamp"]
        }
    },
    "required": ["adt_type"]
}

aggregate_schema = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["sum", "count", "countdistinct", "avg", "std",
                     "last", "percentagechange", "absolutechange",
                     "standardscore"]
        }
    },
    "required": ["adt_type"]
}

post_aggregate_schema = {
    "type": "object",
    "properties": {
        "sql": {"type": "string"}
    },
    "required": ["sql"]
}

# {'days': 14, 'adt_type': 'daywindow'}
window_schema = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string",
                     "enum": ["openwindow", "daywindow", "rowwindow"]}
    },
    "required": ["adt_type"],
    "allOf": [
        {
            "if": {"properties": {"adt_type": {"const": "daywindow"}}},
            "then": {"properties": {"days": {"type": "integer"}}}
        },
        {
            "if": {"properties": {"adt_type": {"const": "rowwindow"}}},
            "then": {"properties": {"rows": {"type": "integer"}}}
        }
    ]
}

select_schema = {
    "type": "object",
    "properties": {"sql": {"type": "string"}}
}

filter_schema = {
    "type": ["null", "object"],
    "properties": {"sql": {"type": "string"}}
}

feature_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "adt_type": {"type": "string", "enum": ["event", "row"]}
    },
    "required": ["name", "adt_type"],
    "allOf": [
        {
            "if": {"properties": {"adt_type": {"const": "event"}}},
            "then": {
                "properties": {
                    "table": {"type": "integer"},
                    "window": window_schema,
                    "select": select_schema,
                    "filter": filter_schema,
                    "aggregate": aggregate_schema,
                    "postAggregateExpr": {"anyOf": [{"type": "null"},
                                          post_aggregate_schema]}
                },
                "required": ["table", "window", "select", "aggregate"]
            }
        },
        {
            "if": {"properties": {"adt_type": {"const": "row"}}},
            "then": {
                "properties": {
                    "entityId": {"type": "integer"},
                    "select": select_schema,
                    "over": {"type": "array", "items": {"type": "integer"}}
                },
                "required": ["over", "select", "entityId"]
            }
        }
    ]
}

feature_template_schema_event = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["event"]},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "table": {"type": "integer"},
        "select": select_schema,
        "filter": filter_schema,
        "aggregate": {"anyOf": [{"type": "null"}, aggregate_schema]},
        "postAggregateExpr": {"anyOf": [{"type": "null"}, post_aggregate_schema]}
    },
    "required": ["adt_type", "id", "name", "table", "select"]
}

feature_template_schema_row = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["row"]},
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "over": {"type": "array", "items": {"type": "integer"}},
        "select": select_schema,
        "entityId": {"type": "integer"},
    },
    "required": ["adt_type", "id", "name", "over", "select", "entityId"]
}

feature_template_schema = {
    "allOf": [
        {
            "type": "object",
            "properties": {
                "adt_type": {"type": "string", "enum": ["event", "row"]},
                "id": {"type": "integer"},
                "name": {"type": "string"},
                "description": {"type": "string"},
            },
            "required": ["adt_type", "id", "name"]
        },
        {
            "oneOf": [
                feature_template_schema_event,
                feature_template_schema_row,
            ]
        }
    ],
}

features_schema = {"type": "array", "items": feature_schema}

generated_features_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string"},
        "date": {"type": "string", "format": "date"},
        "features": {"type": "object", "additionalProperties": True}
    },
    "required": ["id", "date", "features"]
}

feature_run_summary_schema = {
    "FeatureRunSummary": {
        "required": [
            "featureStore",
            "featureRun",
            "runStartDate",
            "runEndDate",
            "runTime",
            "stats"
        ],
        "properties": {
            "runTime": {
                "format": "date-time",
                "description": "A date time as per RFC 3339",
                "type": "string"
            },
            "stats": feature_statistics,
            "featureStore": {"type": "integer"},
            "featureRun": {"type": "integer"},
            "runStartDate": {
                "format": "date",
                "description": "A date as per RFC 3339",
                "type": "string"
            },
            "runEndDate": {
                "format": "date",
                "description": "A date as per RFC 3339",
                "type": "string"
            }
        },
        "type": "object"
    }}
