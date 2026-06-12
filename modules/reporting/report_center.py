import re
from io import BytesIO

import streamlit as st

from modules.reporting.appointment_report import get_appointment_report
from modules.reporting.bed_occupancy_report import get_bed_occupancy_report
from modules.reporting.disease_report import get_disease_report
from modules.reporting.excel_reports import generate_excel_report
from modules.reporting.financial_report import get_financial_report
from modules.reporting.pdf_reports import generate_pdf_report_bytes
from modules.reporting.performance_report import get_doctor_performance
from modules.reporting.recovery_report import get_recovery_report
from modules.reporting.resource_report import get_resource_report


REPORTS = {
    "Disease Statistics": get_disease_report,
    "Resource Utilization": get_resource_report,
    "Doctor Performance": get_doctor_performance,
    "Patient Recovery Report": get_recovery_report,
    "Bed Occupancy Report": get_bed_occupancy_report,
    "Appointment Report": get_appointment_report,
    "Financial Report": get_financial_report,
}


def _safe_filename(name, extension):
    base = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_").lower()
    return f"{base or 'report'}.{extension}"


def _excel_bytes(dataframe):
    buffer = BytesIO()
    dataframe.to_excel(buffer, index=False)
    buffer.seek(0)
    return buffer.getvalue()


def report_center_page():
    st.header("Healthcare Reporting Center")

    report_type = st.selectbox("Select Report", list(REPORTS.keys()))
    df = REPORTS[report_type]()

    c1, c2 = st.columns(2)
    c1.metric("Report Rows", len(df))
    c2.metric("Report Columns", len(df.columns))

    pdf_data = generate_pdf_report_bytes(report_type, df)
    excel_data = _excel_bytes(df)

    st.subheader("Download Report")

    col1, col2 = st.columns(2)

    with col1:
        st.download_button(
            "Download PDF",
            data=pdf_data,
            file_name=_safe_filename(report_type, "pdf"),
            mime="application/pdf",
        )

    with col2:
        st.download_button(
            "Download Excel",
            data=excel_data,
            file_name=_safe_filename(report_type, "xlsx"),
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        )

    st.divider()
    st.subheader("Report Preview")
    st.dataframe(df, use_container_width=True)

    if st.button("Save Excel Copy"):
        filename = _safe_filename(report_type, "xlsx")
        saved_path = generate_excel_report(df, filename)
        st.success(f"Excel copy saved to {saved_path}.")
