#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TheMoviePredictor script
Author: Arnaud de Mouhy <arnaud@admds.net>
Contributor: Baptiste Rogeon <baptiste.rogeon@gmail.com>
"""

import mysql.connector
import sys
import argparse
import csv
import re
import imdb_scrappper

import _parser as ps

from movie import Movie
from omdb import Omdb

parser = ps.Parser()

def args_sanitizer(args):
    context, action = args.context, args.action
    k, v = [*vars(args)], [*vars(args).values()]
    k.remove('context'), k.remove('action'), v.remove(context), v.remove(action)
    return k, v, context, action

def insert_query(args):
    k, v, context, action = args_sanitizer(args)
    keys = list()
    values = list()
    for x in k:
        keys.append(x)
    for x in v:
        if x == None:
            values.append('NULL')
        elif re.search("[a-zA-Z-]", x):
            values.append("'"f"{x}""'")
        elif re.search("[0-9]", x):
            values.append(x)
    return (f"INSERT INTO {context} ({', '.join(keys)}) VALUES ({', '.join(values)})")

def insert_from_IMDB(args, title, original_title, rating, duration, release_date):
    cnx = connect_to_database()
    cursor = create_cursor(cnx)
    cursor.execute(f"INSERT INTO `{args.context}` (`title`, `original_title`, `rating`, `duration`, `release_date`) VALUES ('{title}', '{original_title}', '{rating}', {duration}, {release_date})")
    cnx.commit()
    close_cursor(cursor)
    disconnect_database(cnx)

def insert(args):
    cnx = connect_to_database()
    cursor = create_cursor(cnx)
    cursor.execute(insert_query(args))
    cnx.commit()
    close_cursor(cursor)
    disconnect_database(cnx)

def import_csv(args):
    with open(args.file, 'r', encoding='utf-8', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            row = dict(row)
            row.update({'context': args.context, 'action': args.action})
            row = (argparse.Namespace(**row))
            insert(row)

def print_person(person):
    print("#{}: {} {}".format(person['id'], person['firstname'], person['lastname']))

def print_movie(movie):
    print("#{}: {} released on {}".format(movie['id'], movie['title'], movie['release_date']))

# context_parser = argparse.ArgumentParser(description="Context parser", add_help=False)
# context_parser.add_argument('context', choices=['people', 'movies'], help='Le contexte dans lequel nous allons travailler', nargs="?")

# context_args, unknown_args = context_parser.parse_known_args()

# parser = argparse.ArgumentParser(parents=[context_parser], description='Process MoviePredictor data')

# action_subparser = parser.add_subparsers(title='action', dest='action')

# list_parser = action_subparser.add_parser('list', help='Liste les entités du contexte')
# list_parser.add_argument('--export', help='Chemin du fichier exporté')

# find_parser = action_subparser.add_parser('find', help='Trouve une entité selon un paramètre')
# find_parser.add_argument('id', help='Identifant à rechercher')

# import_parser = action_subparser.add_parser('import', help='Importe un fichier CSV dans la base de données')
# import_parser.add_argument('--file', help='Chemin du fichier à importer')
# api_parser = import_parser.add_argument('--api', help="Choix de l'API à contacter")
# api_parser.add_argument('id', help='Identifiant à rechercher')

# insert_parser = action_subparser.add_parser('insert', help='Insère une entrée dans la base de données')

# scrap_parser = action_subparser.add_parser('scrap', help='Insère un film depuis IMDB')
# scrap_parser.add_argument('--url', help='URL du film sur IMDB', required=True)

# if context_args.context == "people":
#     insert_parser.add_argument('--firstname', help='Prénom')
#     insert_parser.add_argument('--lastname', help='Nom de famille')
# elif context_args.context == "movies":
#     insert_parser.add_argument('--title', help='Titre du film', required=True)
#     insert_parser.add_argument('--duration', help='Durée du film', required=True)
#     insert_parser.add_argument('--original-title', help='Titre original', required=True)
#     insert_parser.add_argument('--origin-country', help='Pays d\'origine', required=True)
#     insert_parser.add_argument('--rating', help='Classification', default='TP')
#     insert_parser.add_argument('--release-date', help="Date de sortie, AAAA-MM-JJ")

# args = parser.parse_args()

# if args.action == "insert":
#     insert(args)
# if args.action == "import":
#     import_csv(args)
# if args.action == "scrap":
#     insert_from_IMDB(args, *imdb_scrappper.perform(args.url))

# if args.context == "people":
#     if args.action == "list":
#         people = find_all("people")
#         if args.export:
#             with open(args.export, 'w', encoding='utf-8', newline='\n') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow(people[0].keys())
#                 for person in people:
#                     writer.writerow(person.values())
#         else:
#             for person in people:
#                 print_person(person)
#     if args.action == "find":
#         peopleId = args.id
#         people = find("people", peopleId)
#         for person in people:
#             print_person(person)

# elif args.context == "movies":
#     if args.action == "list":
#         movies = find_all("movies")
#         for movie in movies:
#             print_movie(movie)
#     if args.action == "find":
#         movieId = args.id
#         movies = find("movies", movieId)
#         for movie in movies:
#             print_movie(movie)

# print(Omdb.get_movie("tt3896198"))