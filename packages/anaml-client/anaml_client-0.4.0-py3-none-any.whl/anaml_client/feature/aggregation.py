#
# Copyright 2020 Simple Machines Pty Ltd - All Rights Reserved.
#
# This file is part of Anaml.
#
# Unauthorized copying and/or distribution of this file, via any medium
# is strictly prohibited.
#
"""Data-types representing Anaml aggregations."""

from __future__ import annotations

import enum

from anaml_client.model import AnamlBaseEnum


@enum.unique
class Aggregation(AnamlBaseEnum):
    """Aggregations for feature definitions."""

    AbsoluteChangeAggregation = "absolutechange"
    AverageAggregation = "avg"
    CountAggregation = "count"
    CountDistinctAggregation = "countdistinct"
    LastAggregation = "last"
    PercentageChangeAggregation = "percentagechange"
    StandardScoreAggregation = "standardscore"
    StdAggregation = "std"
    SumAggregation = "sum"
