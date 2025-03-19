import dxpq_ext

from dxpq.cursor import Cursor


class Connection:
    def __init__(self, connection_string: str):
        self.connection_string = connection_string

    def cursor(self, cursor_type="dict"):
        return Cursor.from_connection(
            dxpq_ext.PGConnection(self.connection_string),
            cursor_type,
        )
