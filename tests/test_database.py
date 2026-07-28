from database.db_connection import get_connection

connection = get_connection()

if connection:
    print("Database connection successfull!")
    connection.close()
