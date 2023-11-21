import time
import board
import adafruit_dht
import sys
import database
import logger

dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)

def main():
    i = 1
    while i != 0:
        try:
            # Get the values from the serial port
            temperature_c = dhtDevice.temperature
            humidity = dhtDevice.humidity
        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            time.sleep(1.0)
            continue
        except Exception as error:
            dhtDevice.exit()
            raise error
        if temperature_c != None:
            i = 0

    # temperature: insert in to the database
    try:
        database.insertToDb("dht22_temp", temperature_c)
        database.insertToDb("dht22_hum", humidity)
    except:
        print("Error: wrong insert!")
        database.closeDb
        logger.logErrors("dht22_sens.py: FAILED to insert in to the database")
        sys.exit(1)

    database.closeDb()


if __name__ == "__main__":
    main()
