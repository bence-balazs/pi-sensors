import database
import logger
import sys
import os

def main():
    uptime = os.popen("awk '{print $1}' /proc/uptime").read()
    print(uptime)

    # try:
    #     database.insertToDb("uptime", uptime)
    # except:
    #     database.closeDb
    #     logger.logErrors("uptime: FAILED to insert in to the database")
    #     sys.exit(1)

if __name__ == "__main__":
    main()
