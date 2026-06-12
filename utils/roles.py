# utils/roles.py

import streamlit as st

# ==========================================
# Patient Management
# ==========================================

from modules.patient_management.patient_registration import (
    patient_registration
)

from modules.analytics.patient_dashboard import (
    patient_dashboard_page
)

# ==========================================
# Doctor Management
# ==========================================

from modules.doctor_management.doctor_profile import (
    doctor_profile
)

from modules.analytics.doctor_dashboard import (
    doctor_dashboard_page
)

# ==========================================
# Appointment Management
# ==========================================

from modules.appointment_management.booking import (
    book_appointment
)

from modules.appointment_management.approval import (
    manage_appointments
)

# ==========================================
# EHR
# ==========================================

from modules.ehr.medical_records import (
    medical_records_page
)

from modules.ehr.prescriptions import (
    prescriptions_page
)

from modules.ehr.diagnostics import (
    diagnostics_page
)

from modules.ehr.vaccinations import (
    vaccinations_page
)

# ==========================================
# Disease Prediction
# ==========================================

from modules.disease_prediction.predictor import (
    disease_prediction_page
)

# ==========================================
# Treatment Recommendation
# ==========================================

from modules.treatment_engine.treatment_page import (
    treatment_recommendation_page
)

# ==========================================
# Outcome Prediction
# ==========================================

from modules.outcome_prediction.outcome_page import (
    outcome_prediction_page
)

# ==========================================
# Bed Management
# ==========================================

from modules.bed_management.bed_dashboard import (
    bed_dashboard_page
)

from modules.bed_management.bed_tracker import (
    bed_tracker_page
)

from modules.bed_management.ward_allocation import (
    ward_allocation_page
)

# ==========================================
# Staff Management
# ==========================================

from modules.staff_management.staff_dashboard import (
    staff_dashboard_page
)

from modules.staff_management.shift_scheduler import (
    shift_scheduler_page
)

from modules.staff_management.nurse_allocation import (
    nurse_allocation_page
)

# ==========================================
# Resource Management
# ==========================================

from modules.resource_management.resource_dashboard import (
    resource_dashboard_page
)

from modules.resource_management.ventilator import (
    ventilator_page
)

from modules.resource_management.oxygen_units import (
    oxygen_units_page
)

from modules.resource_management.equipment import (
    equipment_page
)

# ==========================================
# Report Analysis
# ==========================================

from modules.report_analysis.report_dashboard import (
    report_dashboard_page
)

# ==========================================
# Emergency Alerts
# ==========================================

from modules.emergency_alerts.emergency_monitor import (
    emergency_monitor_page
)

from modules.emergency_alerts.ambulance_request import (
    ambulance_request_page
)

from modules.emergency_alerts.alert_dashboard import (
    alert_dashboard_page
)

# ==========================================
# Chatbot
# ==========================================

from modules.chatbot.chatbot_page import (
    chatbot_page
)

# ==========================================
# Analytics
# ==========================================

from modules.analytics.patient_dashboard import (
    patient_dashboard_page as analytics_patient_dashboard
)

from modules.analytics.doctor_dashboard import (
    doctor_dashboard_page as analytics_doctor_dashboard
)

from modules.analytics.admin_dashboard import (
    admin_analytics_page
)

# ==========================================
# Notifications
# ==========================================

from modules.notifications.notification_dashboard import (
    notification_dashboard_page
)

# ==========================================
# Reporting
# ==========================================

from modules.reporting.report_center import (
    report_center_page
)


def ehr_records_page():

    tab1, tab2, tab3, tab4 = st.tabs(
        [
            "Medical Records",
            "Prescriptions",
            "Diagnostics",
            "Vaccinations"
        ]
    )

    with tab1:
        medical_records_page()

    with tab2:
        prescriptions_page()

    with tab3:
        diagnostics_page()

    with tab4:
        vaccinations_page()

# =========================================================
# PATIENT ROLE
# =========================================================

