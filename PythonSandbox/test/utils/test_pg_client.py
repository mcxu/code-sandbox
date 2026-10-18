import pytest
import os
from PythonSandbox.utils.pg_client import PgClient

class TestPgClient:
    def test_execute_sql_file(self, pg_client: PgClient):
        sql_file_path = "PythonSandbox/test/sql_test_files/users_sample_pg.sql"
        sql_lines = pg_client.read_sql_file(sql_file_path)
        print(f"{sql_lines=}")
        pg_client.execute_script(sql_lines)

        df = pg_client.fetch_all_as_pd("SELECT * FROM users")
        print(f"{df=}\n")
        