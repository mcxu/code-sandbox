"""Simple SQLite client for basic database operations."""

import sqlite3
from typing import Any

class SQLiteClient:
    def __init__(self, db_path: str = ":memory:"):
        """Initialize the SQLite client.
        
        Args:
            db_path: Path to the database file. Defaults to in-memory database.
        """
        self.db_path = db_path
        self.connection = None

    def connect(self):
        """Establish a connection to the database."""
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

    def fetch_all(self, query: str, params: tuple = ()) -> list[dict[str, Any]]:
        """Execute a query and fetch all results as dictionaries."""
        cursor = self.execute(query, params)
        return [dict(row) for row in cursor.fetchall()]

    def fetch_one(self, query: str, params: tuple = ()) -> dict[str, Any] | None:
        """Execute a query and fetch one result as a dictionary."""
        cursor = self.execute(query, params)
        row = cursor.fetchone()
        return dict(row) if row else None

    def __enter__(self):
        """Context manager entry."""
        return self.connect()

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

