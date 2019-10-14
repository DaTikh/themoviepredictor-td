#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
TheMoviePredictor script
Author: Arnaud de Mouhy <arnaud@admds.net>
"""

import mysql.connector
import sys
import argparse
import csv

def connectToDatabase():
    return mysql.connector.connect(user='predictor', password='predictor',
                              host='127.0.0.1',
                              database='predictor')

def disconnectDatabase(cnx):
    cnx.close()

def createCursor(cnx):
    return cnx.cursor(dictionary=True)

def closeCursor(cursor):    
    cursor.close()

def findQuery(table, id):
    return ("SELECT * FROM {} WHERE id = {}".format(table, id))

def findAllQuery(table):
    return ("SELECT * FROM {}".format(table))

def find(table, id):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    query = findQuery(table, id)
    cursor.execute(query)
    results = cursor.fetchall()
    closeCursor(cursor)
    disconnectDatabase(cnx)
    return results

def findAll(table):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    cursor.execute(findAllQuery(table))
    results = cursor.fetchall()
    closeCursor(cursor)
    disconnectDatabase(cnx)
    return results

def insertQuery(context, action, args):
    if context == "people":
        k = "`firstname`, `lastname`"
        v = f"'{args.firstname}', '{args.lastname}'"
    elif context == "movies":
        if action == "insert":
            k = "`title`, `duration`, `original_title`, `origin_country`"
            v = f"'{args.title}', {args.duration}, '{args.original_title}', '{args.origin_country}'"
        elif action == "import":
            k = "`title`, `duration`, `original_title`, `rating`, `release_date`"
            v = f"'{args['title']}', {args['duration']}, '{args['original_title']}', '{args['rating']}', '{args['release_date']}'"
    return (f"INSERT INTO `{context}` ({k}) VALUES ({v})")

def insert(context, action, args):
    cnx = connectToDatabase()
    cursor = createCursor(cnx)
    cursor.execute(insertQuery(context, action, args))
    cnx.commit()
    closeCursor(cursor)
    disconnectDatabase(cnx)

def import_csv(args):
    with open(args.file, 'r', encoding='utf-8', newline='\n') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            insert("movies", "import", row)

def printPerson(person):
    print("#{}: {} {}".format(person['id'], person['firstname'], person['lastname']))

def printMovie(movie):
    print("#{}: {} released on {}".format(movie['id'], movie['title'], movie['release_date']))


parser = argparse.ArgumentParser(description='Process MoviePredictor data')

parser.add_argument('context', choices=['people', 'movies'], help='Le contexte dans lequel nous allons travailler')

action_subparser = parser.add_subparsers(title='action', dest='action')

list_parser = action_subparser.add_parser('list', help='Liste les entités du contexte')
list_parser.add_argument('--export' , help='Chemin du fichier exporté')

find_parser = action_subparser.add_parser('find', help='Trouve une entité selon un paramètre')
find_parser.add_argument('id' , help='Identifant à rechercher')

insert_parser = action_subparser.add_parser('insert', help='Insère une entrée dans la base de données')
insert_parser.add_argument('--firstname', help='Prénom')
insert_parser.add_argument('--lastname', help='Nom de famille')
insert_parser.add_argument('--title', help='Titre du film')
insert_parser.add_argument('--duration', help='Durée du film')
insert_parser.add_argument('--original-title', help='Titre original')
insert_parser.add_argument('--origin-country', help='Pays d\'origine')

import_parser = action_subparser.add_parser('import', help='Importe un fichier CSV dans la base de données')
import_parser.add_argument('--file', help='Chemin du fichier à importer')

args = parser.parse_args()

if args.context == "people":
    if args.action == "list":
        people = findAll("people")
        if args.export:
            with open(args.export, 'w', encoding='utf-8', newline='\n') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(people[0].keys())
                for person in people:
                    writer.writerow(person.values())
        else:
            for person in people:
                printPerson(person)
    if args.action == "find":
        peopleId = args.id
        people = find("people", peopleId)
        for person in people:
            printPerson(person)
    if args.action == "insert":
        insert("people", "insert", args) 


if args.context == "movies":
    if args.action == "list":  
        movies = findAll("movies")
        for movie in movies:
            printMovie(movie)
    if args.action == "find":  
        movieId = args.id
        movies = find("movies", movieId)
        for movie in movies:
            printMovie(movie)
    if args.action == "insert":
        insert("movies", "insert", args)
    if args.action == "import":
        import_csv(args)