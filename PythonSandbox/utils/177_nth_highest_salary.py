import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))

from utils.sqllite_client import SQLiteClient

class NthHighestSalary:

    def __init__(self):
        self.db = SQLiteClient(r"/Users/michaelxu/Documents/Job_Apps_and_Resume/Companies_2025/Apollo/apollo.db")
        self.db.connect()
        self.db.execute("DROP TABLE IF EXISTS employees")

    def nthHighestSalary(self, n: int) -> int:
        with self.db as db:
            return db.fetch_one("SELECT DISTINCT salary FROM employees ORDER BY salary DESC LIMIT 1 OFFSET ?", (n-1,))
    
    def test_nthHighestSalary(self):
        self.createTable()
        n = 3
        result = self.nthHighestSalary(n)
        print("result: ", result)
    
    def createTable(self):
        with self.db as db:
            db.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, salary INTEGER)")
            db.execute("""INSERT INTO employees (salary) VALUES 
                (100), (200), (300), (400), (500)""")

    def test_createTable(self):
        with self.db as db:
            db.execute("CREATE TABLE IF NOT EXISTS employees (id INTEGER PRIMARY KEY AUTOINCREMENT, salary INTEGER)")
            db.execute("""INSERT INTO employees (salary) VALUES 
                (100), (200), (300), (400), (500)""")
            results = db.fetch_all("SELECT * FROM employees")
            print("employees:", results)

if __name__ == "__main__":
    c = NthHighestSalary()
    # c.test_createTable()
    c.test_nthHighestSalary()