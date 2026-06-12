import streamlit as st
from config.database import get_connection


def ventilator_page():

    st.subheader("🫁 Ventilator Management")

    quantity = st.number_input(
        "Number of Ventilators",
        min_value=0
    )

    available = st.number_input(
        "Available Ventilators",
        min_value=0
    )

    if st.button("Save Ventilator Data"):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO resources(
                resource_name,
                resource_type,
                quantity,
                available_quantity
            )
            VALUES(?,?,?,?)
            """,
            (
                "Ventilator",
                "Ventilator",
                quantity,
                available
            )
        )

        conn.commit()
        conn.close()

        st.success("Ventilator Data Saved")