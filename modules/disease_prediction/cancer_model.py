def predict_cancer_risk(
    age,
    bmi
):

    risk = min(
        100,
        (
            age * 0.7
            + bmi * 0.3
        )
    )

    severity = (
        "High"
        if risk > 70
        else "Medium"
        if risk > 40
        else "Low"
    )

    return {
        "prediction": "Cancer Risk Assessment",
        "risk_score": round(risk, 2),
        "severity": severity
    }