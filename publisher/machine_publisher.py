import paho.mqtt.client as mqtt
import json

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/test"

machine_data = {
    "machine_id" : "M001",
    "temperature" : 45.6,
    "rpm" : 1498,
    "power" : 5.6,
    "vibration" : 1.1,
    "status" :"Running"
}

json_data = json.dumps(machine_data)

client = mqtt.Client()

client.connect(BROKER, PORT)

client.publish(TOPIC,json_data)
print("Message sent successfully")


client.disconnect()
