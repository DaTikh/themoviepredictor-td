import csv
import json
from database import Db
import pandas as pd

class Factory():

    def __init__(self):
        self.task = None

    @staticmethod
    def _export_csv(data, filepath): 
        with open(filepath, 'w', encoding='utf-8', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data[0].keys())
            for result in data:
                writer.writerow(result.values())

    @staticmethod
    def _export_json(data, filepath):
        with open(filepath, "w", encoding='utf-8') as write_file:
            json.dump(data, write_file, ensure_ascii=False, default=str)

    @staticmethod
    def _import_csv(context, file):
        with open(file, 'r', encoding='utf-8', newline='\n') as csvfile:
            reader = csv.DictReader(csvfile)
            print("Pour l'instant on affiche juste le contenu du fichier sans l'insérer.")
            for row in reader:
                row = dict(row)
                print(row)

    @staticmethod
    def _import_tsv(context, file):
        with open(file, 'r', encoding='utf-8') as tsvfile:
            f = csv.DictReader(tsvfile, dialect='excel-tab')
            df = pd.DataFrame.from_dict(f, dtype=str)
            df.rename(columns={'tconst': 'imdb_id', 'averageRating': 'public_note', 'numVotes': 'public_votes'})
