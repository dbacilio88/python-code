import psycopg2

# Global constant
PSQL_HOST = "cbaciliod.ciad5dsiooyi.sa-east-1.rds.amazonaws.com"
PSQL_PORT = "5432"
PSQL_USER = "postgres"
PSQL_PASS = "C44910167d"
PSQL_DB = "cinfe"

# Connection
connection_address = """
host=%s port=%s user=%s password=%s dbname=%s
""" % (PSQL_HOST, PSQL_PORT, PSQL_USER, PSQL_PASS, PSQL_DB)
connection = psycopg2.connect(connection_address)

cursor = connection.cursor()

# Query
SQL = "SELECT * FROM \"Coaquira\";"
cursor.execute(SQL)

# Get Values
all_values = cursor.fetchall()

cursor.close()
connection.close()

for data in all_values:
    print('Get values: ', data[1])


print(all_values)
#print(conexion)

