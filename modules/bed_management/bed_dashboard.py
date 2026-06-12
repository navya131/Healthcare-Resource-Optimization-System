import streamlit as st
import pandas as pd

from config.database import get_connection

from modules.bed_management.bed_forecasting import (
    predict_bed_requirement
)


def bed_dashboard_page():

    st.header(
        "📊 Bed Management Dashboard"
    )

    conn = get_connection()

    beds = pd.read_sql_query(
        "SELECT * FROM beds",
        conn
    )

    conn.close()

    total_beds = len(beds)

    occupied = len(
        beds[
            beds["status"] == "Occupied"
        ]
    ) if not beds.empty else 0

    available = len(
        beds[
            beds["status"] == "Available"
        ]
    ) if not beds.empty else 0

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Total Beds",
            total_beds
        )

    with col2:
        st.metric(
            "Available Beds",
            available
        )

    with col3:
        st.metric(
            "Occupied Beds",
            occupied
        )

    st.divider()

    forecast = predict_bed_requirement()

    st.metric(
        "Predicted Future Bed Need",
        forecast
    )

    st.dataframe(
        beds,
        use_container_width=True
    )