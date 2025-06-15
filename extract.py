from pathlib import Path
import fitz
import re

pdf_path = Path(input("Enter the path of pdf: "))
if pdf_path.exists() and pdf_path.is_file():
    print("User input is correct")
    print(pdf_path)

else:
    print("User input is invalid")
    exit()

def check_alphanum(text: str):
    total = len(text)
    if total == 0:
        return 1.0
    else:
        non_alpha = len(re.findall(r"[^a-zA-Z0-9\s]", text))
        return non_alpha / total

all_text = ""
pdf = fitz. open(pdf_path)

# Searchable text
all_text = chr(12).join([page.get_text(sort = True) for page in pdf])

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