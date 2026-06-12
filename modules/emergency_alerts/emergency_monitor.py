import streamlit as st

from modules.emergency_alerts.alert_engine import (
    create_alert
)


def emergency_monitor_page():

    st.header(
        "🚨 Emergency Monitoring"
    )

    oxygen = st.number_input(
        "Oxygen Saturation %",
        0,
        100,
        98
    )

    heart_rate = st.number_input(
        "Heart Rate",
        30,
        250,
        75
    )

    systolic_bp = st.number_input(
        "Systolic BP",
        50,
        250,
        120
    )

    if st.button(
        "Analyze Patient"
    ):

        if oxygen < 90:

            create_alert(
                st.session_state.user_id,
                "Oxygen Alert",
                "Critical",
                "Oxygen level below threshold"
            )

            st.error(
                "Critical Oxygen Alert"
            )

        if heart_rate > 140:

            create_alert(
                st.session_state.user_id,
                "Heart Rate Alert",
                "Critical",
                "Heart rate dangerously high"
            )

            st.error(
                "Heart Rate Emergency"
            )

        if systolic_bp > 180:

            create_alert(
                st.session_state.user_id,
                "Blood Pressure Alert",
                "High",
                "High blood pressure detected"
            )

            st.warning(
                "Blood Pressure Alert"
            )

        if (
            oxygen >= 90 and
            heart_rate <= 140 and
            systolic_bp <= 180
        ):
            st.success(
                "No Emergency Detected"
            )