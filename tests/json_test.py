import json

machine_data ={
    "machine_id" :"M001",
    "temperature" :"45.8",
    "rpm" :1500,
    "power" : 5.7,
    "status" : "Running"
}

print("Python Dictionary:")
print(machine_data)

json_data = json.dumps(machine_data)

print("\n JSON String:")
print(json_data)
print(type(json_data))
print(type(machine_data))