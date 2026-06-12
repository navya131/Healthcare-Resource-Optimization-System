import pandas as pd
import streamlit as st

from config.database import get_connection


def doctor_dashboard_page():
    st.header("Doctor Dashboard")

    conn = get_connection()

    appointments = pd.read_sql_query(
        """
        SELECT
            a.appointment_id,
            a.appointment_date,
            a.appointment_time,
            a.status,
            a.reason,
            COALESCE(a.cancellation_reason, '') AS cancellation_reason,
            u.full_name AS patient_name
        FROM appointments a
        LEFT JOIN users u ON a.patient_user_id = u.id
        LEFT JOIN doctors d ON a.doctor_id = d.doctor_id
        WHERE d.user_id = ?
        ORDER BY a.appointment_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    records = pd.read_sql_query(
        """
        SELECT
            record_id,
            diagnosis,
            visit_date,
            treatment,
            doctor_notes
        FROM medical_records
        ORDER BY record_id DESC
        """,
        conn
    )

    conn.close()

    c1, c2 = st.columns(2)
    c1.metric("Scheduled Patients", len(appointments))
    c2.metric("Recent Records", len(records))

    tab1, tab2 = st.tabs(["Appointments", "Recent Records"])

    with tab1:
        st.dataframe(appointments, use_container_width=True)

    with tab2:
        st.dataframe(records.head(20), use_container_width=True)
