"""Simple SQLite client for basic database operations."""

import sqlite3
import pandas as pd
from typing import Any
from pathlib import Path

class SQLiteClient:
    def __init__(self, db_path: str = ":memory:"):
        """Initialize the SQLite client.
        Args:
            db_path: Path to the database file. Defaults to in-memory database.
        """
        self.db_path = db_path
        self.connection = None

    def __enter__(self):
        """Context manager entry.
        when this client is used like: with SQLiteClient() as db:...
        the 'with' automatically calls this function.
        """
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def connect(self):
        """Establish a connection to the database."""
        if not self.connection:
            self.connection = sqlite3.connect(self.db_path)
            self.connection.row_factory = sqlite3.Row
        return self

    def close(self):
        """Close the database connection."""
        if self.connection:
            self.connection.close()
            self.connection = None

    def execute(self, query: str, params: tuple = ()) -> sqlite3.Cursor:
        """Execute a SQL query.
        Args:
            query: SQL query string.
            params: Query parameters.
            
        Returns:
            Cursor object with query results.
        """
        cursor = self.connection.cursor()
        cursor.execute(query, params)
        self.connection.commit()
        return cursor
    
    def execute_script(self, script: str) -> sqlite3.Cursor:
        """Execute multiple SQL statements."""
        cursor = self.connection.cursor()
        cursor.executescript(script)
        self.connection.commit()
        return cursor
    
    def execute_script_file(self, script_file_path: str) -> sqlite3.Cursor:
        script = self.read_sql_file(script_file_path)
        cursor = self.execute_script(script)
        return cursor

    def fetch_all(self, query: str, params: tuple = ()) -> list[dict[str, Any]]:
        """Execute a query and fetch all results as dictionaries."""
        cursor = self.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]

    def fetch_one(self, query: str, params: tuple = ()) -> dict[str, Any] | None:
        """Execute a query and fetch one result as a dictionary."""
        cursor = self.execute(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None
    
    def fetch_all_as_pd(self, query: str, params: tuple = ()) -> pd.DataFrame:
        """Execute a query via pandas built-in function and fetch results as DataFrame"""
        output_df = pd.read_sql(query, self.connection, params=params)
        return output_df

    def read_sql_file(self, sql_file_path):
        """Return the SQL file's contents."""
        return Path(sql_file_path).read_text(encoding="utf-8")


