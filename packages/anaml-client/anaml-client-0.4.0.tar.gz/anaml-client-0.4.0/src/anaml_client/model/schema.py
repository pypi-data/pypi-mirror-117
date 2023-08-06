#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""JSON Schemas representing a range of Anaml resources."""


def json_list(ty: dict) -> dict:
    """Make a JSON Schema into a list."""
    return {"type": "array", "items": ty}


def json_optional(ty: dict) -> dict:
    """Make a JSON Schema optional."""
    return {"anyOf": [ty, {"type": "null"}]}


"""JSON Schema for fields containing java.time.Instant values."""
instant_field = {
    # Scala type: Instant
    "type": "string",
    "format": "date-time"
}

"""JSON Schema for fields containing java.sql.Timestamp values."""
timestamp_field = {
    # Example: 2021-08-03 10:31:27.721194
    "type": "string",
    "pattern": "^([0-9]{4}-[0-9]{2}-[0-9]{2}) ([0-9]{2}:[0-9]{2}:[0-9]{2}([.][0-9]+)?)$"
}

"""JSON Schema for fields containing LocalDate values."""
localdate_field = {
    # Scala type: LocalDate
    "type": "string",
    "format": "full-date",
}

"""JSON Schema for fields containing LocalTime values."""
localtime_field = {
    "type": "string",
    # Can't use format=full-time due to lack of an offset.
    "pattern": "^([0-9]{2})(:[0-9]{2})(:[0-9]{2}([.][0-9]+)?)?$",
}

"""JSON Schema for version fields containing a UUID."""
version_field = {
    "type": "string",
    "format": "uuid"
}

"""JSON Schema for common Labels metadata field."""
labels_field = json_list(
    {"type": "string"}
)

"""JSON Schema for common Attributes metadata field."""
attributes_field = json_list(
    {
        "type": "object",
        "properties": {
            "key": {"type": "string"},
            "value": {"type": "string"}
        },
        "required": ["key", "value"]
    }
)

quality_rating_field = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["gold", "silver", "bronze"]
        }
    },
    "required": ["adt_type"]
}

"""JSON Schema for commit objects."""
commit_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "string", "format": "uuid"},
        "parents": {"type": "array", "items": {"type": "string", "format": "uuid"}},
        "createdAt": timestamp_field,
        "author": {"type": "integer"},
        "description": json_optional({"type": "string"})
    }
}

"""JSON Schema for fields containing file-format configuration values."""
file_format_field = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["parquet", "orc", "csv"]
        },
        "includeHeader": {
            "type": "boolean",
        }
    },
    "required": ["adt_type"]
}

"""JSON Schema for secret configuration using a basic 'hard-coded' secret value."""
basic_secrets_config = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["basic"]},
        "secret": {"type": "string"}
    },
    "required": ["adt_type", "secret"]
}

"""JSON Schema for secret configuration using AWS Secret Manager."""
aws_secrets_config = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["awssm"]},
        "secretId": {"type": "string"}
    },
    "required": ["adt_type", "secretId"]
}

"""JSON Schema for secret configuration using GCP Secret Manager."""
gcp_secrets_config = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["gcpsm"]},
        "secretProject": {"type": "string"},
        "secretId": {"type": "string"}
    },
    "required": ["adt_type", "secretProject", "secretId"]
}

"""JSON Schema for fields containing secrets configuration."""
secrets_config_field = {
    # SecretsConfig sealed trait.
    "oneOf": [
        basic_secrets_config,
        aws_secrets_config,
        gcp_secrets_config,
    ]
}

"""JSON Schema for fields containing credentials provider configuration."""
credentials_provider_config_field = {
    # CredentialsProviderConfig case class
    "type": "object",
    "properties": {
        # This should be DRYed up w.r.t. secrets_config_field.
        "adt_type": {
            "type": "string",
            "enum": ["basic", "awssm", "gcpsm"]
        },
        "username": {"type": "string"},
        "password": {"type": "string"},
        "passwordSecretId": {"type": "string"},
        "passwordSecretProject": {"type": "string"}
    },
    "required": ["adt_type", "username"]
}

"""JSON Schema for fields containing sensitive attribute configuration information."""
sensitive_attribute_field = {
    "type": "object",
    "properties": {
        "key": {"type": "string"},
        "valueConfig": secrets_config_field
    },
    "required": ["key", "valueConfig"]
}

"""JSON Schema for version targets specifying a CommitId."""
commit_target = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["commit"]},
        "commitId": {"type": "string", "format": "uuid"}
    },
    "required": ["adt_type", "commitId"]
}

"""JSON Schema for version targets specifying a BranchName."""
branch_target = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["branch"]},
        "branchName": {"type": "string"}
    },
    "required": ["adt_type", "branchName"]
}

