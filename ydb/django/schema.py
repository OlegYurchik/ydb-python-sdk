from typing import List, Sequence, Tuple

from django.db.backends.base.schema import BaseDatabaseSchemaEditor
from django.db.models.base import ModelBase
from django.db.models.fields import Field


class DatabaseSchemaEditor(BaseDatabaseSchemaEditor):
    sql_create_unique = "ALTER TABLE %(table)s ADD INDEX %(name)s GLOBAL ON (%(columns)s)"

    def execute(self, sql: str, params: Sequence[str] = ()):
        if (
                not self.collect_sql
                and self.connection.in_atomic_block
                and not self.connection.features.can_rollback_ddl
        ):
            raise Exception(
                "Executing DDL statements while in a transaction on databases that can't perform a "
                "rollback is prohibited."
            )
        sql = str(sql)
        if self.collect_sql:
            ending = "" if sql.rstrip().endswith(";") else ";"
            if params is not None:
                sql = sql % tuple(map(self.quote_value, params))
            self.collected_sql.append(sql + ending)
            return

        with self.connection.cursor() as cursor:
            session = cursor.connection.driver.table_client.session().create()
            session.execute_scheme(sql)

    def table_sql(self, model) -> Tuple[str, List[str]]:
        sql, params = super().table_sql(model=model)
        primary_keys = ", ".join(
            field.column
            for field in model._meta.local_fields
            if field.primary_key
        )
        sql = sql.rstrip(")")
        sql += ", PRIMARY KEY (%s))" % primary_keys
        return sql, params

    def _iter_column_sql(self, column_db_type: str, params: List[str], model: ModelBase,
                         field: Field, include_default: bool) -> Tuple[str, List[str]]:
        generator = super()._iter_column_sql(
            column_db_type=column_db_type,
            params=params,
            model=model,
            field=field,
            include_default=include_default,
        )
        for result in generator:
            if result != "PRIMARY KEY":
                yield result
