import pdfplumber
import easyocr
import os

reader = None


def get_reader():

    global reader

    if reader is None:

        print("Loading EasyOCR...")

        reader = easyocr.Reader(
            ['en']
        )

    return reader


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

        reader = get_reader()

        results = reader.readtext(
            file_path,
            detail=0
        )

        text = "\n".join(
            results
        )

    return text