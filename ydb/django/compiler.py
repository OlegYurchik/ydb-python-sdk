from typing import List, Tuple

from django.db.models.fields import Field
from django.db.models.sql.compiler import (
    SQLAggregateCompiler as DefaultSQLAggregateCompiler,
    SQLCompiler as DefaultSQLCompiler,
    SQLDeleteCompiler as DefaultSQLDeleteCompiler,
    SQLInsertCompiler as DefaultSQLInsertCompiler,
    SQLUpdateCompiler as DefaultSQLUpdateCompiler,
)


class SQLAggregateCompiler(DefaultSQLAggregateCompiler):
    pass


class SQLCompiler(DefaultSQLCompiler):
    pass


class SQLDeleteCompiler(DefaultSQLDeleteCompiler):
    pass


class SQLInsertCompiler(DefaultSQLInsertCompiler):
    def field_as_sql(self, field: Field, val: str) -> Tuple[str, List[str]]:
        sql, params = super().field_as_sql(field=field, val=val)
        sql = "?"
        return sql, params


class SQLUpdateCompiler(DefaultSQLUpdateCompiler):
    pass
