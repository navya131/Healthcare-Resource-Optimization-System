import streamlit as st

from config.database import get_connection

from modules.outcome_prediction.recovery_model import (
    predict_recovery
)

from modules.outcome_prediction.icu_prediction import (
    predict_icu_need
)

from modules.outcome_prediction.mortality_model import (
    predict_mortality_risk
)

from modules.outcome_prediction.stay_duration import (
    predict_stay_duration
)


def outcome_prediction_page():

    st.header(
        "📈 Patient Outcome Prediction"
    )

    age = st.number_input(
        "Age",
        min_value=1,
        max_value=120,
        value=35
    )

    severity_score = st.slider(
        "Disease Severity Score",
        1,
        100,
        50
    )

    bmi = st.number_input(
        "BMI",
        min_value=10.0,
        max_value=60.0,
        value=25.0
    )

    if st.button(
        "Predict Outcome"
    ):

        recovery = predict_recovery(
            age,
            severity_score,
            bmi
        )

        icu = predict_icu_need(
            age,
            severity_score
        )

        mortality = predict_mortality_risk(
            age,
            severity_score
        )

        stay = predict_stay_duration(
            age,
            severity_score
        )

        st.subheader(
            "Prediction Results"
        )

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "Recovery Probability",
                f"{recovery}%"
            )

            st.metric(
                "ICU Requirement",
                icu
            )

        with col2:
            st.metric(
                "Mortality Risk",
                mortality
            )

            st.metric(
                "Expected Stay",
                f"{stay} Days"
            )

        st.success(
            "Outcome Prediction Completed"
        )

        user_id = st.session_state.get("user_id")
        if user_id:
            conn = get_connection()
            conn.execute(
                """
                INSERT INTO outcome_predictions(
                    patient_user_id,
                    recovery_probability,
                    icu_requirement,
                    mortality_risk,
                    expected_stay
                )
                VALUES(?,?,?,?,?)
                """,
                (
                    user_id,
                    recovery,
                    icu,
                    mortality,
                    stay,
                ),
            )
            conn.commit()
            conn.close()
