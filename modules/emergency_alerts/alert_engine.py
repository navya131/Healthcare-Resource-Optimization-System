from config.database import get_connection


def create_alert(
    patient_id,
    alert_type,
    severity,
    message
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO emergency_alerts(
            patient_user_id,
            alert_type,
            severity,
            message
        )
        VALUES(?,?,?,?)
        """,
        (
            patient_id,
            alert_type,
            severity,
            message
        )
    )

    conn.commit()
    conn.close()