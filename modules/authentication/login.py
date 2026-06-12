import streamlit as st

from config.database import get_connection

from config.auth_config import (
    verify_password,
    login_user
)


def login_page():

    st.subheader("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Login"):

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT *
            FROM users
            WHERE email=?
            """,
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if user:

            if verify_password(
                password,
                user["password"]
            ):

                login_user(
                    user["id"],
                    user["full_name"],
                    user["role"]
                )

                if user["role"] == "Doctor":
                    conn = get_connection()
                    conn.execute(
                        """
                        INSERT OR IGNORE INTO doctors(
                            user_id,
                            specialization,
                            department
                        )
                        VALUES (?, 'General Medicine', 'General')
                        """,
                        (user["id"],)
                    )
                    conn.commit()
                    conn.close()

                st.success(
                    f"Welcome {user['full_name']}"
                )

                st.rerun()

            else:

                st.error(
                    "Invalid Password"
                )

        else:

            st.error(
                "User Not Found"
            )
