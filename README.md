# The Movie Predictor


## Cher lecteur·ice, je te remercie d'avance du temps précieux que tu passeras à tester ce petit script, have fun ! ;)


## Pré-requis et installation :

Pour cloner le repo sur ta machine :

```
  $ git clone https://github.com/DaTikh/themoviepredictor-td.git
```

Ensuite il te faudra renommer le fichier `sample.env` en `.env` et y renseigner tes clés d'API, ainsi que les valeurs des variables d'environnement de ton choix.

Enfin, tu pourras lancer le script à l'aide de la commande suivante :

```
  $ docker-compose up
```

Docker lancera les containers, attendra que la database soit online puis cherchera un film via l'API d'Omdb, l'enregistrera en mémoire et affichera la dernière entrée avant de se fermer.

## Les commandes qui vont bien pour s'amuser :

En utilisant le fichier `docker-compose.override.yml` (une fois renommé comme tel) tu peux tester le script dans ton bash avec par exemple les commandes suivantes...

```
  $ docker-compose exec app bash
  # python app.py movies import --api omdb --imdbId tt0338013
  # python app.py people import --api tmdb --name "José Garcia"  
  # python app.py movies import --file new_movies.csv
  # python app.py people list --export people_list.json
  # python app.py movies list --export movie_list.csv
  # python app.py people list
```

Normalement ça doit faire des trucs super cools, tu m'en diras des nouvelles !


## Versions

**Python 3.7.4**

**MySQL 8.0.17**

**Docker 19.03.5**


## Auteur

@Baptiste.R - Baptiste Rogeon, pour vous servir !

*NOTA : $ = bash || # = root*