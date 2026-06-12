import streamlit as st
from config.database import get_connection


def equipment_page():

    st.subheader("⚕ Medical Equipment")

    equipment_name = st.text_input(
        "Equipment Name"
    )

    quantity = st.number_input(
        "Quantity",
        min_value=0
    )

    available = st.number_input(
        "Available Quantity",
        min_value=0
    )

    if st.button("Save Equipment"):

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
                equipment_name,
                "Equipment",
                quantity,
                available
            )
        )

        conn.commit()
        conn.close()

        st.success("Equipment Saved")