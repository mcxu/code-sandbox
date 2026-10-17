# https://leetcode.com/problems/combine-two-tables/

from PythonSandbox.utils.sqllite_client import SQLiteClient

class CombineTwoTables:
    def __init__(self):
        self.db_name = "sqlpractice.db"
        
    def insert(self):
        with SQLiteClient(self.db_name) as db:
            db.execute_script_file("./PythonSandbox/leetcode_sql/175_combine_two_tables.sql")
            person_df = db.fetch_all_as_pd("SELECT * FROM Person")
            address_df = db.fetch_all_as_pd("SELECT * FROM Address")
            print(
                person_df, "\n",
                address_df
            )
    
    def select(self):
        pass

    def test1(self):
        self.insert()

    
if __name__ == "__main__":
    c = CombineTwoTables()
    c.test1()

