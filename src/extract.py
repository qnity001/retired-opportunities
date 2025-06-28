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
    return clean_pdf(all_text)

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

# Remove the forms to clean the pdf for LLM
def clean_pdf(text):
    triggers = [
        "application format",
        "application form",
        "format of application",
        "prescribed format",
        "application in the following format",
        "form"
    ]
    for phrase in triggers:
        index = text.lower().find(phrase)
        if index != -1 and index > len(text) * 0.6:  # appears toward the end
            return text[:index].strip()
    return text

def get_content(pdf_url):
    with tempfile.NamedTemporaryFile(dir = "../temp/pdfs/", suffix = ".pdf", delete = False) as temp:
        try:
            urllib.request.urlretrieve(pdf_url, temp.name)
        except:
            return ""

    try:
        pdf = fitz.open(temp.name)
    except:
        pdf.close()
        os.remove(temp.name)
        return ""
    
    if len(pdf) > 8:
        pdf.close()
        os.remove(temp.name)
        return ""
    
    content = extract(pdf)
    pdf.close()
    os.remove(temp.name)    
    return content