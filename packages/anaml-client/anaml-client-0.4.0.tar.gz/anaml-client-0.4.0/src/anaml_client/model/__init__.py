#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Data types for the Anaml API."""

from __future__ import annotations

import enum
import logging

from dataclasses import dataclass, field
from datetime import datetime, date, timedelta, time
from typing import ClassVar, List, Optional, Tuple, Type
import uuid

import isodate


from .schema import (
    feature_store_run_schema,
    feature_store_schema, feature_set_schema,
    feature_store_execution_statistics_schema, schedule_state_field, schedule_field, never_schedule, daily_schedule,
    cron_schedule, retry_policy_field, never_retry_policy, fixed_retry_policy, version_target_field, branch_target,
    commit_target, destination_reference_field, topic_destination_reference, table_destination_reference,
    folder_destination_reference, credentials_provider_config_field, commit_schema, attributes_field, file_format_field,
    source_reference_schema,
)
from ..statistics import SummaryStatistics, ExecutionStatistics, TaskStatistics
from ..utils import parse_bool, map_opt
from ..utils.serialisation import AnamlBaseClass, TIMESTAMP_FORMAT, AnamlBaseEnum

logger = logging.getLogger(__name__)

#
# These data type declarations must be kept in sync with
# {repo_top}/common/src/main/scala/io/anaml/common/model
#
# Abbreviations for location clues:
#
# REPO = anaml-server/
# COMMON = anaml-server/common
# MODEL = anaml-server/common/src/main/scala/io/anaml/common/model
# PYCLIENT = anaml-server/python-client/src


@dataclass(frozen=True)
class Commit(AnamlBaseClass):
    """An Anaml commit."""

    id: uuid.UUID
    parents: List[uuid.UUID]
    createdAt: datetime
    author: int
    description: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for commit objects."""
        return commit_schema

    @classmethod
    def from_dict(cls: Type[Commit], data: dict) -> Commit:
        """Parse a commit object from valid JSON data."""
        return Commit(
            id=uuid.UUID(hex=data['id']),
            parents=[uuid.UUID(hex=p) for p in data.get('parents', [])],
            createdAt=datetime.strptime(data['createdAt'], TIMESTAMP_FORMAT),
            author=int(data['author']),
            description=data.get('description', None)
        )


#
# Entities $MODEL/EntityData.scala
# Attributes $MODEL/AttributeData.scala
#
Label = str
Attribute = Tuple[str, str]  # (key, value)

EntityId = int
EntityName = str
EntityVersionId = uuid.UUID


@dataclass(frozen=True)
class Ref:
    """A reference to a branch or commit."""

    ref_type: str = field(init=False, repr=False)
    ref: str

    @classmethod
    def branch(cls, name: str) -> BranchRef:
        """Return a branch reference."""
        return BranchRef(name)

    @classmethod
    def commit(cls, id: str) -> CommitRef:
        """Build a commit reference."""
        return CommitRef(id)


@dataclass(frozen=True)
class CommitRef(Ref):
    """A reference to a specific commit."""

    ref_type: str = field(init=False, repr=False, default="commit")


@dataclass(frozen=True)
class BranchRef(Ref):
    """A reference to a branch."""

    ref_type: str = field(init=False, repr=False, default="branch")


@dataclass(frozen=True)
class Entity(AnamlBaseClass):
    """An Anaml entity."""

    id: EntityId
    name: EntityName
    versionId: EntityVersionId
    description: str
    defaultColumn: str
    attributes: List[Attribute]
    labels: List[Label]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for entity objects."""
        # TODO: Add JSON schema.
        return None

    @classmethod
    def from_dict(cls, data: dict) -> Entity:
        """Parse an entity object from validated JSON data."""
        return Entity(
            id=data.get("id", None),
            name=data.get("name", None),
            versionId=uuid.UUID(hex=data.get("versionId")),
            description=data.get("description", None),
            defaultColumn=data.get("defaultColumn", None),
            attributes=data.get("attributes", []),
            labels=data.get("labels", [])
        )


#
# EntityMapping $MODEL/EntityMappingData.scala
#
EntityMappingId = int
EntityMappingVersionId = EntityVersionId

#
# Feature $MODEL/feature/Feature.scala
# all we're defining here is the FeatureId type, since everything else
# for a Feature is defined in $PYCLIENT/anaml_client/feature.
FeatureId = int

