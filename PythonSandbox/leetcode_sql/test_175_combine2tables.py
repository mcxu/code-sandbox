# https://leetcode.com/problems/combine-two-tables/

from pathlib import Path

RESOURCES_DIR = f"{Path(__file__).parent.parent}/lc_sql_resources"

class TestCombineTwoTables:
    def test_setup(self, pg_client):
        pg_client.execute_script_file(f"{RESOURCES_DIR}/175_schema.sql")
        person_df = pg_client.fetch_all_as_pd("SELECT * FROM Person")
        address_df = pg_client.fetch_all_as_pd("SELECT * FROM Address")
        print("\n",
            person_df, "\n",
            address_df
        )
        """
            personid firstname lastname
        0         1     Allen     Wang
        1         2       Bob    Alice 
            addressid  personid           city       state
        0          1         2  New York City    New York
        1          2         3       Leetcode  California
        """
    
    def test_query(self, pg_client):
        query = pg_client.read_sql_file(f"{RESOURCES_DIR}/175_query.sql")
        result = pg_client.fetch_all_as_pd(query)
        print("result:\n", result)

        query2 = """
            SELECT 
            Person.firstname, 
            Person.lastname, 
            Address.city, 
            Address.state
            FROM Address
            RIGHT JOIN Person ON
            Person.personid = Address.personid;
        """
        result2 = pg_client.fetch_all_as_pd(query2)
        print("result2:\n", result2)
