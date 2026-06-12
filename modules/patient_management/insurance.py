import streamlit as st

from config.database import get_connection


def insurance_section():

    st.subheader("🏥 Insurance Information")

    provider = st.text_input(
        "Insurance Provider"
    )

    policy_number = st.text_input(
        "Policy Number"
    )

    if st.button("Save Insurance"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE patients
            SET insurance_provider=?,
                insurance_number=?
            WHERE user_id=?
            """,
            (
                provider,
                policy_number,
                st.session_state.user_id
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Insurance details saved."
        )