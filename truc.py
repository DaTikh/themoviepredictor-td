import sys
import argparse

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
        # if not hasattr(self, args.context):
        #     print('Unrecognized context or action')
        #     parser.print_help()
        #     exit(1)
        self.action = args.action
        self.context = args.context
        getattr(self, args.action)()

    def find(self):
        print('truc truc bidule')
        parser = argparse.ArgumentParser(
            description="Find an item by its id")
        parser.add_argument('id', help='Id to find')
        args = parser.parse_args(sys.argv[3:])
        if self.context == "movies":
            print(f'Searching for the movie with the id: {args.id}')
            print(args)
            db.find_movie(args)
        else:
            print(f'Searching for the person with the id: {args.id}')
            db.find_person(args)
    
    def log(self):
        parser = argparse.ArgumentParser(
            description='''List all the items of the given context:
    -  directly in the console
    -  export in a CSV/JSON file
    ''')
        parser.add_argument('--export', help='File path for the export')
        args = parser.parse_args(sys.argv[3:])
        if self.context == "movies":
            print("moviiiiiiiies")
        else:
            print("peeeeople")

    def insert(self):
        parser = argparse.ArgumentParser(
            description="Insert an item of the given context in the databse")
        if self.context == "movies":
            parser.add_argument('--title', help='Titre du film', required=True)
            parser.add_argument('--duration', help='Durée du film', required=True)
            parser.add_argument('--original-title', help='Titre original', required=True)
            parser.add_argument('--origin-country', help='Pays d\'origine', required=True)
            parser.add_argument('--rating', help='Classification', default='TP')
            parser.add_argument('--release-date', help="Date de sortie, AAAA-MM-JJ")
        else: 
            parser.add_argument('--firstname', help='Prénom', required=True)
            parser.add_argument('--lastname', help='Nom de famille', required=True)
        args = parser.parse_args(sys.argv[3:])
        print(args)

    def add(self):
        print('haha')

if __name__ == '__main__':
    Parser()