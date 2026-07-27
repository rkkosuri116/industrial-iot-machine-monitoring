import paho.mqtt.client as mqtt
import json
import time
import random

#MQTT Configuration

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/test"

# Generate machine data 

def generate_machine_data():
    temperature = round(random.uniform(45.0,46.5),2)
    rpm = random.randint(1490,1505)
    power = round(random.uniform(5.4,5.8),2)
    vibration = round(random.uniform(1.0,1.3),2)

    return {
        "machine_id" : "M001",
        "temperature" : temperature,
        "rpm" : rpm,
        "power" : power,
        "vibration" : vibration,
        "status" :"Running"
    }
def main():

    client = mqtt.Client()
    client.connect(BROKER, PORT)

    print("Connected to MQTT Broker.")
    print("Publishing machine data...\n")


    try:
        while True:
            machine_data = generate_machine_data()

            json_data = json.dumps(machine_data)

            client.publish(TOPIC,json_data)

            print(f"Published: {machine_data}")

            time.sleep(1)
    except KeyboardInterrupt:
        print("\n Stopping publisher....")
    finally:
        client.disconnect()
        print("Disconnected from MQTT Broker.")

if __name__=="__main__":
    main()