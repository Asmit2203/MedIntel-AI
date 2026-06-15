from parse_report import (
    parse_report,
    build_parameter_list
)

sample_text = """
Pregnancies: 2
Glucose: 180
Blood Pressure: 90
Skin Thickness: 35
Insulin: 180
BMI: 32.5
Pedigree: 0.8
Age: 45
"""

report = parse_report(
    sample_text
)

print(report)

print(
    build_parameter_list(
        report
    )
)