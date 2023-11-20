import datetime

def logErrors(file, message):
    f = open("./logs/pi-sensors.log", "a")
    time = datetime.datetime.now()

    f.write(str(time.strftime("[%Y-%m-%d] %H:%M:%S")))
    f.write(" msg: ")
    f.write(message)

    f.write("\n")
    f.close
