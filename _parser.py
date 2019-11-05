import sys
import argparse

from person import Person
from movie import Movie
import database

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
        

    def _find(self):
        parser = argparse.ArgumentParser(
            description="Find an item by its id")
        parser.add_argument('id', help='Id to find')
        args = parser.parse_args(sys.argv[3:])
        if self.context == "movies":
            print(f'Searching for the movie with the id: {args.id}')
            db.find_movie(args)
        else:
            print(f'Searching for the person with the id: {args.id}')
            db.find_person(args)
  

    def _list(self):
        # db = database.Db()
        parser = argparse.ArgumentParser(
            description='''List all the items of the given context:
    -  directly in the console
    -  export in a CSV/JSON file
    ''')
        parser.add_argument('--export', help='File path for the export')
        args = parser.parse_args(sys.argv[3:])
        if args.export:
            if args.export.endswith('.csv'):
                self.db._export_csv(table=self.context, filepath=args.export)
            elif args.export.endswith('.json'):
                self.db._export_json(table=self.context, filepath=args.export)
        else:
            results = self.db._list(table=self.context)
            for result in results:
                print(result)

    def _insert(self):
        parser = argparse.ArgumentParser(
            description="Insert an item of the given context in the databse")
        if self.context == "movies":
            parser.add_argument('--title', help='Titre du film', required=True)
            parser.add_argument('--duration', help='Durée du film', required=True)
            parser.add_argument('--original-title', help='Titre original', required=True)
            parser.add_argument('--origin-country', help='Pays d\'origine', required=True)
            parser.add_argument('--rating', help='Classification', default='TP')
            parser.add_argument('--release-date', help="Date de sortie, AAAA-MM-JJ")
            args = parser.parse_args()
            movie = Movie(title=args.title, original_title=args.original_title, duration=args.duration, rating=args.rating, release_date=args.releasedate)
            # movie_id = insert_movies(movie)
            print(f"Nouveau film inséré avec l'id {movie_id}")
        else: 
            parser.add_argument('--firstname', help='Prénom', required=True)
            parser.add_argument('--lastname', help='Nom de famille', required=True)
            person = Person(firstname=args.firstname, lastname=args.lastname)
            # person_id = insert_person(person)
        args = parser.parse_args(sys.argv[3:])
        print(args)


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

        parser.add_argument('--api', help="Name of the API (omdb/themoviedb)")
        parser.add_argument('--imdbId', help="Id on IMDB")
        parser.add_argument('--file', help="File path")
        args = parser.parse_args(sys.argv[3:])
        # if args.api in ['omdb', 'themoviedb'] and args.imdbId:
            
        # elif args.file:
        
if __name__ == '__main__':
    Parser()