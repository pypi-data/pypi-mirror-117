#
# Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium is
# strictly prohibited.
#
"""Data types for Anaml cluster definitions."""

from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from typing import ClassVar, TypeVar, Type, Optional, List, Dict

from .schema import cluster_schema, local_cluster, spark_config_schema, sparkserver_cluster
from ..model import AnamlBaseClass, Attribute, CredentialsProviderConfig

T = TypeVar('T', bound='Cluster')


@dataclass(frozen=True)
class SparkConfig(AnamlBaseClass):
    """Spark configuration to pass to a cluster."""

    enableHiveSupport: bool
    hiveMetastoreUrl: Optional[str]
    additionalSparkProperties: Dict[str, str]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for spark configuration objects."""
        return spark_config_schema

    @classmethod
    def from_dict(cls: Type[SparkConfig], data: dict) -> SparkConfig:
        """Parse a spark configuration from valid JSON data."""
        return SparkConfig(
            enableHiveSupport=data['enableHiveSupport'],
            hiveMetastoreUrl=data.get('hiveMetastoreUrl', None),
            additionalSparkProperties=data['additionalSparkProperties']
        )


@dataclass(frozen=True)
class Cluster(AnamlBaseClass):
    """Abstract class representing Anaml compute clusters."""

    ADT_TYPE: ClassVar[str] = ""
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    name: str
    description: str
    labels: List[str]
    attributes: List[Attribute]
    isPreviewCluster: bool
    version: uuid.UUID
    predecessor: Optional[uuid.UUID]

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for cluster objects."""
        return cluster_schema

    @classmethod
    def from_dict(cls: Type[T], data: dict) -> T:
        """Parse a cluster object from valid JSON data."""
        adt_type = data.get('adt_type', None)
        for klass in cls.__subclasses__():
            if adt_type == klass.ADT_TYPE:
                return klass.from_dict(data)
        raise ValueError(f"Cannot parse JSON for cluster: Unknown adt_type '{adt_type}'")


@dataclass(frozen=True)
class LocalCluster(Cluster):
    """Configuration for a local cluster."""

    ADT_TYPE: ClassVar[str] = "local"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    anamlServerUrl: str
    credentialsProvider: CredentialsProviderConfig
    sparkConfig: SparkConfig

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for local cluster objects."""
        return local_cluster

    @classmethod
    def from_dict(cls: Type[LocalCluster], data: dict) -> LocalCluster:
        """Parse a local cluster from valid JSON data."""
        predecessor = data.get('predecessor', None)
        if predecessor:
            predecessor = uuid.UUID(hex=predecessor)
        return LocalCluster(
            name=data['name'],
            description=data['description'],
            labels=data['labels'],
            attributes=[Attribute(key=i['key'], value=i['value']) for i in data['attributes']],
            isPreviewCluster=data['isPreviewCluster'],
            version=uuid.UUID(hex=data['version']),
            predecessor=predecessor,
            anamlServerUrl=data['anamlServerUrl'],
            credentialsProvider=CredentialsProviderConfig.from_json(data['credentialsProvider']),
            sparkConfig=SparkConfig.from_dict(data['sparkConfig'])
        )


@dataclass(frozen=True)
class SparkServerCluster(Cluster):
    """Configuration for a Spark Server cluster."""

    ADT_TYPE: ClassVar[str] = "sparkserver"
    adt_type: str = field(default=ADT_TYPE, init=False, repr=False)

    sparkServerUrl: str
    sparkConfig: SparkConfig

    @classmethod
    def json_schema(cls) -> dict:
        """JSON schema for a spark server cluster."""
        return sparkserver_cluster

    @classmethod
    def from_dict(cls: Type[SparkServerCluster], data: dict) -> SparkServerCluster:
        """Parse a spark server cluster from valid JSON data."""
        # TODO: Refactor to use new pattern for handling optional fields.
        predecessor = data.get('predecessor', None)
        if predecessor:
            predecessor = uuid.UUID(hex=predecessor)

        return SparkServerCluster(
            name=data['name'],
            description=data['description'],
            labels=data['labels'],
            attributes=[Attribute(key=i.key, value=i.value) for i in data['attributes']],
            isPreviewCluster=data['isPreviewCluster'],
            version=uuid.UUID(hex=data['version']),
            predecessor=predecessor,
            sparkServerUrl=data['sparkServerUrl'],
            sparkConfig=SparkConfig.from_dict(data['sparkConfig'])
        )
