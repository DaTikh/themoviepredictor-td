import requests

import os
from dotenv import load_dotenv
load_dotenv()

OMDB_API_KEY = os.getenv('OMDB_API_KEY')

class Omdb:

    # def __init__(self):
    #     self.r_type = None
    #     self.r_imdb_id = None
    #     self.r_search = None

    def get_movie(id):
        r = requests.get(f'http://www.omdbapi.com/?i={id}&apikey={OMDB_API_KEY}')
        return r.json()