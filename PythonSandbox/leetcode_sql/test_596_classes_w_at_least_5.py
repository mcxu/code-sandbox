class TestClassesWAtLeast5Students:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Courses;

            Create table If Not Exists Courses (student varchar(255), class varchar(255));
            Truncate table Courses;
            insert into Courses (student, class) values ('A', 'Math');
            insert into Courses (student, class) values ('B', 'English');
            insert into Courses (student, class) values ('C', 'Math');
            insert into Courses (student, class) values ('D', 'Biology');
            insert into Courses (student, class) values ('E', 'Math');
            insert into Courses (student, class) values ('F', 'Computer');
            insert into Courses (student, class) values ('G', 'Math');
            insert into Courses (student, class) values ('H', 'Math');
            insert into Courses (student, class) values ('I', 'Math');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Courses")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT class
            FROM Courses
            GROUP BY class
            HAVING COUNT(student) >= 5;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
