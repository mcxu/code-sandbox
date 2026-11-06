class TestProductSalesAnalysis:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Sales, Product;

            Create table If Not Exists Sales (sale_id int, product_id int, year int, quantity int, price int);
            Create table If Not Exists Product (product_id int, product_name varchar(10));
            Truncate table Sales;
            insert into Sales (sale_id, product_id, year, quantity, price) values ('1', '100', '2008', '10', '5000');
            insert into Sales (sale_id, product_id, year, quantity, price) values ('2', '100', '2009', '12', '5000');
            insert into Sales (sale_id, product_id, year, quantity, price) values ('7', '200', '2011', '15', '9000');
            Truncate table Product;
            insert into Product (product_id, product_name) values ('100', 'Nokia');
            insert into Product (product_id, product_name) values ('200', 'Apple');
            insert into Product (product_id, product_name) values ('300', 'Samsung');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Sales")
        print("\n", data_df)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Product")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT product_name, year, price
            FROM Sales s
            LEFT JOIN Product p
            ON s.product_id = p.product_id
            ORDER BY year ASC;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
