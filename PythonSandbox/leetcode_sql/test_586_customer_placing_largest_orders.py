class TestCustomerPlacingLargestNumberOfOrders:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Orders;

            Create table If Not Exists orders (order_number int, customer_number int);
            Truncate table orders;
            insert into orders (order_number, customer_number) values ('1', '1');
            insert into orders (order_number, customer_number) values ('2', '2');
            insert into orders (order_number, customer_number) values ('3', '3');
            insert into orders (order_number, customer_number) values ('4', '3');
        """)
        person_df = pg_client.fetch_all_as_pd("SELECT * FROM Orders")
        print("\n", person_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT customer_number
            FROM Orders
            GROUP BY customer_number
            ORDER BY COUNT(customer_number) DESC
            LIMIT 1;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("\n", output_df)
