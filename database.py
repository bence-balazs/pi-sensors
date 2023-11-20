import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    database=os.environ.get("pg.database"),
    host=os.environ.get("pg.host"),
    user=os.environ.get("pg.user"),
    password=os.environ.get("pg.password"),
    port=os.environ.get("pg.port"),
)
cursor = conn.cursor()

def closeDb():
    conn.close()

def insertToDb(table, value):
    cursor.execute(f"INSERT into {table} (temp) VALUES ({value});")
    conn.commit()
