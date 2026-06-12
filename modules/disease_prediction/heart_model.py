def predict_heart_disease(
    age,
    bmi,
    blood_pressure,
    cholesterol
):

    risk = min(
        100,
        (
            cholesterol * 0.4
            + blood_pressure * 0.3
            + age * 0.2
            + bmi * 0.1
        )
        / 3
    )

    if risk > 70:

        return {
            "prediction": "Heart Disease Risk",
            "risk_score": round(risk, 2),
            "severity": "High"
        }

    elif risk > 40:

        return {
            "prediction": "Moderate Risk",
            "risk_score": round(risk, 2),
            "severity": "Medium"
        }

    return {
        "prediction": "Low Risk",
        "risk_score": round(risk, 2),
        "severity": "Low"
    }