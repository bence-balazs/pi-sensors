import os
import psycopg2
import logger
import sys
from dotenv import load_dotenv

load_dotenv()

try:
    conn = psycopg2.connect(
        database=os.environ.get("pg.database"),
        host=os.environ.get("pg.host"),
        user=os.environ.get("pg.user"),
        password=os.environ.get("pg.password"),
        port=os.environ.get("pg.port"),
    )
except:
    logger.logErrors("database: connection was refused")
    sys.exit(1)

cursor = conn.cursor()

def insertToDb(table, value):
    cursor.execute(f"INSERT into {table} (value) VALUES ({value});")
    conn.commit()

def closeDb():
    conn.close()
