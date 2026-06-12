import streamlit as st

from config.database import get_connection


def allergies_section():

    st.subheader("🚨 Allergies")

    allergies = st.text_area(
        "Enter allergy information"
    )

    if st.button("Save Allergies"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            UPDATE patients
            SET allergies=?
            WHERE user_id=?
            """,
            (
                allergies,
                st.session_state.user_id
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Allergy information updated."
        )