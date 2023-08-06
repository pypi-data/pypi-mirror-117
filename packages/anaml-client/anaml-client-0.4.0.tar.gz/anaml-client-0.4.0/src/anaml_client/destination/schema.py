#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""JSON Schema definitions for destinations."""

from anaml_client.model.schema import (
    json_list,
    json_optional,
    attributes_field,
    version_field,
    labels_field,
    file_format_field,
    credentials_provider_config_field,
    sensitive_attribute_field
)


"""JSON Schema describing the GCS staging area for BigQuery destinations."""
gcs_staging_area = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["temporary", "persistent"]
        },
        "bucket": {"type": "string"},
        "path": {"type": "string"}
    },
    "required": ["adt_type", "bucket"]
}

"""Shared definition of the fields common to all destination types."""
_destination_common_fields = {
    "id": {"type": "integer"},
    "name": {"type": "string"},
    "description": {"type": "string"},
    "labels": labels_field,
    "attributes": attributes_field,
    "version": version_field,
    "predecessor": json_optional(version_field),
}

"""JSON Schema for a GCP BigQuery destination."""
bigquery_destination = {
    "type": "object",
    "required": ["adt_type", "path", "stagingArea"],

    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["bigquery"]},
        "path": {"type": "string"},
        "stagingArea": gcs_staging_area,
        "tableName": json_optional({"type": "string"})
    }
}

"""JSON Schema for a GCP Cloud Storage destination."""
gcs_destination = {
    "type": "object",
    "required": ["adt_type", "bucket", "path", "fileFormat"],

    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["gcs"]},
        "bucket": {"type": "string"},
        "path": {"type": "string"},
        "fileFormat": file_format_field,
        "folder": json_optional({"type": "string"})
    }
}

"""JSON Schema for a HDFS destination."""
hdfs_destination = {
    "type": "object",
    "required": ["adt_type", "path", "fileFormat"],

    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["hdfs"]},
        "path": {"type": "string"},
        "fileFormat": file_format_field,
        "folder": json_optional({"type": "string"})
    }
}

"""JSON Schema for a Hive table destination."""
hive_destination = {
    "type": "object",
    "required": ["adt_type", "database"],

    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["hive"]},
        "database": {"type": "string"},
        "tableName": json_optional({"type": "string"})
    }
}

"""JSON Schema for a JDBC database table destination."""
jdbc_destination_schema = {
    "type": "object",
    "required": ["adt_type", "url", "schema", "credentialsProvider"],
    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["jdbc"]},
        "url": {"type": "string"},
        "schema": {"type": "string"},
        "credentialsProvider": credentials_provider_config_field,
        "tableName": json_optional({"type": "string"})
    }
}

"""JSON Schema for a Kafka topic destination."""
kafka_destination = {
    "type": "object",
    "required": ["adt_type", "bootstrapServers", "schemaRegistryUrl", "kafkaPropertiesProviders"],
    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["kafka"]},
        "bootstrapServers": {"type": "string"},
        "schemaRegistryUrl": {"type": "string"},
        "kafkaPropertiesProviders": json_list(sensitive_attribute_field),
        "topic": json_optional({"type": "string"})
    }
}

"""JSON Schema for a local file destination."""
local_destination = {
    "type": "object",
    "required": ["adt_type", "path", "fileFormat"],
    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["local"]},
        "path": {"type": "string"},
        "fileFormat": file_format_field,
        "folder": json_optional({"type": "string"}),
    }
}

"""JSON Schema for a feature store destination."""
online_feature_store_destination = {
    "type": "object",
    "required": ["adt_type", "url", "schema", "credentialsProvider"],

    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["onlinefeaturestore"]},
        "url": {"type": "string"},
        "schema": {"type": "string"},
        "credentialsProvider": credentials_provider_config_field,
        "tableName": json_optional({"type": "string"})
    }
}

"""JSON Schema for an AWS S3 destination."""
s3_destination_schema = {
    "type": "object",
    "required": ["adt_type", "bucket", "path", "fileFormat"],
    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["s3"]},
        "bucket": {"type": "string"},
        "path": {"type": "string"},
        "fileFormat": file_format_field,
        "folder": json_optional({"type": "string"})
    }
}

"""JSON Schema for a Spark S3A destination."""
s3a_destination_schema = {
    "type": "object",
    "required": ["adt_type", "bucket", "path", "fileFormat", "endpoint", "accessKey", "secretKey"],
    "properties": {
        **_destination_common_fields,
        "adt_type": {"type": "string", "enum": ["s3a"]},
        "bucket": {"type": "string"},
        "path": {"type": "string"},
        "fileFormat": file_format_field,
        "folder": json_optional({"type": "string"}),
        "endpoint": {"type": "string"},
        "accessKey": {"type": "string"},
        "secretKey": {"type": "string"}
    }
}

"""JSON Schema for supported destinations."""
destination_schema = {
    "allOf": [
        # Require the basic destination fields...
        {
            "type": "object",
            "properties": {**_destination_common_fields},
            "required": ["id", "name", "description", "labels", "attributes"]
        },
        # ...plus the fields for exactly one destination type.
        {
            "oneOf": [
                bigquery_destination,
                gcs_destination,
                hdfs_destination,
                hive_destination,
                jdbc_destination_schema,
                local_destination,
                online_feature_store_destination,
                kafka_destination,
                s3_destination_schema,
                s3a_destination_schema,
            ]
        }
    ]
}
