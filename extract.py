from pathlib import Path
import fitz

pdf_path = Path(input("Enter the path of pdf: "))
if pdf_path.exists() and pdf_path.is_file():
    print("User input is correct")
    print(pdf_path)

else:
    print("User input is invalid")
    exit()

open("content.txt", "w").close()

pdf = fitz.open(pdf_path)
for page in pdf:
    text = page.get_text()
    if len(text) < 200:
        print("Use OCR!")
    with open("content.txt", "a", encoding="utf-8") as file:
        file.write(text)