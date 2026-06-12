import pandas as pd

from config.database import get_connection


def get_appointment_report():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT
                appointment_date,
                COUNT(*) AS total_appointments
            FROM appointments
            GROUP BY appointment_date
            ORDER BY appointment_date DESC
            """,
            conn
        )

    except Exception:

        df = pd.DataFrame()

    conn.close()

    return df