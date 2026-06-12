import streamlit as st

from config.database import initialize_database
from config.auth_config import initialize_session, logout_user

from modules.authentication.login import login_page
from modules.authentication.register import register_page

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from utils.roles import (
    patient_role,
    doctor_role,
    admin_role
)

# ----------------------------------
# PAGE CONFIG
# ----------------------------------

st.set_page_config(
    page_title="Smart Healthcare Analytics Platform",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------
# DATABASE INITIALIZATION
# ----------------------------------

initialize_database()
initialize_session()

# ----------------------------------
# CUSTOM CSS
# ----------------------------------
st.markdown("""
<style>
.main-title {
    font-size: 40px;
    font-weight: bold;
    color: #1f77b4;
}

.card {
    padding: 20px;
    border-radius: 10px;
    background-color: #f5f5f5;
    margin-bottom: 10px;
}

.metric-card {
    text-align: center;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 5px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)
# ----------------------------------
# HOME PAGE
# ----------------------------------

if not st.session_state.logged_in:

    st.markdown(
        """
        <div class='main-header'>
        🏥 Smart Healthcare Analytics Platform
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class='sub-header'>
        Intelligent Healthcare Platform using
        Artificial Intelligence, Machine Learning,
        Resource Optimization and Predictive Analytics
        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Login",
            "Register"
        ]
    )

    if menu == "Login":
        login_page()

    elif menu == "Register":
        register_page()
else:

    display_name = st.session_state.get("username") or st.session_state.get("user_name")
    display_role = st.session_state.get("role") or st.session_state.get("user_role")

    st.sidebar.success(f"Welcome {display_name}")
    st.sidebar.write(f"Role: {display_role}")

    st.markdown("## 📊 Healthcare Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Patients", "250")

    with col2:
        st.metric("Doctors Available", "35")

    with col3:
        st.metric("Prediction Accuracy", "94%")

st.info("AI-driven healthcare insights and patient monitoring system")
st.markdown("## 🤖 Virtual Health Assistant")

question = st.text_input("Ask your health-related question")

if question:
    st.success(f"You asked: {question}")
    st.write("Health Assistant Response: Please consult a healthcare professional for medical advice.")

    if st.sidebar.button("Logout"):
            logout_user()
            st.rerun()
            display_role = st.session_state.get("role") or st.session_state.get("user_role")

    if display_role == "Patient":
            patient_role()

    elif display_role == "Doctor":
            doctor_role()

    elif display_role == "Admin":
            admin_role()

    else:
            st.error("Invalid role assigned.")
