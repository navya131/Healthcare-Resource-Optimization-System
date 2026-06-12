def predict_kidney_disease(
    age,
    bmi,
    blood_pressure,
    glucose
):

    risk = min(
        100,
        (
            glucose * 0.35
            + blood_pressure * 0.35
            + age * 0.2
            + bmi * 0.1
        )
        / 3
    )

    severity = (
        "High"
        if risk > 70
        else "Medium"
        if risk > 40
        else "Low"
    )

    return {
        "prediction": "Kidney Disease Assessment",
        "risk_score": round(risk, 2),
        "severity": severity
    }