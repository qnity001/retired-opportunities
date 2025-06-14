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

open("content.txt", "w").close()

pdf = fitz.open(pdf_path)
for page in pdf:
    text = page.get_text()
    if len(text) < 200 or check_alphanum(text) > 0.5:
        print("Use OCR!")
    with open("content.txt", "a", encoding="utf-8") as file:
        file.write(text)