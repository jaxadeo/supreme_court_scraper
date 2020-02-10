import requests
from bs4 import BeautifulSoup as bs


def case_scraper(url):
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    return soup.find('div', class_='caselawcontent').text

print(case_scraper("https://caselaw.findlaw.com/us-supreme-court/16-460.html"))
