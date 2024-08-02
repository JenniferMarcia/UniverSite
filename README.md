# UniverSite

UniverSite est une application web qui centralise les informations sur les universités à Madagascar, permettant aux futurs étudiants de naviguer et de choisir leur parcours d'enseignement supérieur. Ce projet gère le backend de l'application, y compris la gestion des utilisateurs, l'authentification, et les modèles de données pour les parcours et les filières universitaires.

# Installation

Après avoir cloné le projet:

- Créer un environnement virtuel que ce soit en utilisant virtualenv : python -m venv nom_env ou bien conda: condacreate -n nom_env , puis activez-le
- Installer les dépendances avec la commande pip install -r requierements.txt
- Créer un fichier .env et ajouter à l'intérieur : SECRET_KEY = ""
- Configurer la base de données avec la commande " python manage.py migrate"
- Lancer le serveur avec la commande: python manage.py runserver

# Les endpoints de l'API

- /users/:
    GET: Liste tous les utilisateurs au format JSON.
- /users/<pk>/:
    GET : Affiche les détails d'un utilisateur spécifique (remplacez <pk> par l'ID de l'utilisateur).
- /users/<pk>/update/:
    PUT: Permet de modifier les informations d'un utilisateur (remplacez <pk> par l'ID de l'utilisateur).
- /users/update-password/<pk>/:
    PUT: Permet de mettre à jour le mot de passe d'un utilisateur (remplacez <pk> par l'ID de l'utilisateur).
- /users/create/:
    POST: Permet de créer un nouvel utilisateur.
- /users/token/:
    POST: Permet d'obtenir un token JWT pour l'authentification.
- /users/token/refresh/:
    POST: Permet d'obtenir un nouveau token JWT après expiration du jeton actuel.
- /users/logout/:
    POST: Permet de se déconnecter de l'application.

NB :Assurez-vous d'ajouter /users/ avant d'appeler les endpoints Users.
    Pour les requêtes PUT, envoyez les données à modifier au format JSON dans le corps de la requête.

# API Documentation

- Les endpoints des Api doc sont :
    /swagger.json : affiche une  vue __JSON__  de l'API
    /swagger.yaml : affiche une  vue __YAML__ de l' API
   /swagger/ : affiche vue __swagger-ui__ de l' API  
    /redoc/ : affiche une vue  __ReDoc__ de l'API