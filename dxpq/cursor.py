import dxpq_ext


class Cursor:
    def __init__(self, connection, cursor, cursor_type="dict"):
        self.connection = connection
        self._cursor = cursor
        self.cursor_type = cursor_type

    @classmethod
    def from_connection(cls, connection, cursor_type):
        return cls(connection, dxpq_ext.PGCursor(connection, cursor_type))

    def execute(self, sql: str, params=None):
        if params is not None:
            return self._cursor.execute_params(sql, params)
        return self._cursor.execute(sql)

    def fetchall(self):
        return self._cursor.fetchall()

    def fetchone(self):
        return self._cursor.fetchone()

    def close(self):
        self._cursor.close()
        self.connection.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def __del__(self):
        self.close()
