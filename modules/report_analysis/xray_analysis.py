import streamlit as st

from modules.report_analysis.downloads import show_analysis_pdf_download


def analyze_xray(report_text):

    findings = []

    risk = "Low"

    text = report_text.lower()

    if "fracture" in text:

        findings.append(
            "Bone Fracture Detected"
        )

        risk = "High"

    if "infection" in text:

        findings.append(
            "Possible Infection"
        )

        risk = "Medium"

    if "pneumonia" in text:

        findings.append(
            "Pneumonia Indicator"
        )

        risk = "High"

    return risk, findings


def xray_page():

    st.subheader(
        "🦴 X-Ray Analysis"
    )

    report_text = st.text_area(
        "Paste X-Ray Report"
    )

    if st.button(
        "Analyze X-Ray"
    ):

        risk, findings = analyze_xray(
            report_text
        )

        st.metric(
            "Risk Level",
            risk
        )

        for item in findings:
            st.warning(item)

        show_analysis_pdf_download(
            "X-Ray",
            report_text,
            risk,
            findings
        )
