def medication_guidance(disease):

    medications = {

        "Diabetes": [
            "Metformin (Doctor Prescription Required)",
            "Blood Sugar Monitoring"
        ],

        "Heart Disease": [
            "Blood Pressure Management",
            "Cholesterol Control Medication"
        ],

        "Kidney Disease": [
            "Kidney Function Support Medication",
            "Blood Pressure Control"
        ],

        "Cancer Risk": [
            "Specialist Evaluation Required"
        ]
    }

    return medications.get(
        disease,
        ["Consult Doctor"]
    )