# UniverSite

UniverSite est une application web qui centralise les informations sur les universités à Madagascar, permettant aux futurs étudiants de naviguer et de choisir leur parcours d'enseignement supérieur. Ce projet gère le backend de l'application, y compris la gestion des utilisateurs, l'authentification, et les modèles de données pour les parcours et les filières universitaires.

## Installation

Après avoir cloné le projet:

1. **Créer un environnement virtuel** :

   - Avec `virtualenv` :

     ```bash
     python -m venv nom_env
     ```

   - Avec `Conda` :

     ```bash
     conda create -n nom_env
     ```

   Puis activez-le.

2. **Installer les dépendances avec** :

   ```bash
   pip install -r requirements.txt

3. **Créer un fichier .env et ajouter à l'intérieur** :

    - SECRET_KEY = ""

4. **Configurer la base de données avec** :

    ```bash
        python manage.py migrate
    ```

5. **Lancer le serveur avec** :

    ```bash
        python manage.py runserver
    ```

## Les endpoints de l'API

- /users/:
  - GET: Liste tous les utilisateurs au format JSON.
- /users/<pk>/:
  - GET : Affiche les détails d'un utilisateur spécifique (remplacez <pk> par l'ID de l'utilisateur).
- /users/<pk>/update/:
  - PUT: Permet de modifier les informations d'un utilisateur (remplacez <pk> par l'ID de l'utilisateur).
- /users/update-password/<pk>/:
  - PUT: Permet de mettre à jour le mot de passe d'un utilisateur (remplacez <pk> par l'ID de l'utilisateur).
- /users/create/:
  - POST: Permet de créer un nouvel utilisateur.
- /users/token/:
  - POST: Permet d'obtenir un token JWT pour l'authentification.
- /users/token/refresh/:
  - POST: Permet d'obtenir un nouveau token JWT après expiration du jeton actuel.
- /users/logout/:
  - POST: Permet de se déconnecter de l'application.

**NB** :Assurez-vous d'ajouter /users/ avant d'appeler les endpoints Users.
    Pour les requêtes PUT, envoyez les données à modifier au format JSON dans le corps de la requête.

## API Documentation

- Les endpoints des Api doc sont :
    /swagger.json : affiche une  vue **JSON**  de l'API  
    /swagger.yaml : affiche une  vue **YAML** de l' API  
   /swagger/ : affiche vue **swagger-ui** de l' API  
    /redoc/ : affiche une vue  **ReDoc** de l'API
