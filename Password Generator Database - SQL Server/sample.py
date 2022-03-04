import pyodbc
driver_names = [x for x in pyodbc.drivers() if x.endswith(' for SQL Server')]
print(driver_names)