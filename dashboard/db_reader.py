import pandas as pd
import database.db_connection import get_connection

def get_latest_data():
    connection = get_connection()


    if connection is None:
        return pd.DataFrame()

    query = """
    SELECT *
    FROM machine_data
    ORDER BY timestamp DESC
    LIMIT 20;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df