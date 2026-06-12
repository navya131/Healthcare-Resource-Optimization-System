import pandas as pd
import streamlit as st

from config.database import get_connection
from modules.notifications.reminder_engine import (
    send_appointment_reminder,
    send_medicine_reminder,
)


def _get_targets(role, user_id):
    conn = get_connection()

    if role == "Patient":
        targets = pd.read_sql_query(
            """
            SELECT id, full_name, role, email
            FROM users
            WHERE id = ?
            """,
            conn,
            params=(user_id,)
        )
    elif role == "Doctor":
        targets = pd.read_sql_query(
            """
            SELECT DISTINCT
                u.id,
                u.full_name,
                u.role,
                u.email
            FROM appointments a
            JOIN users u ON a.patient_user_id = u.id
            JOIN doctors d ON a.doctor_id = d.doctor_id
            WHERE d.user_id = ?
            ORDER BY u.full_name
            """,
            conn,
            params=(user_id,)
        )
    else:
        targets = pd.read_sql_query(
            """
            SELECT id, full_name, role, email
            FROM users
            ORDER BY role, full_name
            """,
            conn
        )

    conn.close()
    return targets


def _get_notification_history(role, user_id):
    conn = get_connection()

    if role == "Patient":
        history = pd.read_sql_query(
            """
            SELECT
                n.notification_id,
                n.channel,
                n.subject,
                n.message,
                n.status,
                n.sent_at
            FROM notifications n
            WHERE n.user_id = ?
            ORDER BY n.notification_id DESC
            """,
            conn,
            params=(user_id,)
        )
    else:
        history = pd.read_sql_query(
            """
            SELECT
                n.notification_id,
                u.full_name,
                u.role,
                n.channel,
                n.subject,
                n.message,
                n.status,
                n.sent_at
            FROM notifications n
            LEFT JOIN users u ON n.user_id = u.id
            ORDER BY n.notification_id DESC
            """,
            conn
        )

    conn.close()
    return history


def notification_dashboard_page():
    st.header("Notifications & Reminders")

    role = st.session_state.get("role") or st.session_state.get("user_role")
    user_id = st.session_state.get("user_id")

    targets = _get_targets(role, user_id)

    if targets.empty:
        st.info("No reminder recipients are available yet.")
    else:
        option_map = {
            f"{row.full_name} ({row.role})": row.id
            for row in targets.itertuples(index=False)
        }

        selected_target = st.selectbox(
            "Reminder Recipient",
            list(option_map.keys())
        )

        reminder_type = st.radio(
            "Reminder Type",
            ["Appointment Reminder", "Medicine Reminder"],
            horizontal=True
        )

        default_message = (
            "Reminder: You have an appointment scheduled."
            if reminder_type == "Appointment Reminder"
            else "Reminder: Please take your medication."
        )
        message = st.text_area("Reminder Message", value=default_message)

        if st.button("Send Reminder"):
            if not message.strip():
                st.error("Please enter a reminder message.")
            elif reminder_type == "Appointment Reminder":
                send_appointment_reminder(
                    option_map[selected_target],
                    message.strip()
                )
                st.success("Appointment reminder sent.")
                st.rerun()
            else:
                send_medicine_reminder(
                    option_map[selected_target],
                    message.strip()
                )
                st.success("Medicine reminder sent.")
                st.rerun()

    st.divider()
    st.subheader("Notification History")

    history = _get_notification_history(role, user_id)
    st.dataframe(history, use_container_width=True, hide_index=True)
