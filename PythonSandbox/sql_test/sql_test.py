import sqlite3
print("sqllite3 import: ", sqlite3.__file__)
import _sqlite3
print("sqllite3 import: ", _sqlite3.__file__)
from sqlite3 import Error

def createConnection(dbFile):
    conn = None
    try:
        conn = sqlite3.connect(dbFile)
        print(sqlite3.version)
    except Error as e:
        print(e)
    # finally:
    #     if conn:
    #         conn.close()
    return conn

tableName = "projects"

createTableSQL = """CREATE TABLE IF NOT EXISTS {} (
                    id INTEGER PRIMARY KEY,
                    name TEXT,
                    begin_date DATETIME,
                    end_date DATETIME
                    )""".format(tableName)

getColsSQL = """PRAGMA table_info('{}')""".format(tableName)

insertSQL = """INSERT INTO {} (name,begin_date""".format(tableName)

def executeSql(conn):
    try:
        cursor = conn.cursor()
        res1 = cursor.execute(createTableSQL)
        #res2 = cursor.execute(getColsSQL)
        res3 = cursor.execute("INSERT INTO {}".)
        return res1
    except Error as e:
        print(e)

if __name__ == "__main__":
    conn = createConnection(r"C:\sqlite\sqltestdb.db")
    sqlResp = executeSql(conn)
    if sqlResp:
        print("response: ", sqlResp)
        print("printing rows")
        for row in sqlResp:
            print(row)

