import requests
from bs4 import BeautifulSoup

link = "https://www.kabum.com.br/computadores/notebooks"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.203"} 
site = requests.get(link, headers=headers)
soup = BeautifulSoup(site.text, "html.parser")
page = soup.findAll('a', class_="page")
last_page = page[9].get_text().strip()

for i in range(1,int(last_page)+1):
    url_page = f'https://www.kabum.com.br/computadores/notebooks?page_number={i}'
    site = requests.get(url_page, headers=headers)
    soup = BeautifulSoup(site.text, "html.parser")
    notes = soup.find_all("div", class_="hJDLPs")

    with open ('notes_prices.csv', 'a', newline='',encoding='UTF-8') as f:
        for note in notes:

            name = note.find('span', class_="nlmfp").get_text().strip()
            try:
                price = note.find('span', class_="priceCard").get_text().strip()

            except:
                price = '0'

            row = name + '; ' + price + '\n'
            print(row)
            f.write(row)
        print(url_page)