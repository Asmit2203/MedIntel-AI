import pdfplumber
import easyocr
import os


reader = easyocr.Reader(['en'])


def extract_text(file_path):

    extension = os.path.splitext(
        file_path
    )[1].lower()

    text = ""

    if extension == ".pdf":

        with pdfplumber.open(
            file_path
        ) as pdf:

            for page in pdf.pages:

                page_text = (
                    page.extract_text()
                )

                if page_text:
                    text += (
                        page_text + "\n"
                    )

    else:

        results = reader.readtext(
            file_path,
            detail=0
        )

        text = "\n".join(results)

    return text

def build_parameter_list(
    report
):

    result = []

    for key, value in report.items():

        result.append({

            "name": key,

            "value": value,

            "status":
            parameter_status(
                key,
                value
            )
        })

    return result