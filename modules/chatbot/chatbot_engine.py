def get_bot_response(message):

    message = message.lower()

    responses = {

        "hello":
            "Hello! How can I help you today?",

        "appointment":
            "You can book appointments from the Appointment Module.",

        "diabetes":
            "Maintain a healthy diet, exercise regularly, and monitor glucose levels.",

        "heart disease":
            "Regular checkups and lifestyle management are recommended.",

        "medicine":
            "Please consult your doctor before taking any medication.",

        "help":
            "I can assist with symptoms, appointments, medicines, and reports."
    }

    for keyword, response in responses.items():

        if keyword in message:

            return response

    return (
        "I couldn't understand your query. "
        "Please consult a healthcare professional."
    )