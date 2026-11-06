class TestReplaceEmployeeIdWithUniqueId:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Employees, EmployeeUNI;

            Create table If Not Exists Employees (id int, name varchar(20));
            Create table If Not Exists EmployeeUNI (id int, unique_id int);
            Truncate table Employees;
            insert into Employees (id, name) values ('1', 'Alice');
            insert into Employees (id, name) values ('7', 'Bob');
            insert into Employees (id, name) values ('11', 'Meir');
            insert into Employees (id, name) values ('90', 'Winston');
            insert into Employees (id, name) values ('3', 'Jonathan');
            Truncate table EmployeeUNI;
            insert into EmployeeUNI (id, unique_id) values ('3', '1');
            insert into EmployeeUNI (id, unique_id) values ('11', '2');
            insert into EmployeeUNI (id, unique_id) values ('90', '3');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Employees")
        print("\n", data_df)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM EmployeeUNI")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT u.unique_id, e.name
            FROM Employees e
            LEFT JOIN EmployeeUNI u
            ON e.id = u.id;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
