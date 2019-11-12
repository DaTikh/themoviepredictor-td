# -*- coding: utf-8 -*-

import sys
import argparse

import database

from person import Person
from movie import Movie
from factory import Factory
from omdb import Omdb
from tmdb import Tmdb


class Parser(object):
    
    def __init__(self):
        parser = argparse.ArgumentParser(
            description='TheMoviePredictor by Baptiste Rogeon',
            usage='''app.py <context> <action> [<args>]

The context and action choices are:
    -  contexts : movies, people
    -  actions : find, list, insert, import
''')
        parser.add_argument('context', choices=['movies', 'people'], help="Context in which we will apply the next action")
        parser.add_argument('action', choices=['find', 'list', 'insert', 'import'], help="Action to perform in the given context")
        args = parser.parse_args(sys.argv[1:3])
        self.action = args.action
        self.context = args.context
        self.db = database.Db()
        getattr(self, '_' + args.action)()


    @classmethod
    def second_parser(self, parser):
        return parser.parse_args(sys.argv[3:])


    def _find(self):
        parser = argparse.ArgumentParser(
            description="Find an item by its id")
        parser.add_argument('id', help='Id to find')
        args = self.second_parser(parser)
        results = self.db._find(table=self.context, id=args.id)
        print(results[0])


    def _list(self):
        parser = argparse.ArgumentParser(
            description='''List all the items of the given context:
    -  directly in the console if no arguments
    -  export in a CSV/JSON file (with --export <filepath>)
    ''')
        parser.add_argument('--export', help='File path for the export')
        args = self.second_parser(parser)
        if args.export:
            if args.export.endswith('.csv'):
                results = self.db._list(table=self.context)
                Factory._export_csv(data=results, filepath=args.export)
            elif args.export.endswith('.json'):
                results = self.db._list(table=self.context)
                Factory._export_json(data=results, filepath=args.export)
        else:
            results = self.db._list(table=self.context)
            for result in results:
                print(result)


    def _insert(self):
        parser = argparse.ArgumentParser(
            description="Insert an item of the given context in the databse")
        if self.context == "movies":
            parser.add_argument('--title', help='Titre du film', required=True)
            parser.add_argument('--imdb-id', help='Id sur IMDB', required=True)
            parser.add_argument('--duration', help='Durée du film', required=True)
            parser.add_argument('--original-title', help='Titre original')
            parser.add_argument('--origin-country', help='Pays d\'origine')
            parser.add_argument('--rating', help='Classification', default='TP')
            parser.add_argument('--release-date', help="Date de sortie, AAAA-MM-JJ")
            args = self.second_parser(parser)
            movie = Movie(title=args.title, imdb_id=args.imdb_id, original_title=args.original_title, duration=args.duration, rating=args.rating, release_date=args.release_date)
            movie_id = self.db._insert(table="movies", object=movie)
            print(f"Nouveau film inséré avec l'id {movie_id}")
        else: 
            parser.add_argument('--firstname', help='Prénom', required=True)
            parser.add_argument('--lastname', help='Nom de famille', required=True)
            args = self.second_parser(parser)
            person = Person(firstname=args.firstname, lastname=args.lastname)
            person_id = self.db._insert(table="people", object=person)
            print(f"Nouvelle personne insérée avec l'id {person_id}")


    def _import(self):
        parser = argparse.ArgumentParser(
            description="Select the source to import data from: api, file"
        )

        """  Si on choisit d'obliger la sélection d'une source  """
        # parser.add_argument('source', choices=['api', 'file'], help="Source choice")
        # args = parser.parse_args(sys.argv[3:])
        # if args.source == "api":
        #     parser.add_argument('api_name', help='API name')
        #     parser.add_argument('--imdbId', help="Id on IMDB")

        parser.add_argument('--api', help="Name of the API (omdb/tmdb)")
        parser.add_argument('--imdbId', help="Id on IMDB")
        parser.add_argument('--file', help="File path")
        args = self.second_parser(parser)
        if args.api in ['omdb', 'tmdb'] and args.imdbId:
            if args.api == 'omdb':
                result = getattr(Omdb, 'get_' + self.context)(args.imdbId)
            else:
                result = getattr(Tmdb, 'get_' + self.context)(args.imdbId)
            last_id = self.db._insert(table=self.context, object=result)
            print(f"Last insertion id: #{last_id}.")
            print(f"Inserted object: {vars(result)}")
        elif args.file:
            Factory._import_csv(self.context, args.file)
        else:
            print("Please specify an API (omdb/tmdb) or a filepath.")


if __name__ == '__main__':
    Parser()