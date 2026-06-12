import streamlit as st
import pandas as pd

from config.database import get_connection


def vaccinations_page():

    st.subheader("💉 Vaccination Records")

    vaccine_name = st.text_input(
        "Vaccine Name"
    )

    dose_number = st.text_input(
        "Dose Number"
    )

    vaccination_date = st.date_input(
        "Vaccination Date"
    )

    next_due_date = st.date_input(
        "Next Due Date"
    )

    if st.button("Save Vaccination"):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO vaccinations(
                patient_user_id,
                vaccine_name,
                dose_number,
                vaccination_date,
                next_due_date
            )
            VALUES(?,?,?,?,?)
            """,
            (
                st.session_state.user_id,
                vaccine_name,
                dose_number,
                str(vaccination_date),
                str(next_due_date)
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Vaccination Record Saved"
        )

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM vaccinations
        WHERE patient_user_id=?
        ORDER BY vaccine_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )
