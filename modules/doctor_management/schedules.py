import streamlit as st

from config.database import get_connection


def doctor_schedule():

    st.subheader("📅 Availability Schedule")

    available_date = st.date_input(
        "Available Date"
    )

    start_time = st.time_input(
        "Start Time"
    )

    end_time = st.time_input(
        "End Time"
    )

    max_patients = st.number_input(
        "Maximum Patients",
        min_value=1,
        value=10
    )

    if st.button("Add Schedule"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT doctor_id
            FROM doctors
            WHERE user_id=?
            """,
            (st.session_state.user_id,)
        )

        doctor = cursor.fetchone()

        if doctor:

            cursor.execute(
                """
                INSERT INTO doctor_schedules(
                    doctor_id,
                    available_date,
                    start_time,
                    end_time,
                    max_patients
                )
                VALUES(?,?,?,?,?)
                """,
                (
                    doctor["doctor_id"],
                    str(available_date),
                    str(start_time),
                    str(end_time),
                    max_patients
                )
            )

            conn.commit()

            st.success(
                "Schedule Added Successfully"
            )

        conn.close()