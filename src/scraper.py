import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from datetime import datetime

current_year = str(datetime.today().year)

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
    for word in positive_keywords:
        if word in link_text:
            return True
    return False


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
        if keyword_check(link_text):
            links.append(full_link)
        
    return links

'''
def link_to_link(url: str):
    links = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    for link in soup.select("a[href]"):
        link_text = link.text.strip().lower()
        

        full_link = urljoin(url, link['href'])
        response2 = requests.get(full_link)
        soup2 = BeautifulSoup(response2.text, "html.parser")
        for link2 in soup2.select("a[href$='.pdf']"):
            full_link2 = urljoin(full_link, link2['href'])
            links.append(full_link2)
    
    return links

'''

def get_links():
    url = input("Enter url of portal page:")
    return direct_links(url)