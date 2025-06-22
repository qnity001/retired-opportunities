import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

current_year = str(datetime.today().year)

def direct_links():
    links = []
    url = input("Enter url of portal page:")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
        full_link = urljoin(url, link['href'])
        if current_year not in full_link:
            continue
        links.append(full_link)
    return links
