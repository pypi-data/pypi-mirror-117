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

from abc import ABC, abstractmethod
from dataclasses import dataclass, field, fields
from datetime import datetime, date, timedelta
from enum import Enum
from typing import List, Optional, Type, TypeVar, ClassVar
import uuid

import isodate

from jsonschema import validate
from jsonschema.exceptions import ValidationError

from .schema import (
    feature_store_run_schema,
    feature_store_schema, feature_set_schema, run_status_field,
    feature_store_execution_statistics_schema, schedule_state_field, schedule_field, never_schedule, daily_schedule,
    cron_schedule, retry_policy_field, never_retry_policy, fixed_retry_policy, version_target_field, branch_target,
    commit_target, destination_reference_field, topic_destination_reference, table_destination_reference,
    folder_destination_reference, credentials_provider_config_field, commit_schema, attributes_field, file_format_field,
)
from ..utils import parse_bool

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

A = TypeVar('A', bound='AnamlBaseClass')

TIMESTAMP_FORMAT = "%Y-%m-%d %H:%M:%S.%f"
INSTANT_FORMAT = "%Y-%m-%dT%H:%M:%S.%f%z"


def json_safe(
    data,
    datetime_format: Optional[str] = None
):
    """Convert values to JSON-safe values."""
    if datetime_format is None:
        datetime_format = INSTANT_FORMAT
    if isinstance(data, str) or isinstance(data, bool) or isinstance(data, float) or isinstance(data, int):
        return data
    elif data is None:
        return None
    elif isinstance(data, AnamlBaseClass):
        return data.to_json()
    elif isinstance(data, enum.Enum):
        return data.value
    elif isinstance(data, uuid.UUID):
        return str(data)
    elif isinstance(data, datetime):
        # NB: datetime <: date, so make sure you don't switch the order here!
        return data.strftime(datetime_format)
    elif isinstance(data, date):
        return data.isoformat()
    elif isinstance(data, dict):
        return {
            k: json_safe(v, datetime_format) for k, v in data.items()
        }
    elif isinstance(data, list):
        return [json_safe(v, datetime_format) for v in data]
    else:
        # TODO: This is probably an error.
        return data


