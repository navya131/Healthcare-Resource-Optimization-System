import streamlit as st

from modules.treatment_engine.treatment_recommender import (
    get_treatment_plan
)

from modules.treatment_engine.specialist_recommender import (
    recommend_specialist
)

from modules.treatment_engine.medication_advisor import (
    medication_guidance
)


def treatment_recommendation_page():

    st.header(
        "🩺 Treatment Recommendation Engine"
    )

    disease = st.selectbox(
        "Select Predicted Disease",
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Cancer Risk"
        ]
    )

    specialist = recommend_specialist(
        disease
    )

    treatment_plan = get_treatment_plan(
        disease
    )

    medications = medication_guidance(
        disease
    )

    st.subheader(
        "👨‍⚕️ Recommended Specialist"
    )

    st.success(specialist)

    st.subheader(
        "📋 Treatment Plan"
    )

    for item in treatment_plan:
        st.write(f"✅ {item}")

    st.subheader(
        "💊 Medication Guidance"
    )

    for med in medications:
        st.write(f"💊 {med}")

    st.subheader(
        "🔬 Suggested Tests"
    )

    if disease == "Diabetes":

        st.write("• HbA1c Test")
        st.write("• Fasting Blood Sugar")

    elif disease == "Heart Disease":

        st.write("• ECG")
        st.write("• Echocardiogram")

    elif disease == "Kidney Disease":

        st.write("• Creatinine Test")
        st.write("• Urine Analysis")

    elif disease == "Cancer Risk":

        st.write("• MRI")
        st.write("• CT Scan")
        st.write("• Biopsy")