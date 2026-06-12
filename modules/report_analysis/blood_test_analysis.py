import streamlit as st

from modules.report_analysis.downloads import show_analysis_pdf_download


def analyze_blood_test(report_text):

    findings = []

    risk = "Low"

    text = report_text.lower()

    if "glucose" in text:
        findings.append(
            "Possible Diabetes Indicator"
        )
        risk = "Medium"

    if "cholesterol" in text:
        findings.append(
            "High Cholesterol Detected"
        )
        risk = "Medium"

    if "hemoglobin" in text:
        findings.append(
            "Hemoglobin Value Found"
        )

    return risk, findings


def blood_test_page():

    st.subheader(
        "🩸 Blood Test Analysis"
    )

    report_text = st.text_area(
        "Paste Blood Test Report"
    )

    if st.button(
        "Analyze Blood Report"
    ):

        risk, findings = analyze_blood_test(
            report_text
        )

        st.metric(
            "Risk Level",
            risk
        )

        for item in findings:
            st.warning(item)

        show_analysis_pdf_download(
            "Blood Test",
            report_text,
            risk,
            findings
        )