@dataclass(frozen=True)
class AnamlBaseClass(ABC):
    """Base class for data types used in the Anaml API."""

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON Schema for this resource type."""
        return None

    @classmethod
    @abstractmethod
    def from_dict(cls: Type[A], data: dict) -> A:
        """Construct an instance from a dictionary of JSON data."""
        raise NotImplementedError

    def to_dict(self) -> dict:
        """Returns the object as a dictionary.

        This method should not be recursive, so please don't use :ref:`dataclasses.asdict` here.
        """
        return {
            f.name: getattr(self, f.name) for f in fields(self)
        }

    def to_json(self) -> dict:
        """Returns a JSON dictionary encoding the object."""
        return json_safe(self.to_dict())

    @classmethod
    def from_json(cls: Type[A], d: dict) -> A:
        try:
            schema = cls.json_schema()
            if schema:
                validate(d, schema)
            return cls.from_dict(d)
        except ValidationError:
            logger.error("Unable to validate {klass} schema {schema} from dict {data}".format(
                klass=cls.__name__, schema=cls.json_schema(), data=d
            ))
            raise


@dataclass(frozen=True)
class Commit(AnamlBaseClass):
    """An Anaml commit."""
    id: uuid.UUID
    parents: list[uuid.UUID]
    createdAt: datetime
    author: int
    description: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        return commit_schema

    @classmethod
    def from_dict(cls: Type[Commit], data: dict) -> Commit:
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
Attribute = tuple[str, str]  # (key, value)

EntityId = int
EntityName = str
EntityVersionId = uuid.UUID


class Ref:
    ref_type: str
    ref: str


@dataclass(frozen=True)
class CommitRef(Ref):
    ref_type = "commit"


@dataclass(frozen=True)
class BranchRef(Ref):
    ref_type = "branch"


@dataclass(frozen=True)
class EntityData(AnamlBaseClass):
    """ __doc__ string needed """
    id: EntityId
    name: EntityName
    versionId: EntityVersionId

    @classmethod
    def from_dict(cls, data: dict) -> EntityData:
        return EntityData(
            id=data.get("id", None),
            name=data.get("name", None),
            versionId=uuid.UUID(hex=data.get("versionId"))
        )


@dataclass(frozen=True)
class Entity(EntityData):
    """ __doc__ string needed """
    description: str
    defaultColumn: str
    attributes: list[Attribute]
    labels: list[Label]

    @classmethod
    def from_dict(cls, d: dict) -> Entity:
        return Entity(**EntityData.from_dict(d).to_dict(),
                      description=d.get("description", None),
                      defaultColumn=d.get("defaultColumn", None),
                      attributes=d.get("attributes", []),
                      labels=d.get("labels", []))


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
    """ __doc__ string needed """
    id: EntityMappingId
    fromId: EntityId
    toId: EntityId
    mapping: FeatureId
    versionId: EntityMappingVersionId
    name: str

    @classmethod
    def from_dict(cls, d: dict) -> EntityMapping:
        return EntityMapping(id=d.get("id", None),
                             fromId=d.get("fromId", None),
                             toId=d.get("toId", None),
                             mapping=d.get("mapping", None),
                             versionId=d.get("versionId", None),
                             name=d.get("name", _defaultEntityMappingName))


#
# QualityRating $MODEL/QualityRating.scala
#

class QualityRating(Enum):
    GOLD = "gold"
    SILVER = "silver"
    BRONZE = "bronze"
    NULL = None


#
# SourceData $MODEL/SourceData.scala
#
SourceId = int
SourceVersionId = uuid.UUID
SourceName = str


@dataclass(frozen=True)
class SourceHK(AnamlBaseClass):
    """ base class for Sources """
    id: SourceId
    name: SourceName
    description: str
    version: EntityVersionId
    predecessor: Optional[SourceVersionId]
    attributes: list[Attribute] = field(default_factory=list)
    labels: list[Label] = field(default_factory=list)

    @classmethod
    def from_dict(cls, d: dict) -> SourceHK:
        return SourceHK(
            id=d.get("id", None),
            name=d.get("name", None),
            description=d.get("description", None),
            version=d.get("version", uuid.uuid4()),
            predecessor=d.get("predecessor", None),
            attributes=d.get("attributes", []),
            labels=d.get("labels", []))


class SourceTypes(Enum):
    FOLDER = "folder"
    TABLE = "table"
    TOPIC = "topic"
    EMPTY = ""


@dataclass(frozen=True)
class SourceReference(AnamlBaseClass):
    sourceId: SourceId
    folder: Optional[str]
    table: Optional[str]
    topic: Optional[str]
    source: Optional[SourceTypes] = None

    @classmethod
    def from_dict(cls, d: dict) -> SourceReference:
        return SourceReference(
            sourceId=d.get("sourceId", None),
            folder=d.get("folder", ""),
            table=d.get("table", ""),
            topic=d.get("topic", ""),
            source=d.get("source", SourceTypes.EMPTY))


@dataclass(frozen=True)
class Attribute(AnamlBaseClass):
    """Metadata attributes."""
    key: str
    value: str

    @classmethod
    def json_schema(cls) -> dict:
        return attributes_field

    @classmethod
    def from_dict(cls: Type[Attribute], data: dict) -> Attribute:
        return Attribute(
            key=data['key'],
            value=data['value']
        )


@dataclass(frozen=True)
class SensitiveAttribute:
    key: str
    valueConfig: SecretsConfig

    @classmethod
    def from_dict(cls, data: dict) -> SensitiveAttribute:
        return SensitiveAttribute(
            data['key'],
            SecretsConfig.from_dict(data['valueConfig'])
        )


@dataclass(frozen=True)
class CredentialsProviderConfig(AnamlBaseClass):
    username: str
    secretsConfig: SecretsConfig

    @classmethod
    def json_schema(cls) -> dict:
        return credentials_provider_config_field

    def to_json(self) -> dict:
        config = self.secretsConfig.to_json()
        config["username"] = self.username
        if "secret" in config:
            config["password"] = config["secret"]
            del config["secret"]
        return config

    @classmethod
    def from_dict(cls: Type[CredentialsProviderConfig], data: dict) -> CredentialsProviderConfig:
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
    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    @classmethod
    def from_dict(cls, data: dict) -> SecretsConfig:
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
    ADT_TYPE: ClassVar[str] = "basic"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    secret: str


@dataclass(frozen=True)
class GCPSMSecret(SecretsConfig):
    ADT_TYPE: ClassVar[str] = "gcpsm"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    secretProject: str
    secretId: str


@dataclass(frozen=True)
class AWSSMSecret(SecretsConfig):
    ADT_TYPE: ClassVar[str] = "awssm"
    adt_type: str = field(default=ADT_TYPE, repr=False, init=False)

    secretId: str


@dataclass(frozen=True)
class FileFormat(AnamlBaseClass):
    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    @classmethod
    def json_schema(cls) -> dict:
        return file_format_field

    @classmethod
    def from_dict(cls, data: dict) -> FileFormat:
        if 'orc' == data['adt_type']:
            return Orc()
        elif 'parquet' == data['adt_type']:
            return Parquet()
        elif 'csv' == data['adt_type']:
            return Csv(bool(data['includeHeader']))


@dataclass(frozen=True)
class Orc(FileFormat):
    ADT_TYPE: ClassVar[str] = "orc"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)


@dataclass(frozen=True)
class Parquet(FileFormat):
    ADT_TYPE: ClassVar[str] = "parquet"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)


@dataclass(frozen=True)
class Csv(FileFormat):
    ADT_TYPE: ClassVar[str] = "csv"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    includeHeader: bool


@enum.unique
class RunStatus(enum.Enum,):
    Pending = 'pending'
    Running = 'running'
    Completed = 'completed'
    Failed = 'failed'

    @classmethod
    def json_schema(cls) -> dict:
        return run_status_field

    @classmethod
    def from_dict(cls: Type[RunStatus], data: dict) -> RunStatus:
        return cls(data['adt_type'])


@dataclass(frozen=True)
class FeatureStoreExecutionStatistics(AnamlBaseClass):
    """Statistics from a feature store execution job."""

    # TODO

    @classmethod
    def json_schema(cls) -> dict:
        return feature_store_execution_statistics_schema

    @classmethod
    def from_dict(cls: Type[FeatureStoreExecutionStatistics], data: dict) -> FeatureStoreExecutionStatistics:
        return FeatureStoreExecutionStatistics()


@dataclass(frozen=True)
class RetryPolicy(AnamlBaseClass):
    ADT_TYPE: ClassVar[str] = ""

    @classmethod
    def json_schema(cls) -> dict:
        return retry_policy_field

    @classmethod
    def from_dict(cls: Type[RetryPolicy], data: dict) -> RetryPolicy:
        adt_type = data.get('adt_type', None)
        for ty in cls.__subclasses__():
            if adt_type == ty.ADT_TYPE:
                return cls.from_dict(data)
        raise ValueError(
            f"Could not parse JSON to RetryPolicy: unexpected adt_type {adt_type}"
        )


@dataclass(frozen=True)
class NeverRetryPolicy(RetryPolicy):
    ADT_TYPE = "never"

    @classmethod
    def json_schema(cls) -> dict:
        return never_retry_policy

    @classmethod
    def from_dict(cls: Type[NeverRetryPolicy], data: dict) -> NeverRetryPolicy:
        return NeverRetryPolicy()


@dataclass(frozen=True)
class FixedRetryPolicy(RetryPolicy):
    ADT_TYPE = "fixed"

    backoff: timedelta
    maxAttempts: int

    @classmethod
    def json_schema(cls) -> dict:
        return fixed_retry_policy

    @classmethod
    def from_dict(cls: Type[FixedRetryPolicy], data: dict) -> FixedRetryPolicy:
        return FixedRetryPolicy(
            backoff=isodate.parse_duration(data['backoff']),
            maxAttempts=int(data['maxAttempts'])
        )


@dataclass(frozen=True)
class Schedule(AnamlBaseClass):
    ADT_TYPE: ClassVar[str] = ""

    retryPolicy: RetryPolicy

    @classmethod
    def json_schema(cls) -> dict:
        return schedule_field

    @classmethod
    def from_dict(cls: Type[Schedule], data: dict) -> Schedule:
        adt_type = data['adt_type']
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)


@dataclass(frozen=True)
class DailySchedule(Schedule):
    ADT_TYPE = "daily"

    startTimeOfDay: datetime

    @classmethod
    def json_schema(cls) -> dict:
        return daily_schedule

    @classmethod
    def from_dict(cls: Type[DailySchedule], data: dict) -> DailySchedule:
        startTimeOfDay = data.get('startTimeOfDay', None)
        if startTimeOfDay:
            startTimeOfDay = datetime.fromisoformat(startTimeOfDay)
        return DailySchedule(
            startTimeOfDay=startTimeOfDay,
            retryPolicy=RetryPolicy.from_dict(data['retryPolicy'])
        )


@dataclass(frozen=True)
class CronSchedule(Schedule):
    ADT_TYPE = "cron"

    cronString: str

    @classmethod
    def json_schema(cls) -> dict:
        return cron_schedule

    @classmethod
    def from_dict(cls: Type[Schedule], data: dict) -> Schedule:
        return CronSchedule(
            cronString=data['cronString'],
            retryPolicy=RetryPolicy.from_dict(data['retryPolicy'])
        )


@dataclass(frozen=True)
class NeverSchedule(Schedule):
    ADT_TYPE = "never"

    @classmethod
    def json_schema(cls) -> dict:
        return never_schedule

    @classmethod
    def from_dict(cls: Type[Schedule], data: dict) -> Schedule:
        return NeverSchedule(retryPolicy=NeverRetryPolicy())


@dataclass(frozen=True)
class ScheduleState(AnamlBaseClass):
    schedule: Schedule
    scheduleStartTime: datetime
    retryCount: int

    @classmethod
    def json_schema(cls) -> dict:
        return schedule_state_field

    @classmethod
    def from_dict(cls: Type[ScheduleState], data: dict) -> ScheduleState:
        return ScheduleState(
            schedule=Schedule.from_dict(data['schedule']),
            scheduleStartTime=isodate.parse_datetime(data['scheduleStartTime']),
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
        return feature_store_run_schema

    @classmethod
    def from_dict(cls: Type[FeatureStoreRun], data: dict) -> FeatureStoreRun:
        schedule_state = data.get('scheduleState', None)
        if schedule_state:
            schedule_state = ScheduleState.from_dict(schedule_state)

        statistics = data.get('statistics', None)
        if statistics:
            statistics = FeatureStoreExecutionStatistics.from_dict(statistics)

        return FeatureStoreRun(
            id=int(data['id']),
            created=datetime.strptime(data['created'], INSTANT_FORMAT),
            featureStoreId=int(data['featureStoreId']),
            featureStoreVersionId=uuid.UUID(data['featureStoreVersionId']),
            commitId=uuid.UUID(data['commitId']),
            runStartDate=date.fromisoformat(data['runStartDate']),
            runEndDate=date.fromisoformat(data['runEndDate']),
            status=RunStatus.from_dict(data['status']),
            errorMessage=data.get('errorMessage', None),
            scheduleState=schedule_state,
            statistics=statistics
        )


@dataclass(frozen=True)
class VersionTarget(AnamlBaseClass):
    ADT_TYPE: ClassVar[str] = ""

    @classmethod
    def json_schema(cls) -> dict:
        return version_target_field

    @classmethod
    def from_dict(cls: Type[VersionTarget], data: dict) -> VersionTarget:
        for klass in cls.__subclasses__():
            if data['adt_type'] == klass.ADT_TYPE:
                return cls.from_dict(data)


@dataclass(frozen=True)
class CommitTarget(VersionTarget):
    ADT_TYPE = "commit"

    commitId: uuid.UUID

    @classmethod
    def json_schema(cls) -> dict:
        return commit_target

    @classmethod
    def from_dict(cls: Type[CommitTarget], data: dict) -> CommitTarget:
        return CommitTarget(
            commitId=uuid.UUID(data['commitId'])
        )


@dataclass(frozen=True)
class BranchTarget(VersionTarget):
    ADT_TYPE = "branch"

    branchName: str

    @classmethod
    def json_schema(cls) -> dict:
        return branch_target

    @classmethod
    def from_dict(cls: Type[BranchTarget], data: dict) -> BranchTarget:
        return BranchTarget(
            branchName=data['branchName']
        )


@dataclass(frozen=True)
class DestinationReference(AnamlBaseClass):
    ADT_TYPE: ClassVar[str] = ""

    destinationId: int

    @classmethod
    def json_schema(cls) -> dict:
        return destination_reference_field

    @classmethod
    def from_dict(cls: Type[DestinationReference], data: dict) -> DestinationReference:
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
    ADT_TYPE = "folder"

    folder: str

    @classmethod
    def json_schema(cls) -> dict:
        return folder_destination_reference

    @classmethod
    def from_dict(cls: Type[FolderDestinationReference], data: dict) -> FolderDestinationReference:
        return FolderDestinationReference(
            destinationId=int(data['destinationId']),
            folder=data['folder']
        )


@dataclass(frozen=True)
class TableDestinationReference(DestinationReference):
    ADT_TYPE = "table"

    tableName: str

    @classmethod
    def json_schema(cls) -> dict:
        return table_destination_reference

    @classmethod
    def from_dict(cls: Type[TableDestinationReference], data: dict) -> TableDestinationReference:
        return TableDestinationReference(
            destinationId=int(data['destinationId']),
            tableName=data['tableName']
        )


@dataclass(frozen=True)
class TopicDestinationReference(DestinationReference):
    ADT_TYPE = "topic"

    topic: str

    @classmethod
    def json_schema(cls) -> dict:
        return topic_destination_reference

    @classmethod
    def from_dict(cls: Type[TopicDestinationReference], data: dict) -> TopicDestinationReference:
        return TopicDestinationReference(
            destinationId=int(data['destinationId']),
            topic=data['topic']
        )


@dataclass(frozen=True)
class FeatureStore(AnamlBaseClass):
    """A collection of features."""

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
        return feature_store_schema

    @classmethod
    def from_dict(cls, data: dict) -> FeatureStore:
        start_date = data.get('startDate', None)
        end_date = data.get('endDate', None)
        version_target = data.get('versionTarget', None)

        return FeatureStore(
            id=int(data['id']),
            name=data['name'],
            description=data['description'],
            labels=[lbl for lbl in data['labels']],
            attributes=[
                Attribute(key=a.key, value=a.value) for a in data['attributes']
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
    """A collection of features to be run together."""

    id: int
    name: str
    description: str
    features: List[int]

    @classmethod
    def json_schema(cls) -> dict:
        return feature_set_schema

    @classmethod
    def from_dict(cls, data: dict) -> FeatureSet:
        return FeatureSet(
            id=int(data['id']),
            name=data['name'],
            description=data['description'],
            features=[int(i) for i in data['features']]
        )
