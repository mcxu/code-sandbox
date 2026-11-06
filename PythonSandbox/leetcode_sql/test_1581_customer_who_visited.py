# https://leetcode.com/problems/customer-who-visited-but-did-not-make-any-transactions/description/?envType=study-plan-v2&envId=top-sql-50

class TestCustomerWhoVisited:
    def test_setup(self, pg_client):
        pg_client.execute("""
            DROP TABLE IF EXISTS Visits, Transactions;

            Create table If Not Exists Visits(visit_id int, customer_id int);
            Create table If Not Exists Transactions(transaction_id int, visit_id int, amount int);
            Truncate table Visits;
            insert into Visits (visit_id, customer_id) values ('1', '23');
            insert into Visits (visit_id, customer_id) values ('2', '9');
            insert into Visits (visit_id, customer_id) values ('4', '30');
            insert into Visits (visit_id, customer_id) values ('5', '54');
            insert into Visits (visit_id, customer_id) values ('6', '96');
            insert into Visits (visit_id, customer_id) values ('7', '54');
            insert into Visits (visit_id, customer_id) values ('8', '54');
            Truncate table Transactions;
            insert into Transactions (transaction_id, visit_id, amount) values ('2', '5', '310');
            insert into Transactions (transaction_id, visit_id, amount) values ('3', '5', '300');
            insert into Transactions (transaction_id, visit_id, amount) values ('9', '5', '200');
            insert into Transactions (transaction_id, visit_id, amount) values ('12', '1', '910');
            insert into Transactions (transaction_id, visit_id, amount) values ('13', '2', '970');
        """)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Visits")
        print("\n", data_df)
        data_df = pg_client.fetch_all_as_pd("SELECT * FROM Transactions")
        print("\n", data_df)
    
    def test_query(self, pg_client):
        query = """
            SELECT *
            FROM Transactions t
            LEFT JOIN Visits v
            ON t.visit_id = v.visit_id
        """
        
        query2 = """
            SELECT v.customer_id, COUNT(visit_id) AS count_no_trans
            FROM Visits v
            WHERE visit_id NOT IN (
                SELECT t.visit_id
                FROM Transactions t
                LEFT JOIN Visits v
                ON t.visit_id = v.visit_id
            ) 
            GROUP BY v.customer_id
            ORDER BY count_no_trans DESC;
        """

        output_df = pg_client.fetch_all_as_pd(query2)
        print("\n", output_df)
