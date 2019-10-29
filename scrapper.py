import requests
from bs4 import BeautifulSoup

page = requests.get("https://fr.wikipedia.org/wiki/Joker_(film,_2019)")

soup = BeautifulSoup(page.content, 'html.parser')

title_div = soup.find(id="firstHeading")
title = list(title_div.children)[0].get_text()
print(title)

h2 = soup.find(id="Fiche_technique").parent

fiche_ul = h2.find_next_sibling("ul")

infos = fiche_ul.find_all("li")

for info in infos:
    print(info.text)