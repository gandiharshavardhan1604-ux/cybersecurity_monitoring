import os

from dotenv import load_dotenv
from google import genai


load_dotenv()


def analyze_with_llm(event, rule_analysis):

    api_key = os.getenv("GEMINI_API_KEY")
    model_name = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

    client = genai.Client(api_key=api_key)

    prompt = f"""
You are a cybersecurity monitoring assistant.

Analyze the following security event.

Security Event:
Event Type: {event.event_type}
Username: {event.username}
IP Address: {event.ip_address}
Message: {event.message}

Rule-Based Analysis:
Risk Level: {rule_analysis["risk_level"]}
Threat: {rule_analysis["threat"]}
Reason: {rule_analysis["reason"]}

Provide a short cybersecurity analysis containing:

1. Threat assessment
2. Why the event may be suspicious
3. Recommended security action

Do not invent information that is not present in the event.
"""

    try:

        interaction = client.interactions.create(
            model=model_name,
            input=prompt,
            generation_config={
                "thinking_level": "low"
            },
            timeout=120
        )

        return interaction.output_text

    except Exception:

        return (
            "LLM analysis is temporarily unavailable. "
            "The result is based on rule-based security analysis."
        )