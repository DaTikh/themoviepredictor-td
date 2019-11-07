import requests

import datetime

import os
from dotenv import load_dotenv
load_dotenv()

from movie import Movie

OMDB_API_KEY = os.getenv('OMDB_API_KEY')

class Omdb(object):

    def __init__(self):
        self.imdb_id = None
        self.r_search = None

    @staticmethod
    def get_movie(id):
        r = requests.get(f'http://www.omdbapi.com/?apikey={OMDB_API_KEY}&i={id}').json()
        return Movie(   
                    title=r['Title'],
                    duration=r['Runtime'].split(' ')[0],
                    imdb_id=r['imdbID'],
                    plot=r['Plot'],
                    release_date=datetime.datetime.strptime(r['Released'], "%d %B %Y").strftime("%Y-%m-%d")
                    )