"""JSON Schemas for destinations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, ClassVar
from uuid import UUID

from ..model.types import AnamlBaseClass, Attribute, FileFormat, SensitiveAttribute, CredentialsProviderConfig
from .schema import (
    destination_schema,
    gcs_staging_area,
    bigquery_destination,
    gcs_destination,
    online_feature_store_destination,
    hdfs_destination,
    hive_destination,
    jdbc_destination_schema,
    kafka_destination,
    local_destination,
    s3a_destination_schema,
    s3_destination_schema
)


@dataclass(frozen=True)
class GcsStaging(AnamlBaseClass):
    """Data staging configuration for BigQuery destinations."""

    @classmethod
    def json_schema(cls) -> dict:
        return gcs_staging_area

    @classmethod
    def from_dict(cls, data: dict):
        if 'temporary' == data['adt_type']:
            return TemporaryGcsStaging(data['bucket'])
        elif 'permanent' == data['adt_type']:
            return PermanentGcsStaging(data['bucket'], data['path'])
        else:
            raise ValueError("Unexpected GCS staging type: {ty}".format(
                ty=data['adt_type']
            ))


@dataclass(frozen=True)
class TemporaryGcsStaging(GcsStaging):
    bucket: str


@dataclass(frozen=True)
class PermanentGcsStaging(GcsStaging):
    bucket: str
    path: str


@dataclass(frozen=True)
class Destination(AnamlBaseClass):
    """A storage location for generated features."""

    # Tag used to map a JSON document to a particular subclasses.
    ADT_TYPE: ClassVar[str] = ""

    id: int
    name: str
    description: str
    labels: List[str]
    attributes: List[str]
    version: UUID
    predecessor: Optional[UUID]

    @classmethod
    def json_schema(cls) -> dict:
        return destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> Destination:
        adt_type = data.get('adt_type', None)
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse JSON to destination: Unknown adt_type '{adt_type}'")

    @classmethod
    def _basic_parameters(cls, data: dict) -> dict:
        """Unpack the basic parameters for a destination."""
        kwargs = {
            'id': int(data['id']),
            'name': data['name'],
            'description': data['description'],
            'labels': data['labels'],
            'attributes': [
                Attribute(key=a.key, value=a.value) for a in data['attributes']
            ],
            'version': UUID(hex=data['version']),
            'predecessor': None
        }

        pred = data.get('predecessor')
        if pred:
            kwargs['predecessor'] = UUID(hex=pred)

        return kwargs


@dataclass(frozen=True)
class BigQueryDestination(Destination):
    ADT_TYPE = "bigquery"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    path: str
    stagingArea: GcsStaging
    tableName: Optional[str]

    @classmethod
    def json_schema(cls):
        return bigquery_destination

    @classmethod
    def from_dict(cls, data: dict) -> BigQueryDestination:
        kwargs = cls._basic_parameters(data)
        return BigQueryDestination(
            **kwargs,
            path=data['path'],
            stagingArea=GcsStaging.from_dict(data['stagingArea']),
            tableName=data.get('path', None)
        )


@dataclass(frozen=True)
class GCSDestination(Destination):
    ADT_TYPE = "gcs"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bucket: str
    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls):
        return gcs_destination

    @classmethod
    def from_dict(cls, data: dict) -> GCSDestination:
        kwargs = cls._basic_parameters(data)
        return GCSDestination(
            **kwargs,
            bucket=data['bucket'],
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get('folder', None)
        )


@dataclass(frozen=True)
class HDFSDestination(Destination):
    ADT_TYPE = "hdfs"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls):
        return hdfs_destination

    @classmethod
    def from_dict(cls, data: dict) -> HDFSDestination:
        kwargs = cls._basic_parameters(data)
        return HDFSDestination(
            **kwargs,
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get('folder', None)
        )


@dataclass(frozen=True)
class HiveDestination(Destination):
    ADT_TYPE = "hive"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    database: str
    tableName: Optional[str]

    @classmethod
    def json_schema(cls):
        return hive_destination

    @classmethod
    def from_dict(cls, data: dict) -> HiveDestination:
        kwargs = cls._basic_parameters(data)
        return HiveDestination(
            **kwargs,
            database=data['database'],
            tableName=data.get('tableName', None)
        )


@dataclass(frozen=True)
class JDBCDestination(Destination):
    ADT_TYPE = 'jdbc'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    url: str
    schema: str
    credentialsProvider: CredentialsProviderConfig
    tableName: Optional[str]

    @classmethod
    def json_schema(cls):
        return jdbc_destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> JDBCDestination:
        kwargs = cls._basic_parameters(data)
        return JDBCDestination(
            **kwargs,
            url=data['url'],
            schema=data['schema'],
            credentialsProvider=CredentialsProviderConfig.from_dict(data['credentialsProvider']),
            tableName=data.get('tableName', None)
        )


@dataclass(frozen=True)
class KafkaDestination(Destination):
    ADT_TYPE = 'kafka'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bootstrapServers: str
    schemaRegistryUrl: str
    kafkaPropertiesProviders: List[SensitiveAttribute]
    topic: Optional[str]

    @classmethod
    def json_schema(cls):
        return kafka_destination

    @classmethod
    def from_dict(cls, data: dict) -> KafkaDestination:
        kwargs = cls._basic_parameters(data)
        return KafkaDestination(
            **kwargs,
            bootstrapServers=data['bootstrapServers'],
            schemaRegistryUrl=data['schemaRegistryUrl'],
            kafkaPropertiesProviders=[
                SensitiveAttribute.from_dict(a) for a in data['kafkaPropertiesProviders']
            ],
            topic=data.get('topic', None)
        )


@dataclass(frozen=True)
class LocalDestination(Destination):
    ADT_TYPE = 'local'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls):
        return local_destination

    @classmethod
    def from_dict(cls, data: dict) -> LocalDestination:
        kwargs = cls._basic_parameters(data)
        return LocalDestination(
            **kwargs,
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get("folder", None)
        )


@dataclass(frozen=True)
class OnlineFeatureStoreDestination(Destination):
    ADT_TYPE = 'onlinefeaturestore'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    url: str
    schema: str
    credentialsProvider: CredentialsProviderConfig
    tableName: Optional[str]

    @classmethod
    def json_schema(cls):
        return online_feature_store_destination

    @classmethod
    def from_dict(cls, data: dict) -> OnlineFeatureStoreDestination:
        kwargs = cls._basic_parameters(data)
        return OnlineFeatureStoreDestination(
            **kwargs,
            url=data['url'],
            schema=data['schema'],
            credentialsProvider=CredentialsProviderConfig.from_dict(data['credentialsProvider']),
            tableName=data.get('tableName', None)
        )


@dataclass(frozen=True)
class S3ADestination(Destination):
    ADT_TYPE = 's3a'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bucket: str
    path: str
    fileFormat: FileFormat
    folder: Optional[str]
    endpoint: str
    accessKey: str
    secretKey: str

    @classmethod
    def json_schema(cls):
        return s3a_destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> S3ADestination:
        kwargs = cls._basic_parameters(data)
        return S3ADestination(
            **kwargs,
            bucket=data['bucket'],
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get('folder', None),
            endpoint=data['endpoint'],
            accessKey=data['accessKey'],
            secretKey=data['secretKey']
        )


@dataclass(frozen=True)
class S3Destination(Destination):
    ADT_TYPE = 's3'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bucket: str
    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls):
        return s3_destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> S3Destination:
        kwargs = cls._basic_parameters(data)
        return S3Destination(
            **kwargs,
            bucket=data['bucket'],
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get('folder', None)
        )
