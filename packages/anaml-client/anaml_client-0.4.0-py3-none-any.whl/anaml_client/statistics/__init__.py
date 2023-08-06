#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Data types for Anaml statistics."""

from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import ClassVar, Type, Optional, List

from .schema import (
    feature_statistics,
    numerical_feature_statistics,
    categorical_feature_statistics,
    empty_feature_statistics,
    default_feature_statistics,
    category_frequency, execution_statistics_schema, task_statistics_schema
)
from ..utils import map_opt, parse_bool
from ..utils.serialisation import AnamlBaseClass


@dataclass(frozen=True)
class SummaryStatistics(AnamlBaseClass):
    """Abstract class representing Anaml summary statistics."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    featureName: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for summary statistics objects."""
        return feature_statistics

    @classmethod
    def from_dict(cls: Type[SummaryStatistics], data: dict) -> SummaryStatistics:
        """Parse a summary statistics object from valid JSON data."""
        adt_type = data.get('adt_type', None)
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse JSON for cluster: Unknown adt_type '{adt_type}'")


@dataclass(frozen=True)
class NumericalSummaryStatistics(SummaryStatistics):
    """Summary stats for a numerical column."""

    ADT_TYPE: ClassVar[str] = "numerical"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    count: int
    min: float
    max: float
    stdDev: float
    mean: float
    quantiles: List[float]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for numerical summary statistics objects."""
        return numerical_feature_statistics

    @classmethod
    def from_dict(cls: Type[NumericalSummaryStatistics], data: dict) -> NumericalSummaryStatistics:
        """Parse a numerical summary statistics object from valid JSON data."""
        return NumericalSummaryStatistics(
            featureName=data['featureName'],
            count=data['count'],
            min=data['min'],
            max=data['max'],
            mean=data['mean'],
            stdDev=data['stdDev'],
            quantiles=data['quantiles'],
        )


@dataclass(frozen=True)
class CategoryFrequency(AnamlBaseClass):
    """Metadata attributes."""

    category: str
    frequency: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for category frequency objects."""
        return category_frequency

    @classmethod
    def from_dict(cls: Type[CategoryFrequency], data: dict) -> CategoryFrequency:
        """Parse a category frequency object from valid JSON data."""
        return CategoryFrequency(
            category=data['category'],
            frequency=data['frequency']
        )


@dataclass(frozen=True)
class CategoricalSummaryStatistics(SummaryStatistics):
    """Summary stats for a numerical column."""

    ADT_TYPE: ClassVar[str] = "categorical"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    count: int
    categoryFrequencies: List[CategoryFrequency]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for categorical summary statistics objects."""
        return categorical_feature_statistics

    @classmethod
    def from_dict(cls: Type[CategoricalSummaryStatistics], data: dict) -> CategoricalSummaryStatistics:
        """Parse a categorical summary statistics object from valid JSON data."""
        return CategoricalSummaryStatistics(
            featureName=data['featureName'],
            count=data['count'],
            categoryFrequencies=[
                CategoryFrequency(category=i['category'], frequency=i['frequency'])
                for i in data['categoryFrequencies']
            ],
        )


@dataclass(frozen=True)
class DefaultSummaryStatistics(SummaryStatistics):
    """Summary stats for a numerical column."""

    ADT_TYPE: ClassVar[str] = "default"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    count: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for default summary statistics objects."""
        return default_feature_statistics

    @classmethod
    def from_dict(cls: Type[DefaultSummaryStatistics], data: dict) -> DefaultSummaryStatistics:
        """Parse a default summary statistics object from valid JSON data."""
        return DefaultSummaryStatistics(
            featureName=data['featureName'],
            count=data['count'],
        )


@dataclass(frozen=True)
class EmptySummaryStatistics(SummaryStatistics):
    """Summary stats for a numerical column."""

    ADT_TYPE: ClassVar[str] = "empty"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for empty summary statistics objects."""
        return empty_feature_statistics

    @classmethod
    def from_dict(cls: Type[EmptySummaryStatistics], data: dict) -> EmptySummaryStatistics:
        """Parse an empty statistics object from valid JSON data."""
        return EmptySummaryStatistics(
            featureName=data['featureName'],
        )


@dataclass(frozen=True)
class ExecutionStatistics(AnamlBaseClass):
    """Execution statistics for jobs."""

    executionStartTime: datetime.datetime
    executionEndTime: Optional[datetime.datetime] = None

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for execution statistics objects."""
        return execution_statistics_schema

    @classmethod
    def from_dict(cls: Type[ExecutionStatistics], data: dict) -> ExecutionStatistics:
        """Parse an execution statistics object from valid JSON data."""
        return ExecutionStatistics(
            executionStartTime=datetime.datetime.strptime(data['executionStartTime'], "%Y-%m-%dT%H:%M:%S.%f%z"),
            executionEndTime=map_opt(
                data.get('executionEndTime', None),
                lambda s: datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.%f%z")
            )
        )

    def to_dict(self) -> dict:
        """Override the JSON serialisation of execution statistics."""
        return {
            "executionStartTime": self.executionStartTime.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "executionEndTime": map_opt(self.executionEndTime, lambda d: d.strftime("%Y-%m-%dT%H:%M:%S.%f%z"))
        }


