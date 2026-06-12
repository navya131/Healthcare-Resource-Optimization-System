import pandas as pd

from config.database import get_connection


def get_financial_report():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT
                user_id AS patient_user_id,
                insurance_provider,
                insurance_number AS policy_number
            FROM patients
            WHERE insurance_provider IS NOT NULL
               OR insurance_number IS NOT NULL
            """,
            conn
        )

    except Exception:

        df = pd.DataFrame(
            {
                "Revenue": [0],
                "Expenses": [0],
                "Profit": [0]
            }
        )

    conn.close()

    return df
