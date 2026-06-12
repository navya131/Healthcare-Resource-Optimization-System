import streamlit as st
import pandas as pd

from config.database import get_connection


def view_patient_history():

    st.subheader("📋 Patient History")

    conn = get_connection()

    query = """
    SELECT *
    FROM patients
    WHERE user_id=?
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(st.session_state.user_id,)
    )

    conn.close()

    if not df.empty:
        st.dataframe(
            df,
            use_container_width=True
        )
    else:
        st.warning(
            "No patient record found."
        )