from config.settings import GROQ_API_KEY
from modules.chatbot.chatbot_engine import get_bot_response

try:
    from groq import Groq
except ModuleNotFoundError:
    Groq = None


client = None

if Groq is not None and GROQ_API_KEY:
    try:
        client = Groq(api_key=GROQ_API_KEY)
    except Exception:
        client = None


def get_ai_response(prompt):

    if client is None:
        return get_bot_response(prompt)

    try:
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content":
                    """
                    You are a healthcare AI assistant.
                    Provide general healthcare guidance.
                    Never diagnose patients.
                    Always recommend consulting a doctor.
                    """
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3,
            max_tokens=500
        )

        return completion.choices[0].message.content
    except Exception:
        return get_bot_response(prompt)
