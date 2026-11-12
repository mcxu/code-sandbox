# https://leetcode.com/problems/managers-with-at-least-5-direct-reports/description/?envType=study-plan-v2&envId=top-sql-50

class TestManagersWAtLeast5DirectReports:
    def test_setup(self, pg_client):
        
        query = """
            DROP TABLE IF EXISTS Employee;

            Create table If Not Exists Employee (id int, name varchar(255), department varchar(255), managerId int);
            Truncate table Employee;
        """

        a = """
            insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL);
            insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '100');
            insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '100');
            insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '100');
            insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '100');
            insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '100');
        """

        b = """
            insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL);
            insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
        """

        c = """
            insert into Employee (id, name, department, managerId) values ('101', 'John', 'A', NULL);
            insert into Employee (id, name, department, managerId) values ('102', 'Dan', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('103', 'James', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('104', 'Amy', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('105', 'Anne', 'A', '101');
            insert into Employee (id, name, department, managerId) values ('106', 'Ron', 'B', '101');
            insert into Employee (id, name, department, managerId) values ('107', 'Tom', 'A', '102');
            insert into Employee (id, name, department, managerId) values ('108', 'Tommy', 'A', '102');
            insert into Employee (id, name, department, managerId) values ('109', 'Peter', 'C', '102');
            insert into Employee (id, name, department, managerId) values ('110', 'Dong', 'A', '102');
        """

        d = """
            insert into Employee (id, name, department, managerId) values ('101', NULL, 'A', NULL);
            insert into Employee (id, name, department, managerId) values ('102', NULL, 'A', '101');
            insert into Employee (id, name, department, managerId) values ('103', NULL, 'A', '101');
            insert into Employee (id, name, department, managerId) values ('104', NULL, 'A', '101');
            insert into Employee (id, name, department, managerId) values ('105', NULL, 'A', '101');
            insert into Employee (id, name, department, managerId) values ('106', NULL, 'B', '101');
        """

        pg_client.execute(query + d)
        employee_df = pg_client.fetch_all_as_pd("SELECT * FROM Employee")
        print("Employee:\n", employee_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT a.name
            FROM Employee a
            CROSS JOIN Employee b
            WHERE a.id = b.managerId
            GROUP BY a.id, a.name
            HAVING COUNT(*) >= 5;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("Output\n", output_df)
