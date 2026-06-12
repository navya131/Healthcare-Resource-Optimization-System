import streamlit as st
import pandas as pd

from config.database import get_connection


def my_appointments():

    st.subheader("📖 My Appointments")

    conn = get_connection()

    query = """
    SELECT
        a.appointment_date,
        a.appointment_time,
        a.status,
        u.full_name AS doctor_name
    FROM appointments a
    JOIN doctors d
    ON a.doctor_id=d.doctor_id
    JOIN users u
    ON d.user_id=u.id
    WHERE a.patient_user_id=?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(st.session_state.user_id,)
    )

    st.dataframe(
        df,
        use_container_width=True
    )

    conn.close()