import streamlit as st
import pandas as pd

from config.database import get_connection


def alert_dashboard_page():

    st.header(
        "🚨 Emergency Alerts Dashboard"
    )

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM emergency_alerts
        ORDER BY alert_id DESC
        """,
        conn
    )

    conn.close()

    if df.empty:

        st.success(
            "No Active Alerts"
        )

    else:

        st.dataframe(
            df,
            use_container_width=True
        )