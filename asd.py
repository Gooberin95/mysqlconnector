import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("db_host")
user = os.getenv("db_user")
password = os.getenv("db_password")


mydb = mysql.connector.connect(
    host = host,
    user = user,
    password = password
)

print(mydb)
