ToDo :
 - Générer le robot à sa connexion et non au début de la partie
 - Envoyer la carte à la connexion du client
 - Créer un objet connexion qui gèrera entièrement le côté réseau
 - Documenter toutes les fonctions
 - Remettre à niveau les objets Map et Joueur
 - Purifier le code en général
 - Centraliser les Exceptions

Exigences :
OK :
 - Client/serveur
 - Tour par tour
 - Tkinter

KO :
 - Murer et percer des portes
 - Tests unitaires

Bugs :
 - Il est toujours possible de se connecter après le début de la partie
    --> Mettre un timeout pendant l'obtention de l'ID (étape à laquelle il bloque)
        "La partie a déjà commencée ou le serveur est inaccessible"
 - Un des clients ne voit que des 'X' pour tous les joueurs (potentiellement tous les joueurs sauf le dernier connecté)
 - Le message n'est pas mis à jour lorsque ce n'est plus au joueur de jouer
 - Le nombre de connexions n'est pas limité à 4