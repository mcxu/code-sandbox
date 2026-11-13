class TestProjectEmployeesI:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Project, Employee;

            Create table If Not Exists Project (project_id int, employee_id int);
            Create table If Not Exists Employee (employee_id int, name varchar(10), experience_years int);
            Truncate table Project;
            insert into Project (project_id, employee_id) values ('1', '1');
            insert into Project (project_id, employee_id) values ('1', '2');
            insert into Project (project_id, employee_id) values ('1', '3');
            insert into Project (project_id, employee_id) values ('2', '1');
            insert into Project (project_id, employee_id) values ('2', '4');
            Truncate table Employee;
            insert into Employee (employee_id, name, experience_years) values ('1', 'Khaled', '3');
            insert into Employee (employee_id, name, experience_years) values ('2', 'Ali', '2');
            insert into Employee (employee_id, name, experience_years) values ('3', 'John', '1');
            insert into Employee (employee_id, name, experience_years) values ('4', 'Doe', '2');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Project")
        print("Data:\n", data_df)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Employee")
        print("Data:\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT p.project_id,
                ROUND(
                    SUM(e.experience_years)::numeric/COUNT(p.employee_id),
                    2
                ) AS average_years
            FROM Project p
            LEFT JOIN Employee e
            ON p.employee_id = e.employee_id
            GROUP BY p.project_id
            ORDER BY p.project_id ASC;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("Output\n", output_df)
