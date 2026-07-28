from database.db_connection import get_connection


def insert_machine_data(data):
    connection = get_connection()

    if connection is None:
        return

    cursor = connection.cursor()

    query = """
    INSERT INTO machine_data
    (machine_id, temperature, rpm, power, vibration, status)
    VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (
        data["machine_id"],
        data["temperature"],
        data["rpm"],
        data["power"],
        data["vibration"],
        data["status"]
    )

    cursor.execute(query, values)
    connection.commit()

    print("Data inserted successfully.")

    cursor.close()
    connection.close()