import pandas as pd
import streamlit as st

from config.database import get_connection
from modules.staff_management.workload_prediction import predict_workload


def staff_dashboard_page():
    st.header("Staff Management Dashboard")

    workload = predict_workload()

    c1, c2 = st.columns(2)
    c1.metric("Expected Patients", workload["expected_patients"])
    c2.metric("Required Staff", workload["required_staff"])

    conn = get_connection()
    staff_df = pd.read_sql_query("SELECT * FROM staff", conn)
    shifts_df = pd.read_sql_query("SELECT * FROM staff_shifts", conn)
    conn.close()

    tab1, tab2 = st.tabs(["Staff Directory", "Shifts"])

    with tab1:
        st.dataframe(staff_df, use_container_width=True)

    with tab2:
        st.dataframe(shifts_df, use_container_width=True)