# We don't really care about a name for the mapping, so provide a dummy
# 'name' element to init the base class.
_defaultEntityMappingName = "entity mapping"


@dataclass(frozen=True)
class EntityMapping(AnamlBaseClass):
    """An Anaml entity mapping object."""

    id: EntityMappingId
    fromId: EntityId
    toId: EntityId
    mapping: FeatureId
    versionId: EntityMappingVersionId
    name: str

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for entity mapping objects."""
        # TODO: JSON schema for entity mapping
        return None

    @classmethod
    def from_dict(cls, data: dict) -> EntityMapping:
        """Parse an entity object from validated JSON data."""
        return EntityMapping(
            id=data.get("id", None),
            fromId=data.get("fromId", None),
            toId=data.get("toId", None),
            mapping=data.get("mapping", None),
            versionId=data.get("versionId", None),
            name=data.get("name", _defaultEntityMappingName)
        )


#
# QualityRating $MODEL/QualityRating.scala
#

@enum.unique
class QualityRating(AnamlBaseEnum):
    """Data asset quality ratings built in to Anaml."""

    GOLD = "gold"
    SILVER = "silver"
    BRONZE = "bronze"


#
# SourceData $MODEL/SourceData.scala
#
SourceId = int
SourceVersionId = uuid.UUID
SourceName = str


@dataclass(frozen=True)
class Source(AnamlBaseClass):
    """Data source supported by Anaml."""

    # TODO: Implement subtypes?

    id: SourceId
    name: SourceName
    description: str
    version: EntityVersionId
    predecessor: Optional[SourceVersionId]
    attributes: List[Attribute] = field(default_factory=list)
    labels: List[Label] = field(default_factory=list)

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for source objects."""
        return None

    @classmethod
    def from_dict(cls, data: dict) -> Source:
        """Parse a source object from valid JSON data."""
        return Source(
            id=data.get("id", None),
            name=data.get("name", None),
            description=data.get("description", None),
            version=data.get("version", uuid.uuid4()),
            predecessor=data.get("predecessor", None),
            attributes=data.get("attributes", []),
            labels=data.get("labels", [])
        )


@dataclass(frozen=True)
class SourceReference(AnamlBaseClass):
    """Reference to the data source for a table definition."""

    # TODO: Implement subtypes.

    sourceId: SourceId
    folder: Optional[str]
    table: Optional[str]
    topic: Optional[str]

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for source reference objects."""
        # TODO: JSON schema for source reference.
        return source_reference_schema

    @classmethod
    def from_dict(cls, data: dict) -> SourceReference:
        """Parse a source reference from valid JSON data."""
        return SourceReference(
            sourceId=data["sourceId"],
            folder=data.get("folder", None),
            table=data.get("table", None),
            topic=data.get("topic", None)
        )


@dataclass(frozen=True)
class Attribute(AnamlBaseClass):
    """Metadata attributes used throughout Anaml."""

    key: str
    value: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for attributes."""
        return attributes_field

    @classmethod
    def from_dict(cls: Type[Attribute], data: dict) -> Attribute:
        """Parse an attribute from valid JSON data."""
        return Attribute(
            key=data['key'],
            value=data['value']
        )


@dataclass(frozen=True)
class SensitiveAttribute:
    """Sensitive values, protected by a supported secrets mechanism."""

    key: str
    valueConfig: SecretsConfig

    # TODO: Validation for sensitive attribute.

    @classmethod
    def from_dict(cls, data: dict) -> SensitiveAttribute:
        """Parse a sensitive attribute from valid JSON data."""
        return SensitiveAttribute(
            data['key'],
            SecretsConfig.from_dict(data['valueConfig'])
        )


