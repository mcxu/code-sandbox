class TestAvgSellingPrice:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Prices, UnitsSold;

            Create table If Not Exists Prices (product_id int, start_date date, end_date date, price int);
            Create table If Not Exists UnitsSold (product_id int, purchase_date date, units int);
            Truncate table Prices;
            insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-02-17', '2019-02-28', '5');
            insert into Prices (product_id, start_date, end_date, price) values ('1', '2019-03-01', '2019-03-22', '20');
            insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-01', '2019-02-20', '15');
            insert into Prices (product_id, start_date, end_date, price) values ('2', '2019-02-21', '2019-03-31', '30');
            Truncate table UnitsSold;
            insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-02-25', '100');
            insert into UnitsSold (product_id, purchase_date, units) values ('1', '2019-03-01', '15');
            insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-02-10', '200');
            insert into UnitsSold (product_id, purchase_date, units) values ('2', '2019-03-22', '30');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Prices")
        print("Data:\n", data_df)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM UnitsSold")
        print("Data:\n", data_df)
        """
            product_id  start_date    end_date  price
        0           1  2019-02-17  2019-02-28      5
        1           1  2019-03-01  2019-03-22     20
        2           2  2019-02-01  2019-02-20     15
        3           2  2019-02-21  2019-03-31     30
            Data:
            product_id purchase_date  units
        0           1    2019-02-25    100
        1           1    2019-03-01     15
        2           2    2019-02-10    200
        3           2    2019-03-22     30
        """
    
    def test_query(self, pg_client):
        query = """
            SELECT pr.product_id, 
                ROUND(
                    COALESCE(
                        SUM(pr.price * us.units)::numeric/NULLIF(SUM(us.units), 0), 
                        0
                    ),
                    2
                ) AS average_price
            FROM Prices pr
            LEFT JOIN UnitsSold us
            ON pr.product_id = us.product_id
            AND us.purchase_date BETWEEN pr.start_date AND pr.end_date
            GROUP BY pr.product_id;
        """

        output_df = pg_client.fetch_all_as_pd(query)
        print("Output\n", output_df)
