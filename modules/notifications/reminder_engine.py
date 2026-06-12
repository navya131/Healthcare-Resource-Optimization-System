from modules.notifications.email_service import (
    send_email
)

from modules.notifications.sms_service import (
    send_sms
)

from modules.notifications.whatsapp_service import (
    send_whatsapp
)


def send_appointment_reminder(
    user_id,
    message=None
):

    if message is None:
        message = "Reminder: You have an appointment scheduled."

    send_email(
        user_id,
        "Appointment Reminder",
        message
    )

    send_sms(
        user_id,
        message
    )

    send_whatsapp(
        user_id,
        message
    )


def send_medicine_reminder(
    user_id,
    message=None
):

    if message is None:
        message = "Reminder: Please take your medication."

    send_email(
        user_id,
        "Medicine Reminder",
        message
    )

    send_sms(
        user_id,
        message
    )

    send_whatsapp(
        user_id,
        message
    )
