import fitz
import re
import sys
import urllib.request
import tempfile
import os

# Searchable pdf
def extract(pdf):
    all_text = ""
    for page in pdf:
        text = page.get_text(sort = True)
        if check_garbage(text):
            return extract_OCR(pdf)
        all_text += text + "\n"
    return all_text

# Scanned text
def extract_OCR(pdf):
    all_text = ""
    for page in pdf:
        for item in page.get_images():
            xref = item[0]
            pix = fitz.Pixmap(pdf, xref)
            pdfdata = pix.pdfocr_tobytes()
            ocrpdf = fitz.open("pdf", pdfdata)
            ocrtext = ocrpdf[0].get_text(sort = True)
            all_text += ocrtext + "\n"
    return all_text

def check_garbage(text: str):
    if len(text) < 200:
        return True
    elif check_alphanum(text) > 0.5:
        return True
    else:
        return False

def check_alphanum(text: str):
    total = len(text)
    if total == 0:
        return 1.0
    else:
        non_alpha = len(re.findall(r"[^a-zA-Z0-9\s]", text))
        return non_alpha / total

def get_content(pdf_url):
    with tempfile.NamedTemporaryFile(dir = "./temp/pdfs/", suffix = ".pdf", delete = False) as temp:
        urllib.request.urlretrieve(pdf_url, temp.name)

    pdf = fitz.open(temp.name)
    if len(pdf) > 15:
        return ""
    content = extract(pdf)

    pdf.close()
    os.remove(temp.name)

    return content