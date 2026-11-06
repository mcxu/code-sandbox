class TestInvalidTweets:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Tweets;

            Create table If Not Exists Tweets(tweet_id int, content varchar(50));
            Truncate table Tweets;
            insert into Tweets (tweet_id, content) values ('1', 'Let us Code');
            insert into Tweets (tweet_id, content) values ('2', 'More than fifteen chars are here!');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Tweets")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT tweet_id
            FROM Tweets
            WHERE LENGTH(content) > 15;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
