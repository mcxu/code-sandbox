class TestDeptTop3Salaries:
    def test_setup(self, pg_client):
        query = """
            DROP TABLE IF EXISTS Employee, Department;

            Create table If Not Exists Employee (id int, name varchar(255), salary int, departmentId int);
            Create table If Not Exists Department (id int, name varchar(255));
            Truncate table Employee;
            insert into Employee (id, name, salary, departmentId) values ('1', 'Joe', '85000', '1');
            insert into Employee (id, name, salary, departmentId) values ('2', 'Henry', '80000', '2');
            insert into Employee (id, name, salary, departmentId) values ('3', 'Sam', '60000', '2');
            insert into Employee (id, name, salary, departmentId) values ('4', 'Max', '90000', '1');
            insert into Employee (id, name, salary, departmentId) values ('5', 'Janet', '69000', '1');
            insert into Employee (id, name, salary, departmentId) values ('6', 'Randy', '85000', '1');
            insert into Employee (id, name, salary, departmentId) values ('7', 'Will', '70000', '1');
            Truncate table Department;
            insert into Department (id, name) values ('1', 'IT');
            insert into Department (id, name) values ('2', 'Sales');
        """
        pg_client.execute(query)
        emp_df = pg_client.fetch_all_as_pd("SELECT * FROM Employee;")
        dept_df = pg_client.fetch_all_as_pd("SELECT * FROM Department;")
        print("\nemp_df:\n", emp_df)
        print("\ndept_df:\n", dept_df)
    
    def test_query(self, pg_client):
        query1 = """
            SELECT 
                d.name AS "Department", 
                e.name AS "Employee", 
                e.salary AS "Salary"
            FROM Employee e
            LEFT JOIN Department d
            ON e.departmentid = d.id
        """

        query2 = """
            SELECT 
                e.name, 
                e.salary, 
                e.departmentId,
                DENSE_RANK() OVER (
                    PARTITION BY e.departmentId
                    ORDER BY e.salary DESC
                ) rnk
            FROM Employee e
        """
        """
             name  salary  departmentid  rnk
        0    Max   90000             1    1
        1    Joe   85000             1    2
        2  Randy   85000             1    2
        3   Will   70000             1    3
        4  Janet   69000             1    4
        5  Henry   80000             2    1
        6    Sam   60000             2    2
        """

        query3 = """
            SELECT 
                d.name,
                e.name, 
                e.salary,
                DENSE_RANK() OVER (
                    PARTITION BY d.name
                    ORDER BY e.salary DESC
                ) rnk
            FROM Employee e
            LEFT JOIN Department d
            ON e.departmentId = d.id;
        """
        """ query2 output:
           Department Employee  Salary  rnk
        0         IT      Max   90000    1
        1         IT      Joe   85000    2
        2         IT    Randy   85000    2
        3         IT     Will   70000    3
        4         IT    Janet   69000    4
        5      Sales    Henry   80000    1
        6      Sales      Sam   60000    2
        """

        query4 = """
            SELECT 
                d.name AS "Department", 
                cte.name AS "Employee", 
                cte.salary AS "Salary"
            FROM ( 
                SELECT 
                    e.name, 
                    e.salary, 
                    e.departmentId,
                    DENSE_RANK() OVER (
                        PARTITION BY e.departmentId
                        ORDER BY e.salary DESC
                    ) rnk
                FROM Employee e
            ) cte
            LEFT JOIN Department d
            ON cte.departmentId = d.id
            WHERE cte.rnk <= 3;
        """

        output_df = pg_client.fetch_all_as_pd(query4)
        print("\noutput_df:\n", output_df)