@dataclass(frozen=True)
class CredentialsProviderConfig(AnamlBaseClass):
    """Credentials for Anaml to use when accessing external services."""

    username: str
    secretsConfig: SecretsConfig

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for credentials."""
        return credentials_provider_config_field

    def to_json(self) -> dict:
        """Convert this credentials configuration to a JSON dictionary."""
        config = self.secretsConfig.to_json()
        config["username"] = self.username
        if "secret" in config:
            config["password"] = config["secret"]
            del config["secret"]
        return config

    @classmethod
    def from_dict(cls: Type[CredentialsProviderConfig], data: dict) -> CredentialsProviderConfig:
        """Parse credentials configuration from valid JSON data."""
        adt_type = data['adt_type']
        if 'basic' == adt_type:
            return CredentialsProviderConfig(
                username=data['username'],
                secretsConfig=BasicSecret(secret=data['password'])
            )
        elif 'awssm' == adt_type:
            return CredentialsProviderConfig(
                username=data['username'],
                secretsConfig=AWSSMSecret(secretId=data['passwordSecretId'])
            )
        elif 'gcpsm' == adt_type:
            return CredentialsProviderConfig(
                username=data['username'],
                secretsConfig=GCPSMSecret(
                    secretId=data['passwordSecretId'],
                    secretProject=data['passwordSecretProject'],
                )
            )
        else:
            raise ValueError(f"Cannot parse JSON for credentials provider config: unknown type {adt_type}")


@dataclass(frozen=True)
class SecretsConfig(AnamlBaseClass):
    """A secret value, possibly protected with a secret manager service."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for secret configuration."""
        # TODO: JSON schema for secrets config.
        return None

    @classmethod
    def from_dict(cls, data: dict) -> SecretsConfig:
        """Parse a secret configuration from valid JSON data."""
        # TODO: Refactor in line with new pattern for class-clusters.
        if 'basic' == data['adt_type']:
            return BasicSecret(data['secret'])
        elif 'awssm' == data['adt_type']:
            return AWSSMSecret(data['secretId'])
        elif 'gcpsm' == data['adt_type']:
            return GCPSMSecret(data['secretProject'], data['secretId'])
        else:
            raise ValueError("Unexpected secret config type {ty}".format(
                ty=data['adt_type']
            ))


@dataclass(frozen=True)
class BasicSecret(SecretsConfig):
    """A secret stored directly in an Anaml configuration object."""

    ADT_TYPE: ClassVar[str] = "basic"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    secret: str


@dataclass(frozen=True)
class GCPSMSecret(SecretsConfig):
    """Configuration for a secret stored in Google Cloud Platform Secret Manager."""

    ADT_TYPE: ClassVar[str] = "gcpsm"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    secretProject: str
    secretId: str


@dataclass(frozen=True)
class AWSSMSecret(SecretsConfig):
    """Configuration for a secret stored in AWS Secret Manager."""

    ADT_TYPE: ClassVar[str] = "awssm"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    secretId: str


@dataclass(frozen=True)
class FileFormat(AnamlBaseClass):
    """File formats supported by Anaml."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    @property
    def suffix(self):
        """Suffix for files in this format."""
        return f".{self.ADT_TYPE}"

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for file format values."""
        return file_format_field

    @classmethod
    def from_dict(cls, data: dict) -> FileFormat:
        """Parse a file format from valid JSON data."""
        # TODO: Refactor in line with new pattern for class-clusters.
        if 'orc' == data['adt_type']:
            return Orc()
        elif 'parquet' == data['adt_type']:
            return Parquet()
        elif 'csv' == data['adt_type']:
            return Csv(bool(data['includeHeader']))


@dataclass(frozen=True)
class Orc(FileFormat):
    """The ORC file format."""

    ADT_TYPE: ClassVar[str] = "orc"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)


@dataclass(frozen=True)
class Parquet(FileFormat):
    """The Parquet file format."""

    ADT_TYPE: ClassVar[str] = "parquet"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)


@dataclass(frozen=True)
class Csv(FileFormat):
    """The CSV file format."""

    ADT_TYPE: ClassVar[str] = "csv"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    includeHeader: bool


@enum.unique
class RunStatus(AnamlBaseEnum):
    """Status of Anaml job runs."""

    Pending = 'pending'
    Running = 'running'
    Completed = 'completed'
    Failed = 'failed'


