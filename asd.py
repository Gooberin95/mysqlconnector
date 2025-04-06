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

mycursor.execute('SELECT MAX(salary) FROM employees')

myresult = mycursor.fetchall()

for x in myresult:
    print(x)


