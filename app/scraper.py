import requests
from bs4 import BeautifulSoup


def scrape_shl_page(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.title.text

    return {
        "title": title
    }