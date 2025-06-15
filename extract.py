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

def convert_to_image(page):
    return

all_text = ""
pdf = fitz. open(pdf_path)
all_text = chr(12).join([page.get_text() for page in pdf])
print(all_text)