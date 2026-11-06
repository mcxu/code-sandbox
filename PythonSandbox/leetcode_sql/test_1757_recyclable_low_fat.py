class TestRecyclableLowFats:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Products;
            CREATE TYPE yn AS ENUM ('Y', 'N');

            Create table If Not Exists Products (product_id int, low_fats yn, recyclable yn);
            Truncate table Products;
            insert into Products (product_id, low_fats, recyclable) values ('0', 'Y', 'N');
            insert into Products (product_id, low_fats, recyclable) values ('1', 'Y', 'Y');
            insert into Products (product_id, low_fats, recyclable) values ('2', 'N', 'Y');
            insert into Products (product_id, low_fats, recyclable) values ('3', 'Y', 'Y');
            insert into Products (product_id, low_fats, recyclable) values ('4', 'N', 'N');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Products")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT product_id
            FROM Products
            WHERE low_fats = 'Y' and recyclable = 'Y';
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
