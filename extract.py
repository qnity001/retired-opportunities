from pathlib import Path
import fitz

pdf_path = Path(input("Enter the path of pdf: "))
if pdf_path.exists() and pdf_path.is_file():
    print("User input is correct")
    print(pdf_path)

else:
    print("User input is invalid")
    exit()

pdf = fitz.open(pdf_path)
for page in pdf:
    text = page.get_text()
    with open("content.txt", "w") as file:
        file.write(text)
    