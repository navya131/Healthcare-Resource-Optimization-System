import streamlit as st
import pandas as pd

from config.database import get_connection


def bed_tracker_page():

    st.subheader("🛏 Bed Tracker")

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM beds",
        conn
    )

    conn.close()

    if df.empty:
        st.warning("No beds configured.")
    else:
        st.dataframe(
            df,
            use_container_width=True
        )