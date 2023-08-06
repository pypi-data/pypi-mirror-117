#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Data-types representing Anaml destinations."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import List, Optional, ClassVar
from uuid import UUID

from ..model import AnamlBaseClass, Attribute, FileFormat, SensitiveAttribute, CredentialsProviderConfig
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
    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(init=False, repr=False, default=ADT_TYPE)

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for GCS staging objects."""
        return gcs_staging_area

    @classmethod
    def from_dict(cls, data: dict) -> GcsStaging:
        """Parse a GCS staging object from valid JSON data."""
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
    """Temporary GCS staging configuration for BigQuery destinations."""
    ADT_TYPE: ClassVar[str] = "temporary"
    adt_type: str = field(init=False, repr=False, default=ADT_TYPE)

    bucket: str


@dataclass(frozen=True)
class PermanentGcsStaging(GcsStaging):
    """Permanent GCS staging configuration for BigQuery destinations."""
    ADT_TYPE: ClassVar[str] = "permanent"
    adt_type: str = field(init=False, repr=False, default=ADT_TYPE)

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
        """JSON schema for destination objects."""
        return destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> Destination:
        """Parse a destination object from valid JSON data."""
        adt_type = data.get('adt_type', None)
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse JSON to destination: Unknown adt_type '{adt_type}'")

    @classmethod
    def _basic_parameters(cls, data: dict) -> dict:
        """Parse the basic parameters for a destination from valid JSON data."""
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
    """A BigQuery destination."""

    ADT_TYPE = "bigquery"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    path: str
    stagingArea: GcsStaging
    tableName: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for BigQuery destination objects."""
        return bigquery_destination

    @classmethod
    def from_dict(cls, data: dict) -> BigQueryDestination:
        """Parse a BigQuery destination object from valid JSON data."""
        kwargs = cls._basic_parameters(data)
        return BigQueryDestination(
            **kwargs,
            path=data['path'],
            stagingArea=GcsStaging.from_dict(data['stagingArea']),
            tableName=data.get('path', None)
        )


@dataclass(frozen=True)
class GCSDestination(Destination):
    """A GCS destination."""

    ADT_TYPE = "gcs"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bucket: str
    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for GCS destination objects."""
        return gcs_destination

    @classmethod
    def from_dict(cls, data: dict) -> GCSDestination:
        """Parse a GCS destination object from valid JSON data."""
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
    """A HDFS destination."""

    ADT_TYPE = "hdfs"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for HDFS destination objects."""
        return hdfs_destination

    @classmethod
    def from_dict(cls, data: dict) -> HDFSDestination:
        """Parse a HDFS destination from valid JSON data."""
        kwargs = cls._basic_parameters(data)
        return HDFSDestination(
            **kwargs,
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get('folder', None)
        )


@dataclass(frozen=True)
class HiveDestination(Destination):
    """A Hive destination."""

    ADT_TYPE = "hive"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    database: str
    tableName: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for Hive destination objects."""
        return hive_destination

    @classmethod
    def from_dict(cls, data: dict) -> HiveDestination:
        """Parse a Hive destination from valid JSON data."""
        kwargs = cls._basic_parameters(data)
        return HiveDestination(
            **kwargs,
            database=data['database'],
            tableName=data.get('tableName', None)
        )


@dataclass(frozen=True)
class JDBCDestination(Destination):
    """A JDBC destination."""

    ADT_TYPE = 'jdbc'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    url: str
    schema: str
    credentialsProvider: CredentialsProviderConfig
    tableName: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for JDBC destination objects."""
        return jdbc_destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> JDBCDestination:
        """Parse a JDBC destination from valid JSON data."""
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
    """A Kafka destination."""

    ADT_TYPE = 'kafka'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bootstrapServers: str
    schemaRegistryUrl: str
    kafkaPropertiesProviders: List[SensitiveAttribute]
    topic: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for Kafka destination objects."""
        return kafka_destination

    @classmethod
    def from_dict(cls, data: dict) -> KafkaDestination:
        """Parse a Kafka destination from valid JSON data."""
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
    """A local filesystem destination."""

    ADT_TYPE = 'local'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for local destination objects."""
        return local_destination

    @classmethod
    def from_dict(cls, data: dict) -> LocalDestination:
        """Parse a local filesystem destination from valid JSON data."""
        kwargs = cls._basic_parameters(data)
        return LocalDestination(
            **kwargs,
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get("folder", None)
        )


@dataclass(frozen=True)
class OnlineFeatureStoreDestination(Destination):
    """An online feature store destination."""

    ADT_TYPE = 'onlinefeaturestore'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    url: str
    schema: str
    credentialsProvider: CredentialsProviderConfig
    tableName: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for online feature store destination objects."""
        return online_feature_store_destination

    @classmethod
    def from_dict(cls, data: dict) -> OnlineFeatureStoreDestination:
        """Parse an online feature store destination from valid JSON data."""
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
    """An S3A destination."""

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
    def json_schema(cls) -> dict:
        """JSON schema for S3A destination objects."""
        return s3a_destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> S3ADestination:
        """Parse an S3A destination from valid JSON data."""
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
    """An S3 destination."""

    ADT_TYPE = 's3'
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    bucket: str
    path: str
    fileFormat: FileFormat
    folder: Optional[str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for S3 destination objects."""
        return s3_destination_schema

    @classmethod
    def from_dict(cls, data: dict) -> S3Destination:
        """Parse an S3 destination from valid JSON data."""
        kwargs = cls._basic_parameters(data)
        return S3Destination(
            **kwargs,
            bucket=data['bucket'],
            path=data['path'],
            fileFormat=FileFormat.from_dict(data['fileFormat']),
            folder=data.get('folder', None)
        )
