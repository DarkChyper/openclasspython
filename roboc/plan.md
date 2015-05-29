Version 29/05
evolution entre le labyrinthe initial
  roboc.py
  roboc_class.py
  roboc_fonc.py
  
et une version client/server, multijoueur.
la séparation entre les 2 version est faite de la façon suivante :
  roboc.py => nouvelle version à partir du commit "début nouvelle version"
  roboc_class.py => nouvelle version à partir du commit "début nouvelle version"
  roboc_fonc.py => nouvelle version à partir du commit "début nouvelle version"
  les autres fichiers sont créés pour l'occasion
  
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
