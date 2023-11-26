import qr_scanner
import mysql.connector

connection = mysql.connector.connect(
  host="localhost",
  user="root",
  password="RootUser123",
  database="attendance"
)

# Create a cursor object
cursor = connection.cursor()

roll_num = qr_scanner.roll_num
print("Hi")
print(roll_num)

# Execute a query
cursor.execute("INSERT INTO course (rollno) VALUES ('{}');".format(roll_num))
connection.commit()
cursor.execute("SELECT COUNT(*) FROM course;")
a = cursor.fetchall()
c = a[0][0]
b = int((100*c)/(c+6))
print(a[0][0])
