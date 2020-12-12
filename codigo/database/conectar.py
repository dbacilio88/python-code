import psycopg2

HOST = "cbaciliod.ciad5dsiooyi.sa-east-1.rds.amazonaws.com"
HOST = "cbaciliod.ciad5dsiooyi.sa-east-1.rds.amazonaws.com"
PORT = "5432"
USER = "postgres"
PASSWORD = "C44910167d"
DATABASE = "cinfe"
#connection_address = """host=%s port=%s user=%s password=%s database=%s""" % (HOST,PORT,USER,PASSWORD,DATABASE)

connection = psycopg2.connect(user=USER,password=PASSWORD,host=HOST,database=DATABASE)

#conexion = psycopg2.connect(user=USER,password=PASSWORD,host=URL, database=DATABASE)
print(connection.values)
connection.close()
