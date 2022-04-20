from django.db.backends.base.introspection import BaseDatabaseIntrospection, TableInfo

from ydb.dbapi.cursor import Cursor


class DatabaseIntrospection(BaseDatabaseIntrospection):
    def get_table_list(self, cursor: Cursor):
        query = "SELECT DISTINCT Path FROM `.sys/partition_stats`"
        cursor.execute(query)

        # TODO: I'm not sure what "type" is it
        return [TableInfo(*row, type="t") for row in cursor.fetchall()]
