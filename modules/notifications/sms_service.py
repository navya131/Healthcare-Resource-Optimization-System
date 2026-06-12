from config.database import get_connection


def send_sms(
    user_id,
    message
):

    conn = get_connection()

    conn.execute(
        """
        INSERT INTO notifications(
            user_id,
            channel,
            subject,
            message,
            status
        )
        VALUES(?,?,?,?,?)
        """,
        (
            user_id,
            "SMS",
            "SMS Notification",
            message,
            "Sent"
        )
    )

    conn.commit()
    conn.close()

    return True