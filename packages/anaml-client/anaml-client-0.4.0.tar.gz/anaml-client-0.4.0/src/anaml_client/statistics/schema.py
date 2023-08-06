#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""JSON Schemas definitions for statistics."""

from ..model.schema import json_list, json_optional, instant_field

numerical_feature_statistics = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["numerical"],
        },
        "featureName": {"type": "string"},
        "count": {"type": "integer"},
        "min": {"type": "number"},
        "max": {"type": "number"},
        "mean": {"type": "number"},
        "stdDev": {"type": "number"},
        "quantiles": json_list({"type": "number"}),
    },
    "required": ["adt_type", "featureName", "count", "min", "max", "mean", "stdDev", "quantiles"]
}


category_frequency = {
    "type": "object",
    "properties": {
        "category": {"type": "string"},
        "frequency": {"type": "integer"},
    },
    "required": ["category", "frequency"]
}

categorical_feature_statistics = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["categorical"],
        },
        "featureName": {"type": "string"},
        "count": {"type": "integer"},
        "categoryFrequencies": json_list(category_frequency)
    },
    "required": ["adt_type", "featureName", "count", "categoryFrequencies"]
}

default_feature_statistics = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["default"],
        },
        "featureName": {"type": "string"},
        "count": {"type": "integer"},
    },
    "required": ["adt_type", "featureName", "count"]
}

empty_feature_statistics = {
    "type": "object",
    "properties": {
        "adt_type": {
            "type": "string",
            "enum": ["empty"],
        },
        "featureName": {"type": "string"},
    },
    "required": ["adt_type", "featureName"]
}


feature_statistics = {
    "allOf": [
        {
            "type": "object",
            "required": ["adt_type", "featureName"],
            "properties": {
                "adt_type": {
                    "type": "string",
                    "enum": ["numerical", "categorical", "default", "empty"]
                },
                "featureName": {"type": "string"},
            },
        },
        {
            "oneOf": [
                numerical_feature_statistics,
                categorical_feature_statistics,
                default_feature_statistics,
                empty_feature_statistics
            ]
        }
    ]
}


execution_statistics_schema = {
    "type": "object",
    "properties": {
        "executionStartTime": instant_field,
        "executionEndTime": json_optional(instant_field)
    },
    "required": ["executionStartTime"]
}

task_statistics_schema = {
    "type": "object",
    "properties": {
        "stageId": {"type": "integer"},
        "stageAttemptId": {"type": "integer"},
        "taskType": {"type": "string"},
        "index": {"type": "integer"},
        "taskId": {"type": "integer"},
        "attemptNumber": {"type": "integer"},
        "launchTime": {"type": "integer"},
        "finishTime": {"type": "integer"},
        "duration": {"type": "integer"},
        "schedulerDelay": {"type": "integer"},
        "executorId": {"type": "string"},
        "host": {"type": "string"},
        "taskLocality": {"type": "string"},
        "speculative": {"type": "boolean"},
        "gettingResultTime": {"type": "integer"},
        "successful": {"type": "boolean"},
        "executorRunTime": {"type": "integer"},
        "executorCpuTime": {"type": "integer"},
        "executorDeserializeTime": {"type": "integer"},
        "executorDeserializeCpuTime": {"type": "integer"},
        "resultSerializationTime": {"type": "integer"},
        "jvmGCTime": {"type": "integer"},
        "resultSize": {"type": "integer"},
        "numUpdatedBlockStatuses": {"type": "integer"},
        "diskBytesSpilled": {"type": "integer"},
        "memoryBytesSpilled": {"type": "integer"},
        "peakExecutionMemory": {"type": "integer"},
        "recordsRead": {"type": "integer"},
        "bytesRead": {"type": "integer"},
        "recordsWritten": {"type": "integer"},
        "bytesWritten": {"type": "integer"},
        "shuffleFetchWaitTime": {"type": "integer"},
        "shuffleTotalBytesRead": {"type": "integer"},
        "shuffleTotalBlocksFetched": {"type": "integer"},
        "shuffleLocalBlocksFetched": {"type": "integer"},
        "shuffleRemoteBlocksFetched": {"type": "integer"},
        "shuffleWriteTime": {"type": "integer"},
        "shuffleBytesWritten": {"type": "integer"},
        "shuffleRecordsWritten": {"type": "integer"},
        "statusMessage": json_optional({"type": "string"})
    },
    "required": [
        "stageId",
        "stageAttemptId",
        "taskType",
        "index",
        "taskId",
        "attemptNumber",
        "launchTime",
        "finishTime",
        "duration",
        "schedulerDelay",
        "executorId",
        "host",
        "taskLocality",
        "speculative",
        "gettingResultTime",
        "successful",
        "executorRunTime",
        "executorCpuTime",
        "executorDeserializeTime",
        "executorDeserializeCpuTime",
        "resultSerializationTime",
        "jvmGCTime",
        "resultSize",
        "numUpdatedBlockStatuses",
        "diskBytesSpilled",
        "memoryBytesSpilled",
        "peakExecutionMemory",
        "recordsRead",
        "bytesRead",
        "recordsWritten",
        "bytesWritten",
        "shuffleFetchWaitTime",
        "shuffleTotalBytesRead",
        "shuffleTotalBlocksFetched",
        "shuffleLocalBlocksFetched",
        "shuffleRemoteBlocksFetched",
        "shuffleWriteTime",
        "shuffleBytesWritten",
        "shuffleRecordsWritten",
    ]
}
