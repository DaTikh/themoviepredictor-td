import requests
from datetime import datetime
from bs4 import BeautifulSoup

def perform(url):
    page = requests.get(url, headers={"Accept-Language": "fr-fr"})

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(class_="title_wrapper").find("h1").contents[0].strip()

    info_list = soup.find(class_="title_wrapper").find("h1").find_next_sibling(class_="subtext").contents

    rating = "TP"
    if info_list[0].strip().isdecimal():
        rating = f"-{info_list[0].strip()}"
    elif info_list[0].strip() == "Tous publics":
        rating = "TP"
    else:
        # rating = None
        duration_object = info_list[1].get_text().strip()

    if duration_object == None:
        duration_object = info_list[3].get_text().strip()
    duration_hours = int(datetime.strftime(datetime.strptime(duration_object, "%Ih %Mmin"), "%I"))
    duration_minutes = int(datetime.strftime(datetime.strptime(duration_object, "%Ih %Mmin"), "%M"))
    duration = (duration_hours * 60) + duration_minutes

    release_date = (datetime.strftime(datetime.strptime(info_list[-2].get_text().strip(), "%d %B %Y (France)"), "'%Y-%m-%d'"))

    if soup.find(class_="originalTitle").contents[0].strip():
        original_title = soup.find(class_="originalTitle").contents[0].strip()
    else:
        original_title = title

    return title, original_title, rating, duration, release_date