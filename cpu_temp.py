from gpiozero import CPUTemperature

def main():
    sensor = format(CPUTemperature(), '.1f')
    cpu = format(sensor.temperature, '.1f')
    print(cpu)

if __name__ == "__main__":
    main()
