class TestNoBoringMovies:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Cinema;

            Create table If Not Exists cinema (id int, movie varchar(255), description varchar(255), rating numeric(2, 1));
            Truncate table cinema;
            insert into cinema (id, movie, description, rating) values ('1', 'War', 'great 3D', '8.9');
            insert into cinema (id, movie, description, rating) values ('2', 'Science', 'fiction', '8.5');
            insert into cinema (id, movie, description, rating) values ('3', 'irish', 'boring', '6.2');
            insert into cinema (id, movie, description, rating) values ('4', 'Ice song', 'Fantacy', '8.6');
            insert into cinema (id, movie, description, rating) values ('5', 'House card', 'Interesting', '9.1');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Cinema")
        print("Data:\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT *
            FROM Cinema
            WHERE id % 2 = 1
            AND description NOT LIKE '%boring%'
            ORDER BY rating DESC;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("Output\n", output_df)
