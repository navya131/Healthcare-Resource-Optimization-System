import pandas as pd
import streamlit as st

from modules.reporting.pdf_reports import generate_pdf_report_bytes


def show_analysis_pdf_download(report_type, report_text, risk, findings):
    findings_text = ", ".join(findings) if findings else "No abnormal findings detected."
    report_df = pd.DataFrame(
        [
            {
                "Report Type": report_type,
                "Risk Level": risk,
                "Findings": findings_text,
                "Input Report": report_text,
            }
        ]
    )

    pdf_data = generate_pdf_report_bytes(f"{report_type} Analysis Report", report_df)

    st.download_button(
        "Download PDF Report",
        data=pdf_data,
        file_name=f"{report_type.lower().replace(' ', '_')}_analysis_report.pdf",
        mime="application/pdf",
    )
