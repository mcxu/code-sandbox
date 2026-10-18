# https://leetcode.com/problems/employees-earning-more-than-their-managers/

from pathlib import Path

RESOURCES_DIR = f"{Path(__file__).parent.parent}/lc_sql_resources"

class TestEmployeesEarnings:
    def test_setup(self, pg_client):
        pg_client.execute_script_file(f"{RESOURCES_DIR}/181_schema.sql")
        employee_df = pg_client.fetch_all_as_pd("SELECT * FROM Employee")
        print("employees:\n", employee_df)
    
    def test_query(self, pg_client):
        query1 = """
            SELECT aux.empname as "Employee"
            FROM
            (
                SELECT a.name AS empname, a.salary AS empsalary,
                    b.name AS manname, b.salary AS mansalary
                FROM Employee a
                CROSS JOIN Employee b
                WHERE a.managerId = b.id
                AND a.salary > b.salary
            ) aux;
        """

        # much faster
        query2 = """
            SELECT a.name AS "Employee"
            FROM Employee a
            CROSS JOIN Employee b
            WHERE a.managerId = b.id
            AND a.salary > b.salary;
        """

        output = pg_client.fetch_all_as_pd(query2)
        print("output:\n", output)