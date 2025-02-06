# OCR Project Setup

Follow these steps to set up and run the project.

## Prerequisites

- Python installed
- Node.js installed

## Steps to Set Up the Project

### 1. Create a Python Virtual Environment
Open the terminal and run:
```sh
python -m venv venv
mkdir ocr_project
cd ocr_project
source ../venv/bin/activate
pip install Flask pytesseract Pillow
npm install --local http-server
mkdir node_modules
python app.py
