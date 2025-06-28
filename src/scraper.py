import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

current_year = str(datetime.today().year)

positive = ["recruitment", "appointment", "job", "filling up", "vacancy", "engagement", "contract basis", "hiring", "advertisement", "applications", "enlistment"]
negative = ["result", "updation"]

def direct_links(url):
    links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
        full_link = urljoin(url, link['href'])

        if full_link in links:
            continue
        if current_year not in full_link:
            continue

        link_text = link.text.strip().lower()
        for keyword in positive:
            if keyword in link_text:
                links.append(full_link)
                break
        
    return links

def link_to_link(url: str):
    return

def run():
    url = input("Enter url of portal page:")
    return direct_links(url)