
class PropertyUtil:

    @staticmethod
    def getPropertyString():
        server_name = "Mathesh-PC"
        database_name = "testbeta"
        trusted_connection = "Yes"

        connectionString = f"Driver={{SQL Server}}; Server={server_name}; Database={database_name}; Trusted_Connection={trusted_connection}"
        return connectionString