import streamlit as st

from config.database import get_connection


def patient_registration():

    st.subheader("🧑 Patient Profile")

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=120
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female", "Other"]
    )

    weight = st.number_input(
        "Weight (kg)",
        min_value=0.0
    )

    height = st.number_input(
        "Height (cm)",
        min_value=0.0
    )

    blood_group = st.selectbox(
        "Blood Group",
        [
            "A+","A-","B+","B-",
            "AB+","AB-","O+","O-"
        ]
    )

    medical_conditions = st.text_area(
        "Medical Conditions"
    )

    family_history = st.text_area(
        "Family History"
    )

    if st.button("Save Profile"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO patients
            (
                user_id,
                age,
                gender,
                weight,
                height,
                blood_group,
                medical_conditions,
                family_history
            )
            VALUES(?,?,?,?,?,?,?,?)
            """,
            (
                st.session_state.user_id,
                age,
                gender,
                weight,
                height,
                blood_group,
                medical_conditions,
                family_history
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Patient profile saved successfully."
        )