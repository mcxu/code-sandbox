class TestFindCustomerReferee:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Customer;

            Create table If Not Exists Customer (id int, name varchar(25), referee_id int);
            Truncate table Customer;
            insert into Customer (id, name, referee_id) values ('1', 'Will', NULL);
            insert into Customer (id, name, referee_id) values ('2', 'Jane', NULL);
            insert into Customer (id, name, referee_id) values ('3', 'Alex', '2');
            insert into Customer (id, name, referee_id) values ('4', 'Bill', NULL);
            insert into Customer (id, name, referee_id) values ('5', 'Zack', '1');
            insert into Customer (id, name, referee_id) values ('6', 'Mark', '2');
        """)
        person_df = pg_client.fetch_all_as_pd("SELECT * FROM Customer")
        print("\n", person_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT name 
            FROM Customer
            WHERE referee_id != 2 OR referee_id IS NULL;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
