import random


def predict_diabetes(
    age,
    bmi,
    blood_pressure,
    glucose
):

    risk = min(
        100,
        (
            bmi * 0.4
            + glucose * 0.3
            + blood_pressure * 0.2
            + age * 0.1
        )
        / 2
    )

    if risk > 70:

        prediction = "High Diabetes Risk"

        severity = "High"

    elif risk > 40:

        prediction = "Moderate Diabetes Risk"

        severity = "Medium"

    else:

        prediction = "Low Diabetes Risk"

        severity = "Low"

    return {
        "prediction": prediction,
        "risk_score": round(risk, 2),
        "severity": severity
    }