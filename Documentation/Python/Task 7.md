# Task 7: Database connectivity

- Each service in our project requires a database connection.
- Hence a package named `util` is created with `PropertyUtil` class for getting the connction string dynamically through a `@staticmethod`
- The connection string is returned whenever the `DBConnUtil` class makes call to the `getConnectionString` method of `PropertyUtil`
- The connection string this retrieved is used for establishing connection between the SQL Server and our Application through `PyODBC` package