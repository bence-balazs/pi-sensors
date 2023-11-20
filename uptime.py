import database
import logger
import sys
import os

def main():
    uptime = os.popen("awk '{print $1}' /proc/uptime").read()
    uptime = float(uptime)
    uptime = float(format((uptime / 60) / 60, '.1f'))

    try:
        database.insertToDb("uptime", uptime)
    except:
        database.closeDb
        logger.logErrors("uptime: FAILED to insert in to the database")
        sys.exit(1)

if __name__ == "__main__":
    main()
