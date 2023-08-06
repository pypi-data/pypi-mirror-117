"""JSON Schemas for cluster data types."""
from anaml_client.model.schema import labels_field, attributes_field, credentials_provider_config_field, json_optional

spark_config_schema = {
    "type": "object",
    "properties": {
        "enableHiveSupport": {"type": "boolean"},
        "hiveMetastoreUrl": json_optional({"type": "string"}),
        "additionalSparkProperties": {"type": "object"}
    },
    "required": ["enableHiveSupport", "additionalSparkProperties"],
}

local_cluster = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["local"],
        },
        "anamlServerUrl": {"type": "string"},
        "credentialsProvider": credentials_provider_config_field,
        "sparkConfig": spark_config_schema,
    },
    "required": ["adt_type", "anamlServerUrl", "credentialsProvider", "sparkConfig"]
}


sparkserver_cluster = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["sparkserver"],
        },
        "sparkServerUrl": {"type": "string"},
        "sparkConfig": spark_config_schema
    },
    "required": ["adt_type", "sparkServerUrl", "sparkConfig"]
}


cluster_schema = {
    "allOf": [
        {
            "type": "object",
            "required": ["adt_type", "name", "description", "labels", "attributes", "isPreviewCluster"],
            "properties": {
                "adt_type": {
                    "type": "string",
                    "enum": ["local", "sparkserver"]
                },
                "name": {"type": "string"},
                "description": {"type": "string"},
                "labels": labels_field,
                "attributes": attributes_field,
                "isPreviewCluster": {"type": "boolean"},
            },
        },
        {
            "oneOf": [
                local_cluster,
                sparkserver_cluster
            ]
        }
    ]
}
