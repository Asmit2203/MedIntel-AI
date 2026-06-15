from flask import Blueprint
from flask import request
from flask import jsonify

from llm.gemini_service import model

chat_bp = Blueprint(
    "chat_bp",
    __name__
)


@chat_bp.route(
    "/chat",
    methods=["POST"]
)
def chat():

    try:

        data = request.json

        question = data.get(
            "question",
            ""
        )

        if not question:

            return jsonify({
                "answer":
                "Please provide a question."
            })

        prompt = f"""
You are an AI medical assistant.

Answer the following question in simple language.

Question:
{question}

Keep answer concise and informative.
"""

        response = model.generate_content(
            prompt
        )

        return jsonify({
            "answer":
            response.text
        })

    except Exception as e:

        print(
            "CHAT ERROR:",
            str(e)
        )

        return jsonify({
            "answer":
            f"Backend Error: {str(e)}"
        }), 500