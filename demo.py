import pypyodbc as odbc
DRIVER_NAME='SQL_SERVER'
SERVER_NAME='LAPTOP-OI5R2P2B\SQLEXPRESS'
DATABASE_NAME='demo'

connection_string=f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
"""



conn= odbc.connect(connection_string)
# print(conn)