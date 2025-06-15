from pathlib import Path
import fitz
import re
import sys

# Searchable pdf
def extract_plain(pdf):
    all_text = ""
    for page in pdf:
        text = page.get_text(sort = True)
        if check_garbage(text):
            text = extract_OCR(pdf, page)
        all_text += text + chr(12)

# Scanned text
def extract_OCR(pdf, page):
    for item in page.get_images():
        xref = item[0]
        pix = fitz.Pixmap(pdf, xref)
        pdfdata = pix.pdfocr_tobytes()
        ocrpdf = fitz.open("pdf", pdfdata)
        ocrtext = ocrpdf[0].get_text(sort = True)
        return ocrtext

def check_garbage(text: str):
    if len(text) < 200:
        return True
    elif not text.isascii():
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

if __name__ == "__main__":
    pdf = fitz.open(sys.argv[1])
    all_text = extract_OCR(pdf)
    print(all_text)