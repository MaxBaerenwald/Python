import requests
from bs4 import BeautifulSoup

def get_urls(url = "google.com"):
    """ Parses BlaBla"""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, features="html.parser")
    atags = {}
    for link in soup.find_all('a'):
        atags[link.get('href')] = link.get_text().split(' ')
    return atags
print(get_urls('http://www.python.org/'))