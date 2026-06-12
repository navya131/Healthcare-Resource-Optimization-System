import streamlit as st
import pandas as pd

from config.database import get_connection

from modules.resource_management.forecasting import (
    resource_forecast
)


def resource_dashboard_page():

    st.header(
        "📊 Resource Allocation Dashboard"
    )

    forecast = resource_forecast()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Ventilator Demand",
            forecast["Ventilator"]
        )

    with col2:
        st.metric(
            "Oxygen Demand",
            forecast["Oxygen"]
        )

    with col3:
        st.metric(
            "Equipment Demand",
            forecast["Equipment"]
        )

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM resources",
        conn
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )