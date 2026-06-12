import streamlit as st

from config.database import get_connection


def ward_allocation_page():

    st.subheader("🏥 Ward Allocation")

    ward_type = st.selectbox(
        "Ward Type",
        [
            "General",
            "ICU",
            "Emergency"
        ]
    )

    bed_number = st.text_input(
        "Bed Number"
    )

    if st.button(
        "Add Bed"
    ):

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO beds(
                ward_type,
                bed_number
            )
            VALUES(?,?)
            """,
            (
                ward_type,
                bed_number
            )
        )

        conn.commit()
        conn.close()

        st.success(
            "Bed Added Successfully"
        )