def predict_stay_duration(
    age,
    severity_score
):

    days = int(
        (severity_score / 10)
        + (age / 20)
    )

    return max(1, days)