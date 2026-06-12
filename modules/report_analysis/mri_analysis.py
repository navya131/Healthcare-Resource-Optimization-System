import streamlit as st

from modules.report_analysis.downloads import show_analysis_pdf_download


def analyze_mri(report_text):

    findings = []

    risk = "Low"

    text = report_text.lower()

    if "tumor" in text:

        findings.append(
            "Possible Tumor Detected"
        )

        risk = "High"

    if "lesion" in text:

        findings.append(
            "Lesion Found"
        )

        risk = "High"

    if "abnormality" in text:

        findings.append(
            "MRI Abnormality Found"
        )

        risk = "Medium"

    return risk, findings


def mri_page():

    st.subheader(
        "🧠 MRI Analysis"
    )

    report_text = st.text_area(
        "Paste MRI Report"
    )

    if st.button(
        "Analyze MRI"
    ):

        risk, findings = analyze_mri(
            report_text
        )

        st.metric(
            "Risk Level",
            risk
        )

        for item in findings:
            st.warning(item)

        show_analysis_pdf_download(
            "MRI",
            report_text,
            risk,
            findings
        )
