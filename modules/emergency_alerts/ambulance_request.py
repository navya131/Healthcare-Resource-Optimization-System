import streamlit as st


def ambulance_request_page():

    st.header(
        "🚑 Ambulance Request"
    )

    location = st.text_area(
        "Current Location"
    )

    emergency_type = st.selectbox(
        "Emergency Type",
        [
            "Cardiac",
            "Accident",
            "Respiratory",
            "General"
        ]
    )

    if st.button(
        "Request Ambulance"
    ):

        st.success(
            "Ambulance Request Sent"
        )

        st.info(
            f"Location: {location}"
        )