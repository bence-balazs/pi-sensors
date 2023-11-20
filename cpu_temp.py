from gpiozero import CPUTemperature

def main():
    cpu_temp = format(CPUTemperature(), '.1f')
    print(cpu_temp)

if __name__ == "__main__":
    main()
