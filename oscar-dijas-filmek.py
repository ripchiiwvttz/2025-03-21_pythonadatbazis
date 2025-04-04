import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql"
)

mycursor = mydb.cursor()


DATABASE = "oscar"
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {DATABASE}")


mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(f"{x[0]}")


mycursor.execute("""SELECT ev FROM film GROUP BY ev HAVING COUNT(id) >= 10;""")
for x in mycursor:
    print(f"{x[0]}")