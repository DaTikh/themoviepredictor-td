import csv
import json
from database import Db


class Factory():

    def __init__(self):
        self.task = None

    def _export_csv(self, data, filepath): 
        with open(filepath, 'w', encoding='utf-8', newline='\n') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(data[0].keys())
            for result in data:
                writer.writerow(result.values())

    def _export_json(self, data, filepath):
        with open(filepath, "w", encoding='utf-8') as write_file:
            json.dump(data, write_file, ensure_ascii=False, default=str)