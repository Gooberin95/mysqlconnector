import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("db_host")
user = os.getenv("db_user")
password = os.getenv("db_password")
database = os.getenv('db_database')


mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password,
    database = database
)

mycursor = mydb.cursor()

mycursor.execute(
"INSERT INTO employees (employee_id, first_name, last_name, department, title, salary)"
                 "VALUES ('77777', 'Billy', 'Bob', 'Facilities', 'Cleaner', 800000)"
)

mydb.commit()


mycursor.execute('SELECT * FROM employees')

myresult = mycursor.fetchall()

for row in myresult:
    print(row)

mydb.close()