def patient_role():

    st.sidebar.title("👤 Patient Panel")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Patient Registration",
            "Book Appointment",
            "EHR Records",
            "Disease Prediction",
            "Treatment Recommendation",
            "Outcome Prediction",
            "Medical Report Analysis",
            "Emergency Monitor",
            "Ambulance Request",
            "AI Healthcare Assistant",
            "Analytics Dashboard",
            "Notifications & Reminders",
            "Reporting Center"
        ]
    )

    if menu == "Dashboard":
        patient_dashboard_page()

    elif menu == "Patient Registration":
        patient_registration()

    elif menu == "Book Appointment":
        book_appointment()

    elif menu == "EHR Records":
        ehr_records_page()

    elif menu == "Disease Prediction":
        disease_prediction_page()

    elif menu == "Treatment Recommendation":
        treatment_recommendation_page()

    elif menu == "Outcome Prediction":
        outcome_prediction_page()

    elif menu == "Medical Report Analysis":
        report_dashboard_page()

    elif menu == "Emergency Monitor":
        emergency_monitor_page()

    elif menu == "Ambulance Request":
        ambulance_request_page()

    elif menu == "AI Healthcare Assistant":
        chatbot_page()

    elif menu == "Analytics Dashboard":
        analytics_patient_dashboard()

    elif menu == "Notifications & Reminders":
        notification_dashboard_page()

    elif menu == "Reporting Center":
        report_center_page()


# =========================================================
# DOCTOR ROLE
# =========================================================

def doctor_role():

    st.sidebar.title("👨‍⚕️ Doctor Panel")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Dashboard",
            "Doctor Profile",
            "Manage Appointments",
            "EHR Records",
            "Treatment Recommendation",
            "Analytics Dashboard",
            "Notifications & Reminders",
            "Reporting Center"
        ]
    )

    if menu == "Dashboard":
        doctor_dashboard_page()

    elif menu == "Doctor Profile":
        doctor_profile()

    elif menu == "Manage Appointments":
        manage_appointments()

    elif menu == "EHR Records":
        ehr_records_page()

    elif menu == "Treatment Recommendation":
        treatment_recommendation_page()

    elif menu == "Analytics Dashboard":
        analytics_doctor_dashboard()

    elif menu == "Notifications & Reminders":
        notification_dashboard_page()

    elif menu == "Reporting Center":
        report_center_page()


# =========================================================
# ADMIN ROLE
# =========================================================

def admin_role():

    st.sidebar.title("🛡️ Admin Panel")

    menu = st.sidebar.radio(
        "Navigation",
        [
            "Healthcare Analytics",

            "Bed Dashboard",
            "Bed Tracker",
            "Ward Allocation",

            "Staff Dashboard",
            "Shift Scheduler",
            "Nurse Allocation",

            "Resource Dashboard",
            "Ventilator Management",
            "Oxygen Units",
            "Equipment Management",

            "Emergency Alerts",

            "Notification Center",

            "Reporting Center"
        ]
    )

    if menu == "Healthcare Analytics":
        admin_analytics_page()

    elif menu == "Bed Dashboard":
        bed_dashboard_page()

    elif menu == "Bed Tracker":
        bed_tracker_page()

    elif menu == "Ward Allocation":
        ward_allocation_page()

    elif menu == "Staff Dashboard":
        staff_dashboard_page()

    elif menu == "Shift Scheduler":
        shift_scheduler_page()

    elif menu == "Nurse Allocation":
        nurse_allocation_page()

    elif menu == "Resource Dashboard":
        resource_dashboard_page()

    elif menu == "Ventilator Management":
        ventilator_page()

    elif menu == "Oxygen Units":
        oxygen_units_page()

    elif menu == "Equipment Management":
        equipment_page()

    elif menu == "Emergency Alerts":
        alert_dashboard_page()

    elif menu == "Notification Center":
        notification_dashboard_page()

    elif menu == "Reporting Center":
        report_center_page()
