import pandas as pd
import streamlit as st

from config.database import get_connection


def manage_appointments():
    st.subheader("Appointment Requests")

    conn = get_connection()

    appointments = pd.read_sql_query(
        """
        SELECT
            a.appointment_id,
            u.full_name AS patient_name,
            u.email AS patient_email,
            a.appointment_date,
            a.appointment_time,
            a.reason,
            COALESCE(a.cancellation_reason, '') AS cancellation_reason,
            a.status
        FROM appointments a
        JOIN users u ON a.patient_user_id = u.id
        JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE d.user_id = ?
        ORDER BY a.appointment_date DESC, a.appointment_time DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    if appointments.empty:
        st.info("No appointment requests assigned to you yet.")
        conn.close()
        return

    c1, c2, c3 = st.columns(3)
    c1.metric("Total Requests", len(appointments))
    c2.metric("Pending", len(appointments[appointments["status"] == "Pending"]))
    c3.metric("Approved", len(appointments[appointments["status"] == "Approved"]))

    st.dataframe(appointments, use_container_width=True, hide_index=True)

    pending = appointments[appointments["status"] == "Pending"]
    if pending.empty:
        st.success("No pending appointments need action.")
        conn.close()
        return

    option_map = {
        f"#{row.appointment_id} - {row.patient_name} on {row.appointment_date} at {row.appointment_time}": row.appointment_id
        for row in pending.itertuples(index=False)
    }

    selected = st.selectbox("Select Pending Appointment", list(option_map.keys()))

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Approve Appointment"):
            conn.execute(
                """
                UPDATE appointments
                SET status = 'Approved'
                WHERE appointment_id = ?
                """,
                (option_map[selected],)
            )
            conn.commit()
            st.success("Appointment approved.")
            st.rerun()

    with col2:
        if st.button("Reject Appointment"):
            conn.execute(
                """
                UPDATE appointments
                SET status = 'Rejected'
                WHERE appointment_id = ?
                """,
                (option_map[selected],)
            )
            conn.commit()
            st.warning("Appointment rejected.")
            st.rerun()

    conn.close()
