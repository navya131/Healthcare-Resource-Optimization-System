def get_treatment_plan(disease):

    treatments = {

        "Diabetes": [
            "Monitor blood sugar regularly",
            "Follow low sugar diet",
            "Exercise 30 minutes daily",
            "Regular HbA1c testing"
        ],

        "Heart Disease": [
            "Low cholesterol diet",
            "Daily walking",
            "Blood pressure monitoring",
            "Cardiology consultation"
        ],

        "Kidney Disease": [
            "Monitor kidney function",
            "Reduce sodium intake",
            "Hydration management",
            "Nephrologist consultation"
        ],

        "Cancer Risk": [
            "Regular screening",
            "Lifestyle modifications",
            "Further diagnostic evaluation",
            "Oncology consultation"
        ]
    }

    return treatments.get(
        disease,
        ["Consult healthcare provider"]
    )