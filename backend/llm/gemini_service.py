import os
import json

import google.generativeai as genai

from dotenv import load_dotenv

# -------------------------
# Load Environment Variables
# -------------------------

load_dotenv()

api_key = os.getenv(
    "GEMINI_API_KEY"
)

print(
    "KEY FOUND:",
    api_key is not None
)

if not api_key:

    raise ValueError(
        "GEMINI_API_KEY not found in .env file"
    )

# -------------------------
# Configure Gemini
# -------------------------

genai.configure(
    api_key=api_key
)

# Use a supported model
model = genai.GenerativeModel(
    "gemini-1.5-flash"
)

# -------------------------
# Medical Summary Generator
# -------------------------

def generate_medical_summary(
    report_data,
    risk_level,
    risk_score,
    shap_explanation
):

    prompt = f"""
You are an AI Medical Assistant.

Patient Report:
{report_data}

Risk Level:
{risk_level}

Risk Score:
{risk_score}

Feature Importance:
{shap_explanation}

Tasks:

1. Explain findings in simple language.
2. Mention abnormal values.
3. Give practical health recommendations.
4. Suggest whether a doctor consultation is needed.

Return ONLY valid JSON.

Example:

{{
    "summary": "Patient has elevated glucose levels...",
    "recommendations": [
        "Reduce sugar intake",
        "Exercise regularly",
        "Consult a physician"
    ]
}}
"""

    try:

        response = model.generate_content(
            prompt,
            generation_config={
                "temperature": 0.3,
                "top_p": 0.95,
                "max_output_tokens": 1000
            }
        )

        return response.text

    except Exception as e:

        print(
            "GEMINI ERROR:",
            str(e)
        )

        fallback = {

            "summary":
            f"""
Risk Level: {risk_level}

The patient shows signs of elevated risk based on
the extracted medical parameters.

Risk Score: {risk_score}
            """,

            "recommendations": [

                "Maintain a balanced diet",

                "Exercise at least 30 minutes daily",

                "Monitor blood glucose levels",

                "Consult a healthcare professional"
            ]
        }

        return json.dumps(
            fallback
        )