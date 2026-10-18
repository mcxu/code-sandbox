"""Simple PostgreSQL client for basic database operations."""

from pathlib import Path
from typing import Any

import pandas as pd
import psycopg
from psycopg.rows import dict_row


class PgClient:
    def __init__(self, host=None, port=None, user=None, password=None, dbname=None):
        """Initialize the PostgreSQL client.
        Args:
            host: PostgreSQL server host.
            port: PostgreSQL server port.
            user: PostgreSQL user name.
            password: Password for the user.
            dbname: Database to connect to.
        """
        self.conninfo = dict(host=host, port=port, user=user, password=password, dbname=dbname)
        self.connection = None

    def __enter__(self):
        """Context manager entry.
        when this client is used like: with PgClient() as db:...
        the 'with' automatically calls this function.
        """
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def connect(self):
        """Establish a connection to the database."""
        if not self.connection:
            self.connection = psycopg.connect(**self.conninfo, row_factory=dict_row)
        return self

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute(self, query: str, params: tuple | None = None) -> psycopg.Cursor:
        """Execute a SQL query.
        Args:
            query: SQL query string. Use %s for placeholders.
            params: Query parameters.
        Returns:
            Cursor object with query results.
        """
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            self.connection.commit()
        except Exception as e:
            # PostgreSQL rejects every later query in a failed transaction until it is rolled back.
            self.connection.rollback()
            raise e
        return cursor

    def execute_script(self, script: str) -> psycopg.Cursor:
        """Execute multiple semicolon-separated SQL statements."""
        return self.execute(script)

    def execute_script_file(self, script_file_path: str | Path) -> psycopg.Cursor:
        """Read a SQL file and execute its statements."""
        sql_file_contents = self.read_sql_file(script_file_path)
        return self.execute_script(sql_file_contents)

    def fetch_all(self, query: str, params: tuple | None = None) -> list[dict[str, Any]]:
        """Execute a query and fetch all results as dictionaries."""
        cursor = self.execute(query, params)
        return cursor.fetchall()

    def fetch_one(self, query: str, params: tuple | None = None) -> dict[str, Any] | None:
        """Execute a query and fetch one result as a dictionary."""
        cursor = self.execute(query, params)
        return cursor.fetchone()

    def fetch_all_as_pd(self, query: str, params: tuple | None = None) -> pd.DataFrame:
        """Execute a query and fetch all results as a DataFrame."""
        cursor = self.execute(query, params)
        columns = [col.name for col in cursor.description]
        return pd.DataFrame(cursor.fetchall(), columns=columns)

    def read_sql_file(self, sql_file_path: str | Path) -> str:
        """Return the SQL file's contents."""
        return Path(sql_file_path).read_text(encoding="utf-8")
