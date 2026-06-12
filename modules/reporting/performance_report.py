import pandas as pd

from config.database import get_connection


def get_doctor_performance():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM doctors
            """,
            conn
        )

    except:

        df = pd.DataFrame()

    conn.close()

    return df