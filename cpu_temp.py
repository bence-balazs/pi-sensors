from gpiozero import CPUTemperature
import database
import logger
import sys

def main():
    sensor = CPUTemperature()
    cpu = format(sensor.temperature, '.1f')
    
    try:
        database.insertToDb("cpu_temp", cpu)
    except:
        database.closeDb
        logger.logErrors("cpu_temp.py: FAILED to insert in to the database")
        sys.exit(1)

    database.closeDb()

if __name__ == "__main__":
    main()
