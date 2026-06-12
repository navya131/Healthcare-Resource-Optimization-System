def predict_icu_need(
    age,
    severity_score
):

    risk = (
        age * 0.4 +
        severity_score * 0.6
    )

    if risk >= 70:
        return "High"

    elif risk >= 40:
        return "Medium"

    return "Low"