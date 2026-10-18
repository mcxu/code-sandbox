"""
File for shared test fixtures
"""

import pytest
import os
from PythonSandbox.utils.pg_client import PgClient

@pytest.fixture
def pg_client():
    PG_CLIENT = {
        "host": os.getenv("PG_HOST"),
        "port": int(os.getenv("PG_PORT")),
        "user": os.getenv("PG_USER"),
        "password": os.getenv("PG_PASSWORD"),
        "dbname": os.getenv("PG_DATABASE")
    }
    # print(f"PG_CLIENT=\n{PG_CLIENT}")
    with PgClient(**PG_CLIENT) as client:
        yield client