"""JSON Schema for a version target."""
version_target_field = {
    "oneOf": [commit_target, branch_target]
}

fixed_retry_policy = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["fixed"]},
        "backoff": {"type": "string"},
        "maxAttempts": {"type": "integer"}
    },
    "required": ["adt_type"]
}

never_retry_policy = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["never"]}
    },
    "required": ["adt_type"]
}

retry_policy_field = {
    "oneOf": [
        fixed_retry_policy,
        never_retry_policy
    ]
}

daily_schedule = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["daily"]},
        "startTimeOfDay": json_optional(localtime_field),
        "retryPolicy": retry_policy_field
    },
    "required": ["adt_type", "retryPolicy"]
}

cron_schedule = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["cron"]},
        "cronString": {"type": "string"},
        "retryPolicy": retry_policy_field
    },
    "required": ["adt_type", "cronString", "retryPolicy"]
}

never_schedule = {
    "type": "object",
    "properties": {
        "adt_type": {"type": "string", "enum": ["never"]},
    },
    "required": ["adt_type"]
}

schedule_field = {
    "oneOf": [
        daily_schedule,
        cron_schedule,
        never_schedule
    ]
}

schedule_state_field = {
    "type": "object",
    "properties": {
        "schedule": schedule_field,
        "scheduledStartTime": instant_field,
        "retryCount": {"type": "integer"}
    },
    "required": [
        "schedule",
        "scheduledStartTime",
        "retryCount"
    ],
}

run_status_field = {
    # RunStatus sealed trait.
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["pending", "running", "completed", "failed"]
        }
    },
    "required": ["adt_type"]
}

feature_store_execution_statistics_schema = {
    "type": "object",

}

feature_store_run_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "created": instant_field,
        "featureStoreId": {"type": "integer"},
        "featureStoreVersionId": version_field,
        "commitId": version_field,
        "runStartDate": localdate_field,
        "runEndDate": localdate_field,
        "status": run_status_field,
        "errorMessage": json_optional({"type": "string"}),
        "scheduleState": json_optional(schedule_state_field)
    },
    "required": [
        "id",
        "created",
        "featureStoreId",
        "featureStoreVersionId",
        "commitId",
        "runStartDate",
        "runEndDate",
        "status",
    ],
}

folder_destination_reference = {
    "type": "object",
    "properties": {
        "destinationId": {"type": "integer"},
        "folder": {"type": "string"}
    },
    "required": ["destinationId", "folder"]
}

table_destination_reference = {
    "type": "object",
    "properties": {
        "destinationId": {"type": "integer"},
        "tableName": {"type": "string"}
    },
    "required": ["destinationId", "tableName"]
}

topic_destination_reference = {
    "type": "object",
    "properties": {
        "destinationId": {"type": "integer"},
        "topic": {"type": "string"}
    },
    "required": ["destinationId", "topic"]
}

destination_reference_field = {
    "oneOf": [
        folder_destination_reference,
        table_destination_reference,
        topic_destination_reference
    ]
}

feature_store_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "labels": labels_field,
        "attributes": attributes_field,
        "featureSet": {"type": "integer"},
        "enabled": {"type": "boolean"},
        "destinations": json_list(destination_reference_field),
        "cluster": {"type": "integer"},
        "schedule": schedule_field,
        "startDate": json_optional(localtime_field),
        "endDate": json_optional(localtime_field),
        "versionTarget": json_optional(version_target_field),
        "version": version_field,
    },
    "required": [
        "id", "name", "description", "labels", "attributes", "featureSet", "enabled",
        "destinations", "cluster", "schedule", "version"
    ]
}

feature_set_schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "description": {"type": "string"},
        "features": json_list({"type": "integer"})
    },
    "required": ["id", "name", "description", "features"]
}

folder_source_reference_schema = {
    "type": "object",
    "properties": {
        "sourceId": {"type": "integer"},
        "folder": {"type": "string"}
    },
    "required": ["sourceId", "folder"]
}

table_source_reference_schema = {
    "type": "object",
    "properties": {
        "sourceId": {"type": "integer"},
        "tableName": {"type": "string"}
    },
    "required": ["sourceId", "tableName"]
}

topic_source_reference_schema = {
    "type": "object",
    "properties": {
        "sourceId": {"type": "integer"},
        "topic": {"type": "string"}
    },
    "required": ["sourceId", "topic"]
}

source_reference_schema = {
    "allOf": [
        {
            "type": "object",
            "properties": {
                "sourceId": {"type": "integer"}
            },
            "required": ["sourceId"]
        },
        {
            "oneOf": [
                folder_source_reference_schema,
                table_source_reference_schema,
                topic_source_reference_schema,
            ]
        }
    ]
}
