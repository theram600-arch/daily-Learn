import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="victus123",
  database="mydatabase"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255),age int,marks int, address VARCHAR(255))")

# sql = "INSERT INTO customers (name,age,marks, address) VALUES (%s,%s,%s, %s)"
# val = ("deor",45,39, "hoshiarpur ")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mydb)


# mycursor.execute("SELECT * FROM customers")

# mycursor.execute("SELECT * FROM customers order by name")

# sql = "SELECT * FROM customers WHERE name ='John'"
# mycursor.execute(sql)
# myresult =mycursor.fetchall()
# for x in myresult:
#   print(x)


# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
# mycursor.execute(sql)
# mydb.commit()
# print(mycursor.rowcount, "record(s) deleted")

sql = "DROP TABLE customers"
mycursor.execute(sql)