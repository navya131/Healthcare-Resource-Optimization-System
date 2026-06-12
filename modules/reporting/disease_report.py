import pandas as pd

from config.database import get_connection


def get_disease_report():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT *
            FROM disease_predictions
            """,
            conn
        )

    except:

        df = pd.DataFrame()

    conn.close()

    return df