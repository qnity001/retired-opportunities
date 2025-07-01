import requests
from bs4 import BeautifulSoup, SoupStrainer
from urllib.parse import urljoin

def keyword_check(link_text):
    positive_keywords = [
        "walk-in-interview", 
        "walk in", 
        "walk-in", 
        "interview", 
        "recruitment", 
        "appointment", 
        "job", 
        "filling up", 
        "vacancy", 
        "engagement", 
        "contract basis", 
        "hiring", 
        "advertisement", 
        "applications", 
        "application", 
        "enlistment"
    ]
    negative_keywords = [
        "proforma",
        "birth certificate", 
        "death certificate",
        "rti",
        "update"
    ]
    for word in negative_keywords:
        if word in link_text:
            return False
    for word in positive_keywords:
        if word in link_text:
            return True
    return False

url = input("Enter url:")
response = requests.get(url)

for link in BeautifulSoup(response.text, 'html.parser', parse_only=SoupStrainer('a')):
    if link.has_attr('href'):
        link_text = link.text.strip().lower()
        if keyword_check(link_text):
            full_url = urljoin(url, link['href'])
            response_2 = requests.get(full_url)
            soup_2 = BeautifulSoup(response_2.text, "html.parser")
            for link in soup_2.select("a[href$='.pdf']"):
                pdf_url = urljoin(full_url, link['href'])

                # Try to get the text near or above the PDF link
                parent = link.find_parent()
                nearby_text = parent.get_text(strip=True).lower() if parent else ""

                if keyword_check(nearby_text):
                    print(pdf_url)

