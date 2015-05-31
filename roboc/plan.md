Version 31/05
le labyrinthe initial :
  roboc.py
  roboc_class.py
  roboc_fonc.py
  
La version client/server, multijoueur.
les fichiers de la nouvelle version sont :
  roboc_server.py
  roboc_server_class.py
  roboc_server.py
  roboc_server_class.py
  
fonctionnement extimé pour la nouvelle version :
  client:
    affichage de carte
    envoi de l'ordre de mouvement
    réception nouvelle carte depuis server
    affichage interface
  server:
    réception de l'ordre de mouvement
    calcul de validité de la nouvelle position
    mise à jour de la carte
    envoi de la carte aux clients
    gestion des connexions (max 4 joueurs)
    
Non précisé dans l'exercice mais qui sera implémenté, le premier joueur choisi la carte dans la liste présente sur le serveur.
