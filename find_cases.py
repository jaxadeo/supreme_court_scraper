import requests
from bs4 import BeautifulSoup as bs

def find_cases(url):
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')

    descriptions = soup.find_all("td",{"data-label" : "Description" })
    for description in descriptions:
        print(description.text)

find_cases("https://caselaw.findlaw.com/court/us-supreme-court/years/2018")