import requests
from bs4 import BeautifulSoup as bs
import pandas as pd

def find_cases(year):
    url = "https://caselaw.findlaw.com/court/us-supreme-court/years/" + year
    page = requests.get(url)
    soup = bs(page.content, 'html.parser')
    table = soup.find('table', attrs={'class': 'responsive-card-table unstriped'})
    table_heads = table.find_all('th')
    table_rows = table.find_all('tr')
    links = table.find_all('a', href=True)
    links = [link.get("href") for link in links]
    l = []
    for i in range(len(table_rows)):
        td = table_rows[i].find_all('td')
        row = [tr.text for tr in td]
        l.append(row)
    l.pop(0)
    df = pd.DataFrame(l)
    df['Link'] = links
    return(df)

print(find_cases("2018"))