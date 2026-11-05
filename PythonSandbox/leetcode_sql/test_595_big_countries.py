class TestBigCountries:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS World;

            Create table If Not Exists World (name varchar(255), continent varchar(255), area int, population int, gdp bigint);
            Truncate table World;
            insert into World (name, continent, area, population, gdp) values ('Afghanistan', 'Asia', '652230', '25500100', '20343000000');
            insert into World (name, continent, area, population, gdp) values ('Albania', 'Europe', '28748', '2831741', '12960000000');
            insert into World (name, continent, area, population, gdp) values ('Algeria', 'Africa', '2381741', '37100000', '188681000000');
            insert into World (name, continent, area, population, gdp) values ('Andorra', 'Europe', '468', '78115', '3712000000');
            insert into World (name, continent, area, population, gdp) values ('Angola', 'Africa', '1246700', '20609294', '100990000000');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM World")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT name, population, area
            FROM World
            WHERE area >= 3e6
            OR population >= 25e6;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
