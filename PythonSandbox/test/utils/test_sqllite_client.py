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
            print("All users:", users)

            user = db.fetch_one("SELECT * FROM users WHERE name = ?", ("Alice",))
            print("Found user:", user)
    
    def test_2(self):
        print("hello!!!")