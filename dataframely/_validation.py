# Copyright (c) QuantCo 2025-2025
# SPDX-License-Identifier: BSD-3-Clause

from collections.abc import Iterable
from typing import Literal

import polars as pl

from dataframely.exc import DtypeValidationError, ValidationError

from ._polars import PolarsDataType
from .columns import Column

DtypeCasting = Literal["none", "lenient", "strict"]


def validate_columns(
    lf: pl.LazyFrame,
    actual: Iterable[str],
    expected: Iterable[str],
) -> pl.LazyFrame:
    """Validate the existence of expected columns in a data frame.

    Args:
        lf: The data frame whose list of columns to validate.
        actual: The list of columns that _are_ observed. Passed as a separate argument as a
            performance improvement as it minimizes the number of schema collections.
        expected: The list of columns that _should_ be observed.

    Raises:
        ValidationError: If any expected column is not part of the actual columns.

    Returns:
        The input data frame, either as-is or with extra columns stripped.
    """
    actual_set = set(actual)
    expected_set = set(expected)

    missing_columns = expected_set - actual_set
    if len(missing_columns) > 0:
        raise ValidationError(
            f"{len(missing_columns)} columns in the schema are missing in the "
            f"data frame: {sorted(missing_columns)}."
        )

    return lf.select(expected)


def validate_dtypes(
    lf: pl.LazyFrame,
    actual: pl.Schema,
    expected: dict[str, Column],
    casting: DtypeCasting,
) -> pl.LazyFrame:
    """Validate the dtypes of all expected columns in a data frame.

    Args:
        lf: The data frame whose column dtypes to validate.
        actual: The actual schema of the data frame. Passed as a separate argument as a
            performance improvement as it minimizes the number of schema collections.
        expected: The column definitions carrying the expected dtypes.
        casting: The strategy for casting dtypes.

    Raises:
        DtypeValidationError: If the expected column dtypes do not match the input's and
            ``casting`` set to ``none``.

    Returns:
        The input data frame with all column dtypes ensured to have the expected dtype.
    """
    dtype_errors: dict[str, tuple[PolarsDataType, PolarsDataType]] = {}
    for name, col in expected.items():
        if not col.validate_dtype(actual[name]):
            dtype_errors[name] = (actual[name], col.dtype)

    if len(dtype_errors) > 0:
        if casting == "none":
            raise DtypeValidationError(dtype_errors)
        else:
            return lf.with_columns(
                pl.col(name).cast(expected[name].dtype, strict=(casting == "strict"))
                for name in dtype_errors.keys()
            )

    return lf
