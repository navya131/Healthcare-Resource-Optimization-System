import streamlit as st
import pandas as pd
import os

from config.database import get_connection


UPLOAD_DIR = "uploads"

os.makedirs(
    UPLOAD_DIR,
    exist_ok=True
)


def diagnostics_page():

    st.subheader("🧪 Diagnostic Reports")

    report_name = st.text_input(
        "Report Name"
    )

    report_type = st.selectbox(
        "Report Type",
        [
            "Blood Test",
            "ECG",
            "MRI",
            "CT Scan",
            "X-Ray",
            "Other"
        ]
    )

    uploaded_file = st.file_uploader(
        "Upload Report"
    )

    if st.button("Save Report"):

        if uploaded_file:

            file_path = os.path.join(
                UPLOAD_DIR,
                uploaded_file.name
            )

            with open(
                file_path,
                "wb"
            ) as f:

                f.write(
                    uploaded_file.getbuffer()
                )

            conn = get_connection()

            conn.execute(
                """
                INSERT INTO diagnostics(
                    patient_user_id,
                    report_name,
                    report_type,
                    report_file,
                    upload_date
                )
                VALUES(?,?,?,?,DATE('now'))
                """,
                (
                    st.session_state.user_id,
                    report_name,
                    report_type,
                    file_path
                )
            )

            conn.commit()
            conn.close()

            st.success(
                "Report Uploaded"
            )

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM diagnostics
        WHERE patient_user_id=?
        ORDER BY diagnostic_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )
