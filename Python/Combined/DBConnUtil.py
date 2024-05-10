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
        
    @staticmethod
    def closeConnection():
        if DBConnUtil.conn is not None:
            DBConnUtil.conn.close()
            DBConnUtil.conn = None
            print("Connection Closed")
        
        else:
            print("No such connection exists")
        return DBConnUtil.conn