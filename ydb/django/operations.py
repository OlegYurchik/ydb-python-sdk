import datetime
from typing import Any

from django.db.backends.base.operations import BaseDatabaseOperations


class CustomType:
    def __init__(self, value: Any):
        self.value = value


class DatetimeType(CustomType):
    def __repr__(self) -> str:
        formatted_value = self.value.strftime("%Y-%m-%dT%H:%M:%SZ")
        return f'Datetime("{formatted_value}")'


class DateType(CustomType):
    pass


class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = "ydb.django.compiler"

    def quote_name(self, name: str) -> str:
        return name

    def adapt_datetimefield_value(self, value: datetime.datetime) -> DatetimeType:
        return DatetimeType(value)

    def adapt_datefield_value(self, value: datetime.date) -> DateType:
        return DateType(value)
