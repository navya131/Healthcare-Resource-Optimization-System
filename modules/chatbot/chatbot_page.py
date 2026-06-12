import streamlit as st

from config.database import get_connection

from modules.chatbot.chatbot_engine import (
    get_bot_response
)
from modules.chatbot.groq_chatbot import (
    get_ai_response
)


def chatbot_page():

    st.header(
        "🤖 AI Healthcare Assistant"
    )

    if "chat_history" not in st.session_state:

        st.session_state.chat_history = []

    user_input = st.chat_input(
        "Ask a healthcare question..."
    )

    if user_input:

        response = get_ai_response(
            user_input
        )

        st.session_state.chat_history.append(
            ("You", user_input)
        )

        st.session_state.chat_history.append(
            ("Bot", response)
        )

        conn = get_connection()

        conn.execute(
            """
            INSERT INTO chatbot_history(
                user_id,
                user_message,
                bot_response
            )
            VALUES(?,?,?)
            """,
            (
                st.session_state.user_id,
                user_input,
                response
            )
        )

        conn.commit()
        conn.close()

    for sender, message in st.session_state.chat_history:

        if sender == "You":

            with st.chat_message(
                "user"
            ):
                st.write(message)

        else:

            with st.chat_message(
                "assistant"
            ):
                st.write(message)