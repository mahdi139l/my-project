import requests
from bs4 import BeautifulSoup
import pandas

dolor_url = "https://www.tgju.org/%D9%82%DB%8C%D9%85%D8%AA-%D8%AF%D9%84%D8%A7%D8%B1"
data = requests.get(dolor_url).content

doc = BeautifulSoup(data, "html.parser")

dolor = float(doc.td.string.replace(",", ""))


COIN_TODAY = []

url = "https://coinmarketcap.com/"
data = requests.get(url).content

doc = BeautifulSoup(data, "html.parser")

tbody = doc.tbody.contents[:10]
for tr in tbody:
    temp = {}
    coin = tr.contents[2].p.string
    price = float(tr.contents[3].span.string.replace("$", "").replace(",", ""))
    temp["title"] = coin
    temp["dolor"] = price
    temp["rial"] = f"{(price * dolor):,}"
    COIN_TODAY.append(temp)

for item in COIN_TODAY:
    print(item)


df = pandas.DataFrame(COIN_TODAY)

df.to_excel("coin.xlsx")