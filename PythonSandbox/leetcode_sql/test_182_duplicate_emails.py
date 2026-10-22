# https://leetcode.com/problems/duplicate-emails/description/

from pathlib import Path
RESOURCES_DIR = f"{Path(__file__).parent.parent}/lc_sql_resources"

class TestDuplicateEmails:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Person;

            Create table If Not Exists Person (id int, email varchar(255));
            Truncate table Person;
            insert into Person (id, email) values ('1', 'a@b.com');
            insert into Person (id, email) values ('2', 'c@d.com');
            insert into Person (id, email) values ('3', 'a@b.com');
        """)
        person_df = pg_client.fetch_all_as_pd("SELECT * FROM Person")
        print("\n", person_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT email
            FROM Person
            GROUP BY email
            HAVING COUNT(email) > 1;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
