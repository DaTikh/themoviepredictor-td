# -*- coding: utf-8 -*-

import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

from movie import Movie
from person import Person

TMDB_API_KEY = os.getenv('TMDB_API_KEY')


class Tmdb(object):

    def __init__(self):
        self.imdb_id = None
        self.r_search = None


    @staticmethod
    def get_movies(id):
        r = requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}&language=fr_FR').json()
        return Movie(   
                    title=r['title'],
                    duration=r['runtime'],
                    imdb_id=r['imdb_id'],
                    original_title=r['original_title'],
                    production_budget=r['budget'],
                    synopsis=r['overview'],
                    release_date=datetime.datetime.strptime(r['release_date'], "%Y-%m-%d").strftime("%Y-%m-%d"),
                    productors=Tmdb.get_productors(r)
                    )


    @staticmethod
    def get_people(fullname):
        search_query = fullname.casefold().replace(' ', '+')
        r = requests.get(f'https://api.themoviedb.org/3/search/person?query={search_query}&api_key={TMDB_API_KEY}', headers = {"Accept-Language": "fr-FR"}).json()
        if r['results']:
            r = r['results'][0]
            r = requests.get(f"https://api.themoviedb.org/3/person/{r['id']}?api_key={TMDB_API_KEY}", headers = {"Accept-Language": "fr-FR"}).json()
            return Person(
                        imdb_id=r['imdb_id'],
                        firstname=r['name'].split(' ')[0],
                        lastname=r['name'].split(' ')[-1]
                        )
        else:
            print("Pas de résultat.")
            exit()


    @classmethod
    def get_productors(self, request):
        productors = []
        for producer in request['production_companies']:
            productors.append(producer['name'])
        return ', '.join(productors)