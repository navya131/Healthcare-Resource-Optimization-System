import streamlit as st
import pandas as pd

from config.database import get_connection


def nurse_allocation_page():

    st.subheader("👩‍⚕️ Nurse Allocation")

    conn = get_connection()

    nurses = pd.read_sql_query(
        """
        SELECT *
        FROM staff
        WHERE role='Nurse'
        """,
        conn
    )

    conn.close()

    st.dataframe(
        nurses,
        use_container_width=True
    )