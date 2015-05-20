#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
Labyrinthe pour TP openclassroom
"""

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

if svgpartie.carte == None:
    svgpartie = choixcarte(svgpartie) #fonction du menu de choix de carte

svgpartie = affichcarte(svgpartie) #fonction d'affichage de la carte
"""    
while ??: #définir les critères de fin de partie victoire ou ordre quit
    mvt = input("dans quelle direction se déplacer?" ) #prévoir des sécurités pour entrée débile
    
    3 types d'entrée
        direction + chiffre pour mvt robot
        "quit" pour quitter la partie
        "help" pour rappeler les commandes
    """

