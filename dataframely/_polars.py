# Copyright (c) QuantCo 2025-2025
# SPDX-License-Identifier: BSD-3-Clause

import datetime as dt
from collections.abc import Iterable
from typing import TypeVar

import polars as pl
from polars.datatypes import DataTypeClass

PolarsDataType = pl.DataType | DataTypeClass
FrameType = TypeVar("FrameType", pl.DataFrame, pl.LazyFrame)

EPOCH_DATETIME = dt.datetime(1970, 1, 1)
SECONDS_PER_DAY = 86400

# --------------------------------------- JOINS -------------------------------------- #


def join_all_inner(dfs: Iterable[FrameType], on: str | list[str]) -> FrameType:
    it = iter(dfs)
    result = next(it)
    while (df := next(it, None)) is not None:
        result = result.join(df, on=on)
    return result


def join_all_outer(dfs: Iterable[FrameType], on: str | list[str]) -> FrameType:
    it = iter(dfs)
    result = next(it)
    while (df := next(it, None)) is not None:
        result = result.join(df, on=on, how="full", coalesce=True)
    return result


# ------------------------------------- DATETIMES ------------------------------------ #


def date_matches_resolution(t: dt.date, resolution: str) -> bool:
    return pl.Series([t], dtype=pl.Date).dt.truncate(resolution).item() == t


def datetime_matches_resolution(t: dt.datetime, resolution: str) -> bool:
    return pl.Series([t], dtype=pl.Datetime).dt.truncate(resolution).item() == t


def time_matches_resolution(t: dt.time, resolution: str) -> bool:
    return (
        pl.Series([t], dtype=pl.Time)
        .to_frame("t")
        .select(
            pl.lit(EPOCH_DATETIME.date())
            .dt.combine(pl.col("t"))
            .dt.truncate(resolution)
            .dt.time()
        )
        .item()
        == t
    )


def timedelta_matches_resolution(d: dt.timedelta, resolution: str) -> bool:
    return datetime_matches_resolution(EPOCH_DATETIME + d, resolution)
