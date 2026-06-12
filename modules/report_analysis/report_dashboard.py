import streamlit as st

from modules.report_analysis.blood_test_analysis import (
    blood_test_page
)

from modules.report_analysis.ecg_analysis import (
    ecg_page
)

from modules.report_analysis.xray_analysis import (
    xray_page
)

from modules.report_analysis.mri_analysis import (
    mri_page
)


def report_dashboard_page():

    st.header(
        "📋 Medical Report Analysis"
    )

    report_type = st.selectbox(
        "Select Report Type",
        [
            "Blood Test",
            "ECG",
            "X-Ray",
            "MRI"
        ]
    )

    if report_type == "Blood Test":
        blood_test_page()

    elif report_type == "ECG":
        ecg_page()

    elif report_type == "X-Ray":
        xray_page()

    elif report_type == "MRI":
        mri_page()