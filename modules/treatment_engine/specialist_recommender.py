def recommend_specialist(disease):

    specialists = {

        "Diabetes":
            "Endocrinologist",

        "Heart Disease":
            "Cardiologist",

        "Kidney Disease":
            "Nephrologist",

        "Cancer Risk":
            "Oncologist"
    }

    return specialists.get(
        disease,
        "General Physician"
    )