@dataclass(frozen=True)
class FeatureStoreExecutionStatistics(AnamlBaseClass):
    """Statistics from a feature store execution job."""

    base: ExecutionStatistics
    featureCount: Optional[int]
    featureStatistics: List[SummaryStatistics]
    tasksStatistics: List[TaskStatistics]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for feature store execution statistics."""
        return feature_store_execution_statistics_schema

    @classmethod
    def from_dict(cls: Type[FeatureStoreExecutionStatistics], data: dict) -> FeatureStoreExecutionStatistics:
        """Parse feature store execution statistics from valid JSON data."""
        return FeatureStoreExecutionStatistics(
            base=ExecutionStatistics.from_dict(data['base']),
            featureCount=map_opt(data.get("featureCount", None), int),
            featureStatistics=[SummaryStatistics.from_dict(s) for s in data['featureStatistics']],
            tasksStatistics=[TaskStatistics.from_dict(s) for s in data['tasksStatistics']]
        )


@dataclass(frozen=True)
class RetryPolicy(AnamlBaseClass):
    """Retry policy for Anaml jobs."""

    ADT_TYPE: ClassVar[str] = ""

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for retry policy objects."""
        return retry_policy_field

    @classmethod
    def from_dict(cls: Type[RetryPolicy], data: dict) -> RetryPolicy:
        """Parse a retry policy from valid JSON data."""
        adt_type = data.get('adt_type', None)
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)
        raise ValueError(
            f"Could not parse JSON to RetryPolicy: unexpected adt_type {adt_type}"
        )


@dataclass(frozen=True)
class NeverRetryPolicy(RetryPolicy):
    """Never retry a failed job."""

    ADT_TYPE: ClassVar[str] = "never"

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for never retry policy."""
        return never_retry_policy

    @classmethod
    def from_dict(cls: Type[NeverRetryPolicy], data: dict) -> NeverRetryPolicy:
        """Parse a never retry policy from valid JSON data."""
        return NeverRetryPolicy()


@dataclass(frozen=True)
class FixedRetryPolicy(RetryPolicy):
    """Retry failed jobs according to a fixed backup policy."""

    ADT_TYPE: ClassVar[str] = "fixed"
    adt_type: str = field(init=False, repr=False, default=ADT_TYPE)

    backoff: timedelta
    maxAttempts: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for fixed retry policy."""
        return fixed_retry_policy

    @classmethod
    def from_dict(cls: Type[FixedRetryPolicy], data: dict) -> FixedRetryPolicy:
        """Parse a fixed retry policy from valid JSON data."""
        return FixedRetryPolicy(
            backoff=isodate.parse_duration(data['backoff']),
            maxAttempts=int(data['maxAttempts'])
        )


@dataclass(frozen=True)
class Schedule(AnamlBaseClass):
    """Schedule configuration for an Anaml job."""

    ADT_TYPE: ClassVar[str] = ""

    retryPolicy: RetryPolicy

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for schedule objects."""
        return schedule_field

    @classmethod
    def from_dict(cls: Type[Schedule], data: dict) -> Schedule:
        """Parse a schedule from valid JSON data."""
        adt_type = data['adt_type']
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)


@dataclass(frozen=True)
class DailySchedule(Schedule):
    """Schedule for jobs that should be run once daily."""

    ADT_TYPE: ClassVar[str] = "daily"
    adt_type: str = field(init=False, repr=False, default=ADT_TYPE)

    startTimeOfDay: time

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for daily schedule objects."""
        return daily_schedule

    @classmethod
    def from_dict(cls: Type[DailySchedule], data: dict) -> DailySchedule:
        """Parse a daily schedule from valid JSON data."""
        start_time_of_day = data.get('startTimeOfDay', None)
        if start_time_of_day:
            start_time_of_day = time.fromisoformat(start_time_of_day)
        return DailySchedule(
            startTimeOfDay=start_time_of_day,
            retryPolicy=RetryPolicy.from_dict(data['retryPolicy'])
        )


@dataclass(frozen=True)
class CronSchedule(Schedule):
    """Schedule for jobs that should be run according to an arbitrary cron expression."""

    ADT_TYPE: ClassVar[str] = "cron"

    cronString: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for cron schedule objects."""
        return cron_schedule

    @classmethod
    def from_dict(cls: Type[Schedule], data: dict) -> Schedule:
        """Parse a cron schedule from valid JSON data."""
        return CronSchedule(
            cronString=data['cronString'],
            retryPolicy=RetryPolicy.from_dict(data['retryPolicy'])
        )


@dataclass(frozen=True)
class NeverSchedule(Schedule):
    """Schedule for jobs that should not be run automatically."""

    ADT_TYPE: ClassVar[str] = "never"

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for never schedule objects."""
        return never_schedule

    @classmethod
    def from_dict(cls: Type[Schedule], data: dict) -> Schedule:
        """Parse a never schedule from valid JSON data."""
        return NeverSchedule(retryPolicy=NeverRetryPolicy())


