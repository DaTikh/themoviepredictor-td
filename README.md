# The Movie Predictor


## Cher lecteur, je te remercie d'avance du temps précieux que tu passeras à tester ce petit script, have fun ! ;)


## Pré-requis et installation :

Pour cloner le repo sur ta machine :

```
  $ git clone https://github.com/DaTikh/themoviepredictor-td.git
```

    - Ensuite il te faudra lancer les containers depuis le dossier avec Docker :

```
  $ docker-compose up -d
```

    - Librairies utilisées :

```
  $ pip install argparse && pip install requests && pip install bs4
```

    - Puis rendez-vous sur ton web browser préféré à l'adresse :

 ```
   @ http://localhost:8080/
 ```

Une fois sur l'interface d'Adminer, connecte toi sur la database avec les identifiants suivants :

```
Server : themoviepredictor-td_database_1
User: predictor
Password : predictor
Database : predictor
```

Une fois connecté clique sur **Import**, puis sélectionne le fichier *TheMoviePredictor_create.sql*.
Félicitations, tu viens de créer et peupler la database !

*NOTA : $ = bash || @ = web browser*


## Les commandes qui vont bien pour s'amuser :

Dans ton bash tu peux tester le script avec par exemple les commandes suivantes...

```
  $ python app.py people insert --firstname "John" --lastname "Doe"
  $ $ python app.py movies insert --title "Star Wars, épisode VIII : Les Derniers Jedi" --duration 152 --original-title "Star Wars: Episode VIII – The Last Jedi" --origin-country US
  $ python app.py movies import --file new_movies.csv
  $ python app.py people list
  $ python app.py movies list
```

Normalement ça doit faire des trucs super cools, tu m'en diras des nouvelles !


## Versions

**Python 3.7.4**

**MySQL 8.0.17**

**Docker 19.03.2**


## Contributeurs

@Baptiste.R - Baptiste Rogeon, pour vous servir !