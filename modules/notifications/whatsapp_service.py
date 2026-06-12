from config.database import get_connection


def send_whatsapp(
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
            "WhatsApp",
            "WhatsApp Notification",
            message,
            "Sent"
        )
    )

    conn.commit()
    conn.close()

    return True