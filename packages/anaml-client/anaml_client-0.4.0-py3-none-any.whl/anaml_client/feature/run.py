#
#  Copyright 2021 Simple Machines Pty Ltd - All Rights Reserved.
#
#  This file is part of Anaml.
#
#  Unauthorized copying and/or distribution of this file, via any medium is strictly prohibited.
#

"""Summary details about a run for an individual feature."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional, Type

from .schema import feature_run_summary_schema
from ..statistics import SummaryStatistics
from ..utils.serialisation import AnamlBaseClass


@dataclass(frozen=True)
class FeatureRunSummary(AnamlBaseClass):
    """Summary details describing a run of a particular feature."""

    featureStore: int
    featureRun: int
    runStartDate: date
    runEndDate: date
    runTime: datetime
    stats: SummaryStatistics

    @classmethod
    def json_schema(cls) -> Optional[dict]:
        """JSON schema for feature run summary objects."""
        return feature_run_summary_schema

    @classmethod
    def from_dict(cls: Type[FeatureRunSummary], data: dict) -> FeatureRunSummary:
        """Parse a feature run summary from valid JSON data."""
        return FeatureRunSummary(
            featureStore=int(data['featureStore']),
            featureRun=int(data['featureRun']),
            runStartDate=date.fromisoformat(data['runStartDate']),
            runEndDate=date.fromisoformat(data['runEndDate']),
            runTime=datetime.strptime(data['runTime'], "%Y-%m-%dT%H:%M:%S.%f%z"),
            stats=SummaryStatistics.from_dict(data['stats'])
        )

    def to_dict(self) -> dict:
        """Convert to a dictionary, ready for JSON serialisation."""
        return dict(
            featureStore=self.featureStore,
            featureRun=self.featureRun,
            runStartDate=self.runStartDate,
            runEndDate=self.runEndDate,
            runTime=self.runTime.strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
            stats=self.stats
        )
