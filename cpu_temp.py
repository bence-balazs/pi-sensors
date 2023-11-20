from gpiozero import CPUTemperature
from database import insertToDb

def main():
    sensor = CPUTemperature()
    cpu = format(sensor.temperature, '.1f')
    print(cpu)

if __name__ == "__main__":
    main()
