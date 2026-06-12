import streamlit as st

from config.database import get_connection


def _get_existing_profile(user_id):
    conn = get_connection()
    profile = conn.execute(
        """
        SELECT
            specialization,
            department,
            experience,
            qualification,
            consultation_fee,
            bio
        FROM doctors
        WHERE user_id = ?
        """,
        (user_id,)
    ).fetchone()
    conn.close()
    return profile


def doctor_profile():
    st.subheader("Doctor Profile")

    existing = _get_existing_profile(st.session_state.user_id)

    specialization = st.text_input(
        "Specialization",
        value=existing["specialization"] if existing and existing["specialization"] else ""
    )

    department = st.text_input(
        "Department",
        value=existing["department"] if existing and existing["department"] else ""
    )

    experience = st.number_input(
        "Experience (Years)",
        min_value=0,
        value=int(existing["experience"] or 0) if existing else 0
    )

    qualification = st.text_input(
        "Qualification",
        value=existing["qualification"] if existing and existing["qualification"] else ""
    )

    consultation_fee = st.number_input(
        "Consultation Fee",
        min_value=0.0,
        value=float(existing["consultation_fee"] or 0.0) if existing else 0.0
    )

    bio = st.text_area(
        "Professional Bio",
        value=existing["bio"] if existing and existing["bio"] else ""
    )

    if st.button("Save Doctor Profile"):
        if not specialization.strip() or not department.strip():
            st.error("Department and specialization are required.")
            return

        conn = get_connection()
        conn.execute(
            """
            INSERT INTO doctors(
                user_id,
                specialization,
                department,
                experience,
                qualification,
                consultation_fee,
                bio
            )
            VALUES(?,?,?,?,?,?,?)
            ON CONFLICT(user_id) DO UPDATE SET
                specialization = excluded.specialization,
                department = excluded.department,
                experience = excluded.experience,
                qualification = excluded.qualification,
                consultation_fee = excluded.consultation_fee,
                bio = excluded.bio
            """,
            (
                st.session_state.user_id,
                specialization.strip(),
                department.strip(),
                experience,
                qualification.strip(),
                consultation_fee,
                bio.strip()
            )
        )
        conn.commit()
        conn.close()

        st.success("Doctor profile saved.")
