class TestEmployeeBonus:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Employee, Bonus;

            Create table If Not Exists Employee (empId int, name varchar(255), supervisor int, salary int);
            Create table If Not Exists Bonus (empId int, bonus int);
            Truncate table Employee;
            insert into Employee (empId, name, supervisor, salary) values ('3', 'Brad', NULL, '4000');
            insert into Employee (empId, name, supervisor, salary) values ('1', 'John', '3', '1000');
            insert into Employee (empId, name, supervisor, salary) values ('2', 'Dan', '3', '2000');
            insert into Employee (empId, name, supervisor, salary) values ('4', 'Thomas', '3', '4000');
            Truncate table Bonus;
            insert into Bonus (empId, bonus) values ('2', '500');
            insert into Bonus (empId, bonus) values ('4', '2000');
        """)
        employee_df = pg_client.fetch_all_as_pd("SELECT * FROM Employee")
        print("Employee:\n", employee_df)
        bonus_df = pg_client.fetch_all_as_pd("SELECT * FROM Bonus")
        print("Bonus:\n", bonus_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT e.name, b.bonus
            FROM Employee e
            LEFT JOIN Bonus b
            ON e.empId = b.empId
            WHERE b.bonus < 1000 OR b.bonus IS NULL;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("Output\n", output_df)
