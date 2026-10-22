from pathlib import Path
RESOURCES_DIR = f"{Path(__file__).parent.parent}/lc_sql_resources"

class TestRisingTemp:
    def test_setup(self, pg_client):
        prep = """
            DROP TABLE IF EXISTS Weather;
        """
        query = """
            Create table If Not Exists Weather (id int, recordDate date, temperature int);
            Truncate table Weather;
            insert into Weather (id, recordDate, temperature) values ('1', '2015-01-01', '10');
            insert into Weather (id, recordDate, temperature) values ('2', '2015-01-02', '25');
            insert into Weather (id, recordDate, temperature) values ('3', '2015-01-03', '20');
            insert into Weather (id, recordDate, temperature) values ('4', '2015-01-04', '30');
        """
        pg_client.execute(prep)
        pg_client.execute(query)
        weather_df = pg_client.fetch_all_as_pd("SELECT * FROM Weather;")
        print("Weather:\n", weather_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT currDates.id
            FROM Weather currDates
            INNER JOIN Weather prevDates
            ON (currDates.recordDate - prevDates.recordDate) = 1
            WHERE currDates.temperature > prevDates.temperature;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("Output:\n", output_df)
    
    