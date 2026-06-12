import streamlit as st

from modules.report_analysis.downloads import show_analysis_pdf_download


def analyze_ecg(report_text):

    findings = []

    risk = "Low"

    text = report_text.lower()

    if "arrhythmia" in text:

        findings.append(
            "Abnormal Heart Rhythm"
        )

        risk = "High"

    if "tachycardia" in text:

        findings.append(
            "High Heart Rate"
        )

        risk = "High"

    if "bradycardia" in text:

        findings.append(
            "Low Heart Rate"
        )

        risk = "Medium"

    return risk, findings


def ecg_page():

    st.subheader(
        "❤️ ECG Analysis"
    )

    report_text = st.text_area(
        "Paste ECG Report"
    )

    if st.button(
        "Analyze ECG"
    ):

        risk, findings = analyze_ecg(
            report_text
        )

        st.metric(
            "Risk Level",
            risk
        )

        for item in findings:
            st.warning(item)

        show_analysis_pdf_download(
            "ECG",
            report_text,
            risk,
            findings
        )
