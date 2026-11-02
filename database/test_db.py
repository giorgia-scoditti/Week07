import mysql.connector
from mysql.connector import connect

cnx = mysql.connector.connect(option_files="db.cnf")

query = "SELECT * FROM trip"

cursor = cnx.cursor()
cursor.execute(query)

for row in cursor:
    print(row)

cursor.close()
cnx.close()