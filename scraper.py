import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def direct_links():
    links = []
    url = input("Enter url of portal page:")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href$='.pdf']"):
        full_link = urljoin(url, link['href'])
        links.append(full_link)
    return links
