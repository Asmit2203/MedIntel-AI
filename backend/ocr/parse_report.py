import re

from utils.ranges import (
    NORMAL_RANGES
)


def extract_value(
    text,
    keyword
):

    pattern = (
        rf"{keyword}\D+(\d+\.?\d*)"
    )

    match = re.search(
        pattern,
        text,
        re.IGNORECASE
    )

    if match:

        return float(
            match.group(1)
        )

    return None


def parse_report(text):

    report = {

        "Pregnancies":
        extract_value(
            text,
            "Pregnancies"
        ),

        "Glucose":
        extract_value(
            text,
            "Glucose"
        ),

        "BloodPressure":
        extract_value(
            text,
            "Blood Pressure"
        ),

        "SkinThickness":
        extract_value(
            text,
            "Skin Thickness"
        ),

        "Insulin":
        extract_value(
            text,
            "Insulin"
        ),

        "BMI":
        extract_value(
            text,
            "BMI"
        ),

        "DiabetesPedigreeFunction":
        extract_value(
            text,
            "Pedigree"
        ),

        "Age":
        extract_value(
            text,
            "Age"
        )
    }

    return report

def parameter_status(
    parameter,
    value
):

    if value is None:

        return "Unknown"

    low, high = (
        NORMAL_RANGES[
            parameter
        ]
    )

    if value < low:

        return "Low"

    if value > high:

        return "High"

    return "Normal"

def build_parameter_list(report):

    result = []

    for key, value in report.items():

        result.append({
            "name": key,
            "value": value,
            "status": parameter_status(
                key,
                value
            )
        })

    return result