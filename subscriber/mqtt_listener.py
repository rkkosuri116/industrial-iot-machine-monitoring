import paho.mqtt.client as mqtt
import json\

BROKER = "localhost"
PORT = 1883
TOPIC = "factory/test"

def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT Broker!")
    print(f"Subscribed to topic: {TOPIC}")
    print("Waiting for messages...")
    client.subscribe(TOPIC)


def on_message(client, userdata, msg):
    print(f"Topic: {msg.topic}")
    data = json.loads(msg.payload.decode())
    print("\n -------Machine Data---------")

    print(f"Machine ID : {data['machine_id']}")
    print(f"Temperature: {data['temperature']} °C")
    print(f"RPM        : {data['rpm']}")
    print(f"Power      : {data['power']} kW")
    print(f"Vibration  : {data['vibration']} mm/s")
    print(f"Status     : {data['status']}")

    print("-------------------------")

client = mqtt.Client()

client.on_connect = on_connect
client.on_message = on_message

client.connect(BROKER,PORT)
print("Starting MQTT listener...")
client.loop_forever()
