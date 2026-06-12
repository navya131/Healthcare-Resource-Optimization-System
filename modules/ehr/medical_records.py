import streamlit as st
import pandas as pd

from config.database import get_connection


def medical_records_page():

    st.subheader("🏥 Medical Records")

    diagnosis = st.text_input("Diagnosis")

    symptoms = st.text_area("Symptoms")

    treatment = st.text_area("Treatment")

    doctor_notes = st.text_area("Doctor Notes")

    visit_date = st.date_input("Visit Date")

    if st.button("Save Medical Record"):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO medical_records(
                patient_user_id,
                diagnosis,
                symptoms,
                treatment,
                doctor_notes,
                visit_date
            )
            VALUES(?,?,?,?,?,?)
            """,
            (
                st.session_state.user_id,
                diagnosis,
                symptoms,
                treatment,
                doctor_notes,
                str(visit_date)
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Medical Record Saved"
        )

    st.divider()

    conn = get_connection()

    query = """
    SELECT *
    FROM medical_records
    WHERE patient_user_id=?
    ORDER BY record_id DESC
    """

    df = pd.read_sql_query(
        query,
        conn,
        params=(st.session_state.user_id,)
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )