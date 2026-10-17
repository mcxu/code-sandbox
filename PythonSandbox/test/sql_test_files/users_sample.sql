CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE
);

INSERT INTO users (name, email) VALUES ("Alice", "alice@example.com");
INSERT INTO users (name, email) VALUES ("Bob", "bob@example.com");

-- SELECT * FROM users;
-- SELECT * FROM users WHERE name = "Alice";
