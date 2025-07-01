from src.scraper import get_links
from src.extract import get_content
from summary_llm import summarize, get_metadata
import json
import re

open("results.jsonl", "w").close()

def remove_extra_spaces(content: str):
    text = re.sub(r'\n\s*\n+', '\n\n', content)
    text = re.sub(r'[ \t]+', ' ', text)  
    return text

def run():
    links = get_links()
    for link in links:
        print(link)
        content = get_content(link)
        if content == "":
            continue
        content = remove_extra_spaces(content)

        # Send the content to ollama for summary
        content = summarize(content)
        metadata = get_metadata(content)
        print(metadata)

        # Save the information in jsonl
        output = {
            "url" : link,
            "content": content
        }
        with open("results.jsonl", "a", encoding="utf-8") as file:
            file.write(json.dumps(output, ensure_ascii = False) + "\n")
