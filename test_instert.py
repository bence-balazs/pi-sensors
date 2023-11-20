import database
import sys

def main():

    try:
        database.insertToDb("cpu_temp", 25111113)
    except:
        print("Error: wrong insert!")
        database.closeDb
        sys.exit(1)

    try:
        database.queryDb("cpua_temp")
    except:
        print("queryDb: something went wrong")
        database.closeDb()
        sys.exit(1)

    database.closeDb()
main()
