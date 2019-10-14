import requests
from bs4 import BeautifulSoup

page = requests.get("https://fr.wikipedia.org/wiki/Matrix_(film)")

soup = BeautifulSoup(page.content, 'html.parser')

title_div = soup.find(id="firstHeading")
title = list(title_div.children)[0].get_text()

original_title_div = soup.find(class_="infobox_v3")
list(original_title_div)[8]