@dataclass(frozen=True)
class ScheduleState(AnamlBaseClass):
    """State of an Anaml job run."""

    schedule: Schedule
    scheduledStartTime: datetime
    retryCount: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for a schedule state object."""
        return schedule_state_field

    @classmethod
    def from_dict(cls: Type[ScheduleState], data: dict) -> ScheduleState:
        """Parse a schedule state object from valid JSON data."""
        return ScheduleState(
            schedule=Schedule.from_dict(data['schedule']),
            scheduledStartTime=isodate.parse_datetime(data['scheduledStartTime']),
            retryCount=int(data['retryCount'])
        )


@dataclass(frozen=True)
class FeatureStoreRun(AnamlBaseClass):
    """Details of a feature store run."""

    id: int
    created: datetime
    featureStoreId: int
    featureStoreVersionId: uuid.UUID
    commitId: uuid.UUID
    runStartDate: date
    runEndDate: date
    status: RunStatus
    errorMessage: Optional[str]
    scheduleState: Optional[ScheduleState]
    statistics: Optional[FeatureStoreExecutionStatistics]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for feature store run objects."""
        return feature_store_run_schema

    def to_dict(self) -> dict:
        """Serialise to a dictionary of JSON data."""
        return {
            "id": self.id,
            "created": self.created.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            "featureStoreId": self.featureStoreId,
            "featureStoreVersionId": self.featureStoreVersionId,
            "commitId": self.commitId,
            "runStartDate": self.runStartDate,
            "runEndDate": self.runEndDate,
            "status": self.status,
            "errorMessage": self.errorMessage,
            "scheduleState": self.scheduleState,
            "statistics": self.statistics,
        }

    @classmethod
    def from_dict(cls: Type[FeatureStoreRun], data: dict) -> FeatureStoreRun:
        """Parse a feature store run from valid JSON data."""
        return FeatureStoreRun(
            id=int(data['id']),
            created=isodate.parse_datetime(data['created']),
            featureStoreId=int(data['featureStoreId']),
            featureStoreVersionId=uuid.UUID(data['featureStoreVersionId']),
            commitId=uuid.UUID(data['commitId']),
            runStartDate=date.fromisoformat(data['runStartDate']),
            runEndDate=date.fromisoformat(data['runEndDate']),
            status=RunStatus.from_dict(data['status']),
            errorMessage=data.get('errorMessage', None),
            scheduleState=map_opt(data.get('scheduleState', None), ScheduleState.from_dict),
            statistics=map_opt(data.get('statistics', None), FeatureStoreExecutionStatistics.from_dict)
        )


@dataclass(frozen=True)
class VersionTarget(AnamlBaseClass):
    """Version targeted by a feature store."""

    ADT_TYPE: ClassVar[str] = ""

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for version target objects."""
        return version_target_field

    @classmethod
    def from_dict(cls: Type[VersionTarget], data: dict) -> VersionTarget:
        """Parse a version target from valid JSON data."""
        for klass in cls.__subclasses__():
            if data['adt_type'] == klass.ADT_TYPE:
                return cls.from_dict(data)


@dataclass(frozen=True)
class CommitTarget(VersionTarget):
    """Version target for a specific commit."""

    ADT_TYPE: ClassVar[str] = "commit"

    commitId: uuid.UUID

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for commit version target objects."""
        return commit_target

    @classmethod
    def from_dict(cls: Type[CommitTarget], data: dict) -> CommitTarget:
        """Parse a commit version target from valid JSON data."""
        return CommitTarget(
            commitId=uuid.UUID(data['commitId'])
        )


@dataclass(frozen=True)
class BranchTarget(VersionTarget):
    """Version target for a branch."""

    ADT_TYPE: ClassVar[str] = "branch"

    branchName: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for branch version target objects."""
        return branch_target

    @classmethod
    def from_dict(cls: Type[BranchTarget], data: dict) -> BranchTarget:
        """Parse a branch version target from valid JSON data."""
        return BranchTarget(
            branchName=data['branchName']
        )


@dataclass(frozen=True)
class DestinationReference(AnamlBaseClass):
    """Reference to a destination data store."""

    ADT_TYPE: ClassVar[str] = ""

    destinationId: int

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for destination reference objects."""
        return destination_reference_field

    @classmethod
    def from_dict(cls: Type[DestinationReference], data: dict) -> DestinationReference:
        """Parse a destination reference from valid JSON data."""
        if 'folder' in data:
            return FolderDestinationReference(
                destinationId=int(data['destinationId']),
                folder=data['folder']
            )
        elif 'topic' in data:
            return TopicDestinationReference(
                destinationId=int(data['destinationId']),
                topic=data['topic']
            )
        elif 'tableName' in data:
            return TableDestinationReference(
                destinationId=int(data['destinationId']),
                tableName=data['tableName']
            )
        else:
            raise ValueError("Cannot parse JSON for destination reference")


