class TestConfirmationRate:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Signups, Confirmations;
            DROP TYPE IF EXISTS confirmation_action;
            CREATE TYPE confirmation_action AS ENUM ('confirmed', 'timeout');

            Create table If Not Exists Signups (user_id int, time_stamp timestamp);
            Create table If Not Exists Confirmations (user_id int, time_stamp timestamp, action confirmation_action);
            Truncate table Signups;
            insert into Signups (user_id, time_stamp) values ('3', '2020-03-21 10:16:13');
            insert into Signups (user_id, time_stamp) values ('7', '2020-01-04 13:57:59');
            insert into Signups (user_id, time_stamp) values ('2', '2020-07-29 23:09:44');
            insert into Signups (user_id, time_stamp) values ('6', '2020-12-09 10:39:37');
            Truncate table Confirmations;
            insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-01-06 03:30:46', 'timeout');
            insert into Confirmations (user_id, time_stamp, action) values ('3', '2021-07-14 14:00:00', 'timeout');
            insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-12 11:57:29', 'confirmed');
            insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-13 12:58:28', 'confirmed');
            insert into Confirmations (user_id, time_stamp, action) values ('7', '2021-06-14 13:59:27', 'confirmed');
            insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-01-22 00:00:00', 'confirmed');
            insert into Confirmations (user_id, time_stamp, action) values ('2', '2021-02-28 23:59:59', 'timeout');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Signups")
        print("\n", data_df)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Confirmations")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT s.user_id, 
                ROUND(
                    (COUNT(action) FILTER (WHERE action = 'confirmed'))::numeric/(COUNT(s.user_id)),
                    2
                ) AS confirmation_rate
            FROM Signups s
            LEFT JOIN Confirmations c
            ON s.user_id = c.user_id
            GROUP BY s.user_id;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)