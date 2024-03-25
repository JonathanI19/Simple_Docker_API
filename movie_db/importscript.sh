#!/bin/bash

mongoimport --db='movie_db' --collection='names' --file='/tmp/names.json' --jsonArray --username='admin' --password='pass' --authenticationDatabase=admin
mongoimport --db='movie_db' --collection='roles' --file='/tmp/roles.json' --jsonArray --username='admin' --password='pass' --authenticationDatabase=admin
mongoimport --db='movie_db' --collection='titles' --file='/tmp/titles.json' --jsonArray --username='admin' --password='pass' --authenticationDatabase=admin