import mysql.connector
from database.db_config import HOST,USER,PASSWORD,DATABASE

def get_connection():
    try:
        connection = mysql.connector.connect(
            host = HOST,
            user = USER,
            password = PASSWORD,
            database = DATABASE
        )

        if connection.is_connected():
            print("Connected to MYSQL Database")

        return connection
    
    except mysql.connector.Error as err:
        print(f"Database Error: {err}")
        return None
