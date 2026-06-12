import pandas as pd

from config.database import get_connection


def get_resource_report():

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM resources
        """,
        conn
    )

    conn.close()

    return df