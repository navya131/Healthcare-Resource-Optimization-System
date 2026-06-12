import pandas as pd

from config.database import get_connection


def get_bed_occupancy_report():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT
                ward_type,
                status,
                COUNT(*) AS total_beds
            FROM beds
            GROUP BY ward_type, status
            """,
            conn
        )

    except Exception:

        df = pd.DataFrame()

    conn.close()

    return df