import pandas as pd

from config.database import get_connection


def get_recovery_report():

    conn = get_connection()

    try:

        df = pd.read_sql_query(
            """
            SELECT
                patient_user_id,
                recovery_probability,
                icu_requirement,
                mortality_risk,
                expected_stay,
                prediction_date
            FROM outcome_predictions
            ORDER BY prediction_date DESC
            """,
            conn
        )

    except Exception:

        df = pd.DataFrame()

    conn.close()

    return df