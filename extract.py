from pathlib import Path
import fitz
import re
import sys

def check_alphanum(text: str):
    total = len(text)
    if total == 0:
        return 1.0
    else:
        non_alpha = len(re.findall(r"[^a-zA-Z0-9\s]", text))
        return non_alpha / total

all_text = ""
pdf = fitz. open(sys.argv[1])

# Searchable text
#all_text = chr(12).join([page.get_text(sort = True) for page in pdf])

# Scanned text
for page in pdf:
    for item in page.get_images():
        xref = item[0]
        pix = fitz.Pixmap(pdf, xref)
        pdfdata = pix.pdfocr_tobytes()
        ocrpdf = fitz.open("pdf", pdfdata)
        ocrtext = ocrpdf[0].get_text(sort = True)
        all_text += ocrtext + chr(12)

print(all_text)