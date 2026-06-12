import streamlit as st


def load_css(css_file):
    with open(css_file) as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


def show_success(message):
    st.success(message)


def show_error(message):
    st.error(message)


def show_warning(message):
    st.warning(message)