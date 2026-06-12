import streamlit as st

from config.database import get_connection

from modules.disease_prediction.diabetes_model import (
    predict_diabetes
)

from modules.disease_prediction.heart_model import (
    predict_heart_disease
)

from modules.disease_prediction.kidney_model import (
    predict_kidney_disease
)

from modules.disease_prediction.cancer_model import (
    predict_cancer_risk
)


def disease_prediction_page():

    st.header("🤖 AI Disease Prediction")

    disease_type = st.selectbox(
        "Select Prediction Model",
        [
            "Diabetes",
            "Heart Disease",
            "Kidney Disease",
            "Cancer Risk"
        ]
    )

    age = st.number_input(
        "Age",
        1,
        120
    )

    bmi = st.number_input(
        "BMI",
        10.0,
        60.0
    )

    blood_pressure = st.number_input(
        "Blood Pressure",
        50,
        250
    )

    glucose = st.number_input(
        "Glucose Level",
        50,
        500
    )

    cholesterol = st.number_input(
        "Cholesterol",
        50,
        500
    )

    if st.button("Predict Disease"):

        if disease_type == "Diabetes":

            result = predict_diabetes(
                age,
                bmi,
                blood_pressure,
                glucose
            )

        elif disease_type == "Heart Disease":

            result = predict_heart_disease(
                age,
                bmi,
                blood_pressure,
                cholesterol
            )

        elif disease_type == "Kidney Disease":

            result = predict_kidney_disease(
                age,
                bmi,
                blood_pressure,
                glucose
            )

        else:

            result = predict_cancer_risk(
                age,
                bmi
            )

        st.success(
            f"Prediction: {result['prediction']}"
        )

        st.metric(
            "Risk Score",
            f"{result['risk_score']}%"
        )

        st.metric(
            "Severity",
            result['severity']
        )

        user_id = st.session_state.get("user_id")
        if user_id:
            conn = get_connection()
            conn.execute(
                """
                INSERT INTO disease_predictions(
                    patient_user_id,
                    disease_type,
                    prediction,
                    risk_score,
                    severity
                )
                VALUES(?,?,?,?,?)
                """,
                (
                    user_id,
                    disease_type,
                    result["prediction"],
                    result["risk_score"],
                    result["severity"],
                ),
            )
            conn.commit()
            conn.close()
