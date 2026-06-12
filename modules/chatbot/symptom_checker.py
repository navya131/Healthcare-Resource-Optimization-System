def check_symptoms(symptoms):

    symptoms = symptoms.lower()

    if "fever" in symptoms and "cough" in symptoms:

        return (
            "Possible respiratory infection. "
            "Consult a physician."
        )

    if "chest pain" in symptoms:

        return (
            "Possible cardiac condition. "
            "Seek medical attention."
        )

    if "headache" in symptoms:

        return (
            "May be due to stress, migraine, "
            "or dehydration."
        )

    return (
        "Unable to determine condition. "
        "Consult a doctor."
    )