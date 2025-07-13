from src.scraper import get_links
from src.extract import get_content
from src.summary_llm_api import summarize
import json
import re

def remove_extra_spaces(content: str):
    text = re.sub(r'\n\s*\n+', '\n\n', content)
    text = re.sub(r'[ \t]+', ' ', text)  
    return text

def run():
    output = {}
    links = get_links()
    for link in links:
        print(link)
        content = get_content(link)
        if content == "":
            continue
        content = remove_extra_spaces(content)

        # Send the content to ollama for summary
        content = summarize(content)
        #metadata = get_metadata(content)
        #print(metadata)

        # Save the information in dictionary
        output[link] = content

    with open("retired_backend/summaries/data/summary_data.json", "w") as file:
        file.write(json.dumps(output, indent=4))
    print("Stored the contents in results.json")
