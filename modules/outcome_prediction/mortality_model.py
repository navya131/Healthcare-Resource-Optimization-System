def predict_mortality_risk(
    age,
    severity_score
):

    risk = (
        age * 0.5 +
        severity_score * 0.5
    )

    if risk >= 75:
        return "High"

    elif risk >= 50:
        return "Moderate"

    return "Low"