@dataclass(frozen=True)
class FolderDestinationReference(DestinationReference):
    """Specify a folder in a destination data store."""

    ADT_TYPE: ClassVar[str] = "folder"

    folder: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for a folder destination reference."""
        return folder_destination_reference

    @classmethod
    def from_dict(cls: Type[FolderDestinationReference], data: dict) -> FolderDestinationReference:
        """Parse a folder destination reference from valid JSON data."""
        return FolderDestinationReference(
            destinationId=int(data['destinationId']),
            folder=data['folder']
        )


@dataclass(frozen=True)
class TableDestinationReference(DestinationReference):
    """Specify a table in a destination data store."""

    ADT_TYPE: ClassVar[str] = "table"

    tableName: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for a table destination reference."""
        return table_destination_reference

    @classmethod
    def from_dict(cls: Type[TableDestinationReference], data: dict) -> TableDestinationReference:
        """Parse a table destination reference from valid JSON data."""
        return TableDestinationReference(
            destinationId=int(data['destinationId']),
            tableName=data['tableName']
        )


@dataclass(frozen=True)
class TopicDestinationReference(DestinationReference):
    """Specify a topic in a destination data store."""

    ADT_TYPE: ClassVar[str] = "topic"

    topic: str

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for a topic destination reference."""
        return topic_destination_reference

    @classmethod
    def from_dict(cls: Type[TopicDestinationReference], data: dict) -> TopicDestinationReference:
        """Parse a topic destination reference from valid JSON data."""
        return TopicDestinationReference(
            destinationId=int(data['destinationId']),
            topic=data['topic']
        )


@dataclass(frozen=True)
class FeatureStore(AnamlBaseClass):
    """Configuration for a feature store job."""

    id: int
    name: str
    description: str
    labels: List[str]
    attributes: List[Attribute]
    featureSet: int
    enabled: bool
    destinations: List[DestinationReference]
    cluster: int
    schedule: Schedule
    startDate: Optional[date]
    endDate: Optional[date]
    versionTarget: Optional[VersionTarget]
    version: uuid.UUID

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for feature store objects."""
        return feature_store_schema

    @classmethod
    def from_dict(cls, data: dict) -> FeatureStore:
        """Parse a feature store from valid JSON data."""
        # TODO: Update to follow new pattern for handling optional fields.
        start_date = data.get('startDate', None)
        end_date = data.get('endDate', None)
        version_target = data.get('versionTarget', None)

        return FeatureStore(
            id=int(data['id']),
            name=data['name'],
            description=data['description'],
            labels=[lbl for lbl in data['labels']],
            attributes=[
                Attribute(key=a['key'], value=a['value']) for a in data['attributes']
            ],
            featureSet=int(data['featureSet']),
            enabled=parse_bool(data['enabled']),
            destinations=[
                DestinationReference.from_dict(d) for d in data['destinations']
            ],
            cluster=int(data['cluster']),
            schedule=Schedule.from_dict(data['schedule']),
            startDate=(start_date and isodate.parse_date(start_date)),
            endDate=(end_date and isodate.parse_date(end_date)),
            versionTarget=version_target,
            version=uuid.UUID(data['version'])
        )


@dataclass(frozen=True)
class FeatureSet(AnamlBaseClass):
    """A collection of related features."""

    name: str
    description: str
    features: List[int]

    id: Optional[int] = None

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for feature set objects."""
        return feature_set_schema

    @classmethod
    def from_dict(cls, data: dict) -> FeatureSet:
        """Parse a feature set from valid JSON data."""
        return FeatureSet(
            id=int(data['id']),
            name=data['name'],
            description=data['description'],
            features=[int(i) for i in data['features']]
        )
