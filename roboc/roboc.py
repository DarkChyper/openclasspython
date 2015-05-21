#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
Labyrinthe pour TP openclassroom
"""
# permet entre autre l'enregistrement d'objet directement récupérables dans un fichier
import pickle
from roboc_class import *
from roboc_fonc import *

#tentative de récupération des scores d'une précédente partie
try:
    with open("scores", "rb") as Scores:
        try:
            mon_depickler = pickle.Unpickler(Scores)
            svgpartie = mon_depickler.load()
        except: #pas de sauvegarde en cours
            svgpartie = svg()
except: #si le fichier est corrompu au point de ne pas pouvoir le lire ou n'existe pas
            svgpartie = svg()

intro()
aide()

if svgpartie.carte == None:
    svgpartie = choixcarte(svgpartie) #fonction du menu de choix de carte

svgpartie = affichcarte_init(svgpartie) #fonction d'affichage de la carte
mvt = ""
    
while svgpartie.victoire == False and mvt.upper() != "QUIT": #définir les critères de fin de partie victoire ou ordre quit
    """
    3 types d'entrée
        direction + chiffre pour mvt robot
        "quit" pour quitter la partie
        "help" pour rappeler les commandes
    """
    mvt = input("dans quelle direction se déplacer? ") #prévoir des sécurités pour entrée débile
    
    if mvt.upper() == "HELP":
        aide()
        continue
    elif mvt.upper() == "QUIT":
        continue

    if len(mvt) == 1:
        svgpartie = mouvement(svgpartie, mvt)
    elif len(mvt) > 1:
        svgpartie = mouvementlong(svgpartie, mvt)

    affichecarte(svgpartie)

    svgpartie.save()


if svgpartie.victoire == True:
    svgpartie.clear()

svgpartie.save()
