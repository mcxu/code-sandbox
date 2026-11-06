# https://leetcode.com/problems/average-time-of-process-per-machine/description/?envType=study-plan-v2&envId=top-sql-50

class TestAverageTimeOfProcessPerMachine:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Activity;

            CREATE TYPE se AS ENUM ('start', 'end');
            Create table If Not Exists Activity (machine_id int, process_id int, activity_type se, timestamp float);
            Truncate table Activity;
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'start', '0.712');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '0', 'end', '1.52');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'start', '3.14');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('0', '1', 'end', '4.12');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'start', '0.55');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '0', 'end', '1.55');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'start', '0.43');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('1', '1', 'end', '1.42');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'start', '4.1');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '0', 'end', '4.512');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'start', '2.5');
            insert into Activity (machine_id, process_id, activity_type, timestamp) values ('2', '1', 'end', '5');
            
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Activity")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT machine_id, process_id, activity_type, timestamp
            FROM Activity 
            WHERE activity_type = 'start';
        """
        """
            machine_id  process_id activity_type  timestamp
            0           0           0         start      0.712
            1           0           1         start      3.140
            2           1           0         start      0.550
            3           1           1         start      0.430
            4           2           0         start      4.100
            5           2           1         start      2.500
        """
        query2 = """
            SELECT machine_id, process_id, activity_type, timestamp
            FROM Activity 
            WHERE activity_type = 'end';
        """
        """
                machine_id  process_id activity_type  timestamp
            0           0           0           end      1.520
            1           0           1           end      4.120
            2           1           0           end      1.550
            3           1           1           end      1.420
            4           2           0           end      4.512
            5           2           1           end      5.000
        """
        query3 = """
            SELECT s.machine_id,
                ROUND(
                    SUM(e.timestamp - s.timestamp)::numeric/COUNT(s.process_id),
                    3
                ) AS processing_time
            FROM (
                SELECT * FROM Activity 
                WHERE activity_type = 'start'
            ) s 
            LEFT JOIN (
                SELECT * FROM Activity 
                WHERE activity_type = 'end'
            ) e 
            ON s.machine_id = e.machine_id AND s.process_id = e.process_id
            GROUP BY s.machine_id
            ORDER BY s.machine_id ASC;
        """

        output_df = pg_client.fetch_all_as_pd(query3)
        print("\n", output_df)