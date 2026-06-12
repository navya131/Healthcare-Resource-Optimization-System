import streamlit as st
import pandas as pd

from config.database import get_connection


def shift_scheduler_page():

    st.subheader("🗓 Staff Shift Scheduler")

    staff_name = st.text_input(
        "Staff Name"
    )

    role = st.selectbox(
        "Role",
        [
            "Doctor",
            "Nurse",
            "Receptionist",
            "Technician"
        ]
    )

    department = st.text_input(
        "Department"
    )

    if st.button("Add Staff"):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO staff(
                name,
                role,
                department
            )
            VALUES(?,?,?)
            """,
            (
                staff_name,
                role,
                department
            )
        )

        conn.commit()
        conn.close()

        st.success("Staff Added")

    st.divider()

    conn = get_connection()

    df = pd.read_sql_query(
        "SELECT * FROM staff",
        conn
    )

    conn.close()

    st.dataframe(
        df,
        use_container_width=True
    )