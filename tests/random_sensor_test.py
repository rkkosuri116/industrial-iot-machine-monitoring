import random
import time

while True:

    temperature = round(random.uniform(45.0,46.5),2)
    rpm = round(random.randint(1490,1505))
    power = round(random.uniform(5.4,5.8),2)
    vibration = round(random.uniform(1.0,1.3),2)

    print(f"Temperature: {temperature}")
    print(f"RPM: {rpm}")
    print(f"Power: {power}")
    print(f"Vibration: {vibration}")
    print("----------------------")

    time.sleep(1)
