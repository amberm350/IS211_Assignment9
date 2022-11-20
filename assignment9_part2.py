import requests
from bs4 import BeautifulSoup


def download(url):
    
    return requests.get(url).text

if __name__ == "__main__":
    wiki_url = "https://en.wikipedia.org/wiki/List_of_Super_Bowl_champions"
    url_text = download(wiki_url)

    
    soup = BeautifulSoup(url_text, features="html.parser")

    result_table = soup.find_all('table', class_="wikitable sortable")
    rows = result_table[0].find_all('tr')
    headers = rows[0].find_all('th')
    print(
        f"{headers[1].text.strip():<15} - {headers[2].text.strip():<30} - {headers[3].text.strip():<15}"
    )
    for row in rows:
        cells = row.find_all('td')
        if not cells:
            continue
        print(
            f"{cells[0].text.strip():<15} - {cells[1].text.strip():<30} - {cells[2].text.strip():<15}"
        )