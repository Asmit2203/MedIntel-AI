from flask import Blueprint
from flask import request
from flask import jsonify

import os
import json
import traceback

from ocr.extract_text import extract_text

from ocr.parse_report import (
    parse_report,
    build_parameter_list
)

from ml.predict import predict_risk

from ml.explain import (
    explain_prediction
)

from llm.gemini_service import (
    generate_medical_summary
)

upload_bp = Blueprint(
    "upload_bp",
    __name__
)

UPLOAD_FOLDER = "uploads"


@upload_bp.route(
    "/upload",
    methods=["POST"]
)
def upload_file():

    try:

        print("\n========== NEW UPLOAD ==========")

        # --------------------------
        # Validate File
        # --------------------------

        if "file" not in request.files:

            return jsonify({
                "message":
                "No file uploaded"
            }), 400

        file = request.files["file"]

        if file.filename == "":

            return jsonify({
                "message":
                "Empty file"
            }), 400

        print("STEP 1: FILE RECEIVED")

        # --------------------------
        # Save File
        # --------------------------

        os.makedirs(
            UPLOAD_FOLDER,
            exist_ok=True
        )

        file_path = os.path.join(
            UPLOAD_FOLDER,
            file.filename
        )

        file.save(file_path)

        print(
            f"Saved File: {file_path}"
        )

        # --------------------------
        # OCR
        # --------------------------

        extracted_text = extract_text(
            file_path
        )

        print("STEP 2: OCR COMPLETE")

        print("\nOCR TEXT:\n")
        print(extracted_text)

        # --------------------------
        # Parse Report
        # --------------------------

        report = parse_report(
            extracted_text
        )

        print("STEP 3: REPORT PARSED")

        print(report)

        # --------------------------
        # Feature Vector
        # --------------------------

        features = [

            report.get(
                "Pregnancies"
            ) or 0,

            report.get(
                "Glucose"
            ) or 100,

            report.get(
                "BloodPressure"
            ) or 80,

            report.get(
                "SkinThickness"
            ) or 20,

            report.get(
                "Insulin"
            ) or 80,

            report.get(
                "BMI"
            ) or 22,

            report.get(
                "DiabetesPedigreeFunction"
            ) or 0.5,

            report.get(
                "Age"
            ) or 30
        ]

        print("\nFEATURES:")
        print(features)

        # --------------------------
        # Prediction
        # --------------------------

        prediction = predict_risk(
            features
        )

        print("STEP 4: PREDICTION COMPLETE")

        print(prediction)

        # --------------------------
        # SHAP
        # --------------------------

        shap_data = explain_prediction(
            features,
            [
                "Pregnancies",
                "Glucose",
                "BloodPressure",
                "SkinThickness",
                "Insulin",
                "BMI",
                "DiabetesPedigreeFunction",
                "Age"
            ]
        )

        print("STEP 5: SHAP COMPLETE")

        print(shap_data)

        # --------------------------
        # Gemini
        # --------------------------

        llm_response = (
            generate_medical_summary(
                report,
                prediction[
                    "risk_level"
                ],
                prediction[
                    "risk_score"
                ],
                shap_data
            )
        )

        print("STEP 6: GEMINI COMPLETE")

        print(llm_response)

        # --------------------------
        # Parse Gemini JSON
        # --------------------------

        try:

            parsed_llm = json.loads(
                llm_response
            )

        except:

            parsed_llm = {
                "summary":
                llm_response,
                "recommendations":
                []
            }

        # --------------------------
        # Final Response
        # --------------------------

        return jsonify({

            "risk_level":
            prediction[
                "risk_level"
            ],

            "risk_score":
            prediction[
                "risk_score"
            ],

            "summary":
            parsed_llm.get(
                "summary",
                "No summary generated."
            ),

            "recommendations":
            parsed_llm.get(
                "recommendations",
                []
            ),

            "parameters":
            build_parameter_list(
                report
            )
        })

    except Exception as e:

        print(
            "\n========== ERROR =========="
        )

        traceback.print_exc()

        return jsonify({
            "error":
            str(e)
        }), 500