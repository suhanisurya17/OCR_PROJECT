from flask import Flask, request, render_template
import pytesseract
from PIL import Image
from io import BytesIO
import enum

app = Flask(__name__)


class OS(enum.Enum):
    Mac = 0
    Windows = 1


class Language(enum.Enum):
    ENG = 'eng'
    RUS = 'rus'
    ITA = 'ita'


class ImageReader:

    def __init__(self, os: OS):
        if os == OS.Mac:
            print('Running on: MAC\n')

    def extract_text(self, image_path: str, lang: Language) -> str:
        img = Image.open(image_path)
        extracted_text = pytesseract.image_to_string(img, lang=lang.value)
        return extracted_text


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    if file.filename == '':
        return 'No selected file'

    img_byte_arr = BytesIO()
    img_byte_arr.write(file.read())

    ir = ImageReader(OS.Mac)  # Initialize ImageReader
    text = ir.extract_text(img_byte_arr, lang=Language.ENG)  # Extract text from uploaded image

    return render_template('index.html', extracted_text=text)


if __name__ == '__main__':
    app.run(port=5001)  # Specify a different port to avoid conflicts

# Steps to get everything running
# python -m venv venv
# pip install Flask
# pip install pytesseract
# pip install Pillow
# npm install --local http-server
# source ./venv/bin/activate
# cd ocr_project
# python app.py