class TestStudentsAndExams:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Students, Subjects, Examinations;

            Create table If Not Exists Students (student_id int, student_name varchar(20));
            Create table If Not Exists Subjects (subject_name varchar(20));
            Create table If Not Exists Examinations (student_id int, subject_name varchar(20));
            Truncate table Students;
            insert into Students (student_id, student_name) values ('1', 'Alice');
            insert into Students (student_id, student_name) values ('2', 'Bob');
            insert into Students (student_id, student_name) values ('13', 'John');
            insert into Students (student_id, student_name) values ('6', 'Alex');
            Truncate table Subjects;
            insert into Subjects (subject_name) values ('Math');
            insert into Subjects (subject_name) values ('Physics');
            insert into Subjects (subject_name) values ('Programming');
            Truncate table Examinations;
            insert into Examinations (student_id, subject_name) values ('1', 'Math');
            insert into Examinations (student_id, subject_name) values ('1', 'Physics');
            insert into Examinations (student_id, subject_name) values ('1', 'Programming');
            insert into Examinations (student_id, subject_name) values ('2', 'Programming');
            insert into Examinations (student_id, subject_name) values ('1', 'Physics');
            insert into Examinations (student_id, subject_name) values ('1', 'Math');
            insert into Examinations (student_id, subject_name) values ('13', 'Math');
            insert into Examinations (student_id, subject_name) values ('13', 'Programming');
            insert into Examinations (student_id, subject_name) values ('13', 'Physics');
            insert into Examinations (student_id, subject_name) values ('2', 'Math');
            insert into Examinations (student_id, subject_name) values ('1', 'Math');
        """)
        students_df = pg_client.fetch_all_as_pd("SELECT * FROM Students")
        print("Students:\n", students_df)
        subjects_df = pg_client.fetch_all_as_pd("SELECT * FROM Subjects")
        print("Subjects:\n", subjects_df)
        exams_df = pg_client.fetch_all_as_pd("SELECT * FROM Examinations")
        print("Examinations:\n", exams_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT ex.student_id, st.student_name, ex.subject_name, 
                COUNT((st.student_name, ex.subject_name))
            FROM Examinations ex
            LEFT JOIN Students st
            USING (student_id)
            GROUP BY ex.student_id, st.student_name, ex.subject_name
            ORDER BY ex.student_id ASC;
        """

        query2 = """
            SELECT st.student_id, st.student_name, su.subject_name,
                COUNT(ex.student_id) AS attended_exams
            FROM Students st
            CROSS JOIN Subjects su
            LEFT JOIN Examinations ex
                ON st.student_id = ex.student_id 
                AND su.subject_name = ex.subject_name
            GROUP BY st.student_id, st.student_name, su.subject_name
            ORDER BY st.student_id, su.subject_name;
        """

        output_df = pg_client.fetch_all_as_pd(query2)
        print("Output\n", output_df)
