from typing import Any, Dict

from django.db.backends.base.base import BaseDatabaseWrapper

from ydb import dbapi as Database
from ydb.dbapi import Connection, connect
from ydb.dbapi.cursor import Cursor
from .client import DatabaseClient
from .creation import DatabaseCreation
from .features import DatabaseFeatures
from .introspection import DatabaseIntrospection
from .operations import DatabaseOperations
from .schema import DatabaseSchemaEditor


class DatabaseWrapper(BaseDatabaseWrapper):
    vendor = "ydb"
    display_name = "YDB"

    data_types = {
        "AutoField": "Uint32",
        "BigAutoField": "Uint64",
        "SmallAutoField": "Uint8",

        "BooleanField": "Bool",
        "NullBooleanField": "Bool",
        "IntegerField": "Int32",
        "SmallIntegerField": "Int8",
        "PositiveIntegerField": "Uint32",
        "PositiveSmallIntegerField": "Uint8",
        "BigIntegerField": "Int64",
        "PositiveBigIntegerField": "Uint64",
        "DecimalField": "Decimal",
        "FloatField": "Float",

        "CharField": "Utf8",
        "TextField": "Utf8",
        "SlugField": "Utf8",
        "EmailField": "Utf8",
        "FilePathField": "Utf8",
        "GenericIPAddressField": "Uff8",
        "IPAddressField": "Utf8",
        "URLField": "Utf8",
        "UUIDField": "Utf8",

        "DateField": "Date",
        "DateTimeField": "Datetime",
        "DurationField": "Interval",
        "TimeField": "Datetime",

        "BinaryField": "String",
        "CommaSeparatedIntegerField": "List<Int32>",
    }

    client_class = DatabaseClient
    creation_class = DatabaseCreation
    features_class = DatabaseFeatures
    introspection_class = DatabaseIntrospection
    ops_class = DatabaseOperations

    SchemaEditorClass = DatabaseSchemaEditor
    Database = Database

    data_types_suffix = {}  # default
    data_type_check_constraints = {}  # default
    ops = None  # default

    queries_limit = 9000  # default

    # Connections and cursors
    def get_connection_params(self):
        host = self.settings_dict["HOST"]
        port = self.settings_dict.get("PORT", 2136)
        name = self.settings_dict.get("NAME", "local")

        return {
            "endpoint": f"grpc://{host}:{port}",
            "database": f"/{name}",
        }

    def get_new_connection(self, conn_params: Dict[str, Any]) -> Connection:
        return connect(**conn_params)

    def init_connection_state(self):
        raise NotImplementedError

    def create_cursor(self, name=None) -> Cursor:
        return self.connection.cursor()

    def is_usable(self):
        raise NotImplementedError

    # Transaction management
    def _set_autocommit(self, autocommit: bool):
        with self.wrap_database_errors:
            self.connection.autocommit = autocommit

    def _start_transaction_under_autocommit(self):
        raise NotImplementedError

    # Foreign key constraints
    def disable_constraint_checking(self):
        raise NotImplementedError

    def enable_constraint_checking(self):
        raise NotImplementedError

    def check_constraints(self, table_names=None):
        raise NotImplementedError
