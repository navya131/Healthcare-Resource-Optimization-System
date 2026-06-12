import streamlit as st

from config.database import get_connection
from config.auth_config import hash_password


def register_page():

    st.subheader("📝 User Registration")

    full_name = st.text_input("Full Name")

    email = st.text_input("Email")

    phone = st.text_input("Phone Number")

    password = st.text_input(
        "Password",
        type="password"
    )

    role = st.selectbox(
        "Select Role",
        ["Patient", "Doctor", "Admin"]
    )

    if st.button("Register"):

        if not all([full_name, email, password]):
            st.error("Please fill all required fields.")
            return

        conn = get_connection()
        cursor = conn.cursor()

        try:

            hashed_password = hash_password(password)

            cursor.execute(
                """
                INSERT INTO users
                (full_name,email,password,role,phone)
                VALUES (?,?,?,?,?)
                """,
                (
                    full_name,
                    email,
                    hashed_password,
                    role,
                    phone
                )
            )

            user_id = cursor.lastrowid

            if role == "Doctor":
                cursor.execute(
                    """
                    INSERT INTO doctors(user_id, specialization, department)
                    VALUES (?, 'General Medicine', 'General')
                    """,
                    (user_id,)
                )

            conn.commit()

            st.success(
                "Registration Successful!"
            )

        except Exception as e:

            st.error(
                f"User already exists or error: {e}"
            )

        finally:
            conn.close()
