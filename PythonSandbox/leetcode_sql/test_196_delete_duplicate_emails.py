class TestDeleteDuplicateEmails:
    def test_setup(self, pg_client):
        pg_client.execute("""
            -- DROP TABLE IF EXISTS Person;

            Create table If Not Exists Person (Id int, Email varchar(255));
            Truncate table Person;
            insert into Person (id, email) values ('1', 'john@example.com');
            insert into Person (id, email) values ('2', 'bob@example.com');
            insert into Person (id, email) values ('3', 'john@example.com');
        """)
        person_df = pg_client.fetch_all_as_pd("SELECT * FROM Person")
        print("\n", person_df)
    
    def test_query(self, pg_client):
        # inner = """
        #     SELECT *
        #     FROM Person p1, Person p2
        #     WHERE p1.email = p2.email;
        # """
        # temp = pg_client.fetch_all_as_pd(inner)
        # print("temp:\n", temp)

        query = """
            DELETE FROM Person 
            WHERE id IN (
                SELECT p1.id
                FROM Person p1, Person p2
                WHERE p1.email = p2.email
                AND p1.id > p2.id
            );
        """
        pg_client.execute(query)
        person_df = pg_client.fetch_all_as_pd("SELECT * FROM Person")
        print("\n", person_df)

