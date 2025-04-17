# Copyright (c) QuantCo 2025-2025
# SPDX-License-Identifier: BSD-3-Clause

from dataframely import (
    Any,
    Date,
    Datetime,
    Decimal,
    Enum,
    Float32,
    Int64,
    List,
    Schema,
    Struct,
)


class MyImportedBaseSchema(Schema):
    a = Int64()


class MyImportedSchema(MyImportedBaseSchema):
    b = Float32()
    c = Enum(["a", "b", "c"])
    d = Struct({"a": Int64(), "b": Struct({"c": Enum(["a", "b"])})})
    e = List(Struct({"a": Int64()}))
    f = Datetime()
    g = Date()
    h = Any()
    some_decimal = Decimal(12, 8)
