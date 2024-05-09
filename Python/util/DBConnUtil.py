import pyodbc

from PropertyUtil import PropertyUtil

class DBConnUtil:
    conn = None
    @staticmethod
    def getConnection():
        if DBConnUtil.conn is None:
            connectionString = PropertyUtil.getPropertyString()
            try:
                DBConnUtil.conn = pyodbc.connect(connectionString)
                print("Connection Established Successfully")
            except ConnectionError as err:
                print(f"Failed to establish connection: {err}")
        else:
            print("Connection already established")
        return DBConnUtil.conn