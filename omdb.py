# -*- coding: utf-8 -*-

import requests
import datetime
import os
from dotenv import load_dotenv
load_dotenv()

from movie import Movie
from person import Person
from tmdb import Tmdb

OMDB_API_KEY = os.getenv('OMDB_API_KEY')


class Omdb(object):

    def __init__(self):
        self.imdb_id = None
        self.r_search = None


    @staticmethod
    def get_movies(id):
        r = requests.get(f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={id}', headers = {"Accept-Language": "fr-FR"}).json()
        return Movie(   
                    title=r['Title'],
                    duration=r['Runtime'].split(' ')[0],
                    imdb_id=r['imdbID'],
                    synopsis=r['Plot'],
                    release_date=datetime.datetime.strptime(r['Released'], "%d %b %Y").strftime("%Y-%m-%d"),
                    actors=r['Actors'],
                    productors=r['Production'],
                    directors=r['Director']
                    )


    @staticmethod
    def get_people(fullname):
        print("On passe quand même par TMDB parce qu'on peut pas chercher des personnes sur OMDB (:>*")
        return Tmdb.get_people(fullname)


    @classmethod
    def get_rating(r):
        if r['Rated'] in ["PG-13"]:
            pass