@dataclass(frozen=True)
class TaskStatistics(AnamlBaseClass):
    """Statistics describing the execution of one task during a job run."""

    stageId: int
    stageAttemptId: int
    taskType: str
    index: int
    taskId: int
    attemptNumber: int
    launchTime: int
    finishTime: int
    duration: int
    schedulerDelay: int
    executorId: str
    host: str
    taskLocality: str
    speculative: bool
    gettingResultTime: int
    successful: bool
    executorRunTime: int
    executorCpuTime: int
    executorDeserializeTime: int
    executorDeserializeCpuTime: int
    resultSerializationTime: int
    jvmGCTime: int
    resultSize: int
    numUpdatedBlockStatuses: int
    diskBytesSpilled: int
    memoryBytesSpilled: int
    peakExecutionMemory: int
    recordsRead: int
    bytesRead: int
    recordsWritten: int
    bytesWritten: int
    shuffleFetchWaitTime: int
    shuffleTotalBytesRead: int
    shuffleTotalBlocksFetched: int
    shuffleLocalBlocksFetched: int
    shuffleRemoteBlocksFetched: int
    shuffleWriteTime: int
    shuffleBytesWritten: int
    shuffleRecordsWritten: int
    statusMessage: Optional[str] = None

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for task statistics objects."""
        return task_statistics_schema

    @classmethod
    def from_dict(cls: Type[TaskStatistics], data: dict) -> TaskStatistics:
        """Parse a task statistics object from valid JSON data."""
        return TaskStatistics(
            stageId=int(data["stageId"]),
            stageAttemptId=int(data["stageAttemptId"]),
            taskType=data["taskType"],
            index=int(data["index"]),
            taskId=int(data["taskId"]),
            attemptNumber=int(data["attemptNumber"]),
            launchTime=int(data["launchTime"]),
            finishTime=int(data["finishTime"]),
            duration=int(data["duration"]),
            schedulerDelay=int(data["schedulerDelay"]),
            executorId=data["executorId"],
            host=data["host"],
            taskLocality=data["taskLocality"],
            speculative=parse_bool(data["speculative"]),
            gettingResultTime=int(data["gettingResultTime"]),
            successful=parse_bool(data["successful"]),
            executorRunTime=int(data["executorRunTime"]),
            executorCpuTime=int(data["executorCpuTime"]),
            executorDeserializeTime=int(data["executorDeserializeTime"]),
            executorDeserializeCpuTime=int(data["executorDeserializeCpuTime"]),
            resultSerializationTime=int(data["resultSerializationTime"]),
            jvmGCTime=int(data["jvmGCTime"]),
            resultSize=int(data["resultSize"]),
            numUpdatedBlockStatuses=int(data["numUpdatedBlockStatuses"]),
            diskBytesSpilled=int(data["diskBytesSpilled"]),
            memoryBytesSpilled=int(data["memoryBytesSpilled"]),
            peakExecutionMemory=int(data["peakExecutionMemory"]),
            recordsRead=int(data["recordsRead"]),
            bytesRead=int(data["bytesRead"]),
            recordsWritten=int(data["recordsWritten"]),
            bytesWritten=int(data["bytesWritten"]),
            shuffleFetchWaitTime=int(data["shuffleFetchWaitTime"]),
            shuffleTotalBytesRead=int(data["shuffleTotalBytesRead"]),
            shuffleTotalBlocksFetched=int(data["shuffleTotalBlocksFetched"]),
            shuffleLocalBlocksFetched=int(data["shuffleLocalBlocksFetched"]),
            shuffleRemoteBlocksFetched=int(data["shuffleRemoteBlocksFetched"]),
            shuffleWriteTime=int(data["shuffleWriteTime"]),
            shuffleBytesWritten=int(data["shuffleBytesWritten"]),
            shuffleRecordsWritten=int(data["shuffleRecordsWritten"]),
            statusMessage=data.get('statusMessage', None)
        )
