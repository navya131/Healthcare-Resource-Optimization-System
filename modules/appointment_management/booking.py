import pandas as pd
import streamlit as st

from config.database import get_connection


def _ensure_registered_doctors(conn):
    conn.execute(
        """
        INSERT INTO doctors(user_id, specialization, department)
        SELECT id, 'General Medicine', 'General'
        FROM users
        WHERE role = 'Doctor'
        AND id NOT IN (
            SELECT user_id
            FROM doctors
            WHERE user_id IS NOT NULL
        )
        """
    )
    conn.commit()


def book_appointment():
    st.subheader("Book Appointment")

    conn = get_connection()
    _ensure_registered_doctors(conn)

    doctors = pd.read_sql_query(
        """
        SELECT
            d.doctor_id,
            u.full_name,
            u.email,
            COALESCE(d.specialization, 'General Medicine') AS specialization,
            COALESCE(d.department, 'General') AS department,
            COALESCE(d.experience, 0) AS experience,
            COALESCE(d.consultation_fee, 0) AS consultation_fee
        FROM users u
        JOIN doctors d ON d.user_id = u.id
        WHERE u.role = 'Doctor'
        ORDER BY u.full_name
        """,
        conn
    )

    if doctors.empty:
        st.warning("No registered doctors are available yet.")
        conn.close()
        return

    st.write("Available Doctors")
    st.dataframe(
        doctors[
            [
                "full_name",
                "specialization",
                "department",
                "experience",
                "consultation_fee",
                "email"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )

    doctor_options = {
        f"{row.full_name} | {row.specialization} | {row.department}": row.doctor_id
        for row in doctors.itertuples(index=False)
    }

    selected_doctor = st.selectbox(
        "Select Doctor",
        list(doctor_options.keys())
    )

    appointment_date = st.date_input("Appointment Date")
    appointment_time = st.time_input("Appointment Time")
    reason = st.text_area("Reason for Visit")

    if st.button("Book Appointment"):
        if not reason.strip():
            st.error("Please enter the reason for the visit.")
        else:
            conn.execute(
                """
                INSERT INTO appointments(
                    patient_user_id,
                    doctor_id,
                    appointment_date,
                    appointment_time,
                    reason
                )
                VALUES(?,?,?,?,?)
                """,
                (
                    st.session_state.user_id,
                    doctor_options[selected_doctor],
                    str(appointment_date),
                    str(appointment_time),
                    reason.strip()
                )
            )
            conn.commit()
            st.success("Appointment request submitted to the selected doctor.")

    conn.close()
