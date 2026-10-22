# https://leetcode.com/problems/customers-who-never-order/description/

from pathlib import Path
RESOURCES_DIR = f"{Path(__file__).parent.parent}/lc_sql_resources"

class TestCustomersWhoNeverOrder:
    def test_setup(self, pg_client):
        prep = """
            DROP TABLE IF EXISTS Customers;
            DROP TABLE IF EXISTS Orders;
        """
        query = """
            Create table If Not Exists Customers (id int, name varchar(255));
            Create table If Not Exists Orders (id int, customerId int);
            Truncate table Customers;
            insert into Customers (id, name) values ('1', 'Joe');
            insert into Customers (id, name) values ('2', 'Henry');
            insert into Customers (id, name) values ('3', 'Sam');
            insert into Customers (id, name) values ('4', 'Max');
            Truncate table Orders;
            insert into Orders (id, customerId) values ('1', '3');
            insert into Orders (id, customerId) values ('2', '1');
        """
        pg_client.execute(prep)
        pg_client.execute(query)
        customers_pd = pg_client.fetch_all_as_pd("SELECT * FROM Customers;")
        orders_pd = pg_client.fetch_all_as_pd("SELECT * FROM Orders;")
        print("Customers:\n", customers_pd)
        print("Orders:\n", orders_pd)
        """
        Customers:
            id   name
        0   1    Joe
        1   2  Henry
        2   3    Sam
        3   4    Max
        Orders:
            id  customerid
        0   1           3
        1   2           1
        """
    
    def test_query(self, pg_client):
        query = """
            SELECT Customers.name as "Customers"
            FROM Customers
            LEFT JOIN Orders
            ON Customers.id = Orders.customerId
            WHERE Orders.customerId IS NULL;
        """
        output_df = pg_client.fetch_all_as_pd(query)
        print("Output:\n", output_df)