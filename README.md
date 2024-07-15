# DRFUniversite
Description : UniverSite est un site web qui regroupe les univérsités de Madagascar afin que les futurs étudiants puissent trouver leur voie dans l'enseigenemt supérieur.
Ce projet gère le coté back-end du site notament la connexion , le crud de l'user ainsi que des models : Parcours et Filière des universités. 

#Installation
NB : Assuer vous que votre environnement virtuel soit activé.
Après avoir cloner le projet: 
  -Créer un environnement virtuel et installer les dépendances avec la commande pip install -r requierements.txt
  - Configurer la base de données avec la commande " python manage.py migrate"
  - Créer un super utilisateur
  - Lancer le serveur avec la commande "python manage.py runserver"

#Les endpoints des API
 -> les points de l'application UserApp
   Note: Ajouter /users/ avant d'écrire les endpoints ( exemple: http://127.0.0.1:8000/users/)
      "" : Liste des users affichée en fomat JSON
      -"<pk>/" : Detail sur un utilisateur
      -"<pk>/update/" : pour modifier les info sur un utilisateur 
      -update-password/<pk>/" : pour mettre à jour le mot de passe d'un user
     -"create/" : pour créer un utilisateur
     -"token/" : pour obtenir le JWT 
     -"token/refresh/" : pour obtenir un nouveau jeton après expiration 
     -"logout/" : pour se déconnecter
     
     
     
     
     
     
 





