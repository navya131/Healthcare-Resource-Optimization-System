from config.database import get_connection


def send_email(
    user_id,
    subject,
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
            "Email",
            subject,
            message,
            "Sent"
        )
    )

    conn.commit()
    conn.close()

    return True