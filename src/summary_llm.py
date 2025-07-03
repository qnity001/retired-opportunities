import ollama
import re
import json

with open("content.txt", "r",  encoding="utf-8", errors="ignore") as file:
    content = file.read()
    content = re.sub(r'\n\s*\n+', '\n\n', content)
    content = re.sub(r'[ \t]+', ' ', content) 

def summarize(content: str):
    
    input_prompt = f"""
    You are a government job summarizer. Summarize the key points from this PDF recruitment notice for retired professionals in under 150 words. 
    
    Instructions:
    - Read the content carefully.
    - Highlight only the useful information like skills, post name and job duration. 
    - Exclude instructions, forms and annexures, age limit, pay scale and application deadline. 
    - Summarize the following job posting strictly in a single, well-structured paragraph. Do not use bullet points or lists. Keep the summary concise, clear, and human-readable. 
    - Output ONLY the summary as plain text. Do NOT add introductions, disclaimers, or extra sentences. Begin directly with the first word of the summary.
    
    Text: {content} 
    Summary: 
    """

    response = ollama.generate(
        model = "llama3:8b",  
        prompt = input_prompt
    )
    return response["response"]

'''
def get_metadata(content: str):

    input_prompt = f"You are a government job assistant who checks for recruitments. The job post might be poorly formatted or noisy or garbled or jumbled. Extract the following fields from this government job post and return them as a JSON object: 'job_title', 'eligibility', 'minimum_qualification', 'age_limit', 'application_deadline', 'pay_scale', 'employment_type', 'field_of_work'. If any field is not present, return 'unknown'. Text: {content}"

    response = ollama.generate(
        model = "mistral:7b-instruct",
        prompt = input_prompt
    )
    json_object = response["response"]
    metadata = json.loads(json_object)
    return metadata
    '''