def predict_recovery(
    age,
    severity_score,
    bmi
):

    score = max(
        10,
        100 - (
            age * 0.3 +
            severity_score * 0.5 +
            bmi * 0.2
        )
    )

    return round(score, 2)