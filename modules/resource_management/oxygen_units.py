import streamlit as st
from config.database import get_connection


def oxygen_units_page():

    st.subheader("🧪 Oxygen Unit Management")

    quantity = st.number_input(
        "Total Oxygen Units",
        min_value=0
    )

    available = st.number_input(
        "Available Oxygen Units",
        min_value=0
    )

    if st.button("Save Oxygen Data"):

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
                "Oxygen Unit",
                "Oxygen",
                quantity,
                available
            )
        )

        conn.commit()
        conn.close()

        st.success("Oxygen Data Saved")