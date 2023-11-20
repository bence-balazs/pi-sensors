import datetime

def logErrors(message):
    f = open("./logs/cpu_temp.log", "a")
    time = datetime.datetime.now()

    f.write(str(time.strftime("[%Y-%m-%d] %H:%M:%S")))
    f.write(" msg: ")
    f.write(message)

    f.write("\n")
    f.close
