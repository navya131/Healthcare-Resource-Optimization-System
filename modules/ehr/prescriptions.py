import streamlit as st
import pandas as pd

from config.database import get_connection


def prescriptions_page():

    st.subheader("💊 Prescriptions")

    medication = st.text_input(
        "Medication"
    )

    dosage = st.text_input(
        "Dosage"
    )

    duration = st.text_input(
        "Duration"
    )

    instructions = st.text_area(
        "Instructions"
    )

    if st.button("Save Prescription"):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO prescriptions(
                patient_user_id,
                medication,
                dosage,
                duration,
                instructions,
                prescribed_date
            )
            VALUES(?,?,?,?,?,DATE('now'))
            """,
            (
                st.session_state.user_id,
                medication,
                dosage,
                duration,
                instructions
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Prescription Saved"
        )

    conn = get_connection()

    df = pd.read_sql_query(
        """
        SELECT *
        FROM prescriptions
        WHERE patient_user_id=?
        ORDER BY prescription_id DESC
        """,
        conn,
        params=(st.session_state.user_id,)
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )