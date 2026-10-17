import pandas as pd
from PythonSandbox.utils.sqllite_client import SQLiteClient

class TestSQLiteClient:
    def test_1(self):
        with SQLiteClient() as db:
            # Create a table
            db.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT UNIQUE
                )
            """)

            # Insert data
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Alice", "alice@example.com"))
            db.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Bob", "bob@example.com"))

            # Query data
            users = db.fetch_all("SELECT * FROM users")
            print("All users:\n", users)

            user = db.fetch_one("SELECT * FROM users WHERE name = ?", ("Alice",))
            print("Found user:\n", user)
    
    def test_read_sql_file(self):
        sql_file_path = "PythonSandbox/test/sql_test_files/users_sample.sql"
        client = SQLiteClient()
        contents = client.read_sql_file(sql_file_path)
        print(f"{contents=}")
        expected = 'CREATE TABLE IF NOT EXISTS users (\n    id INTEGER PRIMARY KEY AUTOINCREMENT,\n    name TEXT NOT NULL,\n    email TEXT UNIQUE\n)\n\nINSERT INTO users (name, email) VALUES ("Alice", "alice@example.com")\nINSERT INTO users (name, email) VALUES ("Bob", "bob@example.com")\n\nSELECT * FROM users\nSELECT * FROM users WHERE name = "Alice"\n'
        assert contents == expected
    
    def test_execute_sql_file(self):
        with SQLiteClient() as client:
            sql_file_path = "PythonSandbox/test/sql_test_files/users_sample.sql"
            sql_lines = client.read_sql_file(sql_file_path)
            print(f"{sql_lines=}")
            client.execute_script(sql_lines)

            users_df = client.fetch_all_as_pd("""
                SELECT * FROM users;
            """)
            print("users_df:", users_df)

