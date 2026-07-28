from database.insert_data import insert_machine_data

sample_data = {
    "machine_id": "M001",
    "temperature": 45.6,
    "rpm": 1498,
    "power": 5.6,
    "vibration": 1.1,
    "status": "Running"
}

insert_machine_data(sample_data)