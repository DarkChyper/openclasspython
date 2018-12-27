#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
Labyrinthe pour TP openclassroom
"""
# permet entre autre l'enregistrement d'objet directement récupérables dans un fichier
import pickle
from roboc_class import *
from roboc_fonc import *

#récupération des scores d'une précédente partie
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

if svgpartie.carte != None: #si une partie existe on propose de la continuer
    restart = ""
    while restart == "":
        restart = input("Voulez vous reprendre la précédente partie? Y/N ")
        if restart.upper() == "N":
            svgpartie.clear()
        elif restart.upper() == "Y":
            pass
        else:
            restart = ""

suite = ""
while suite.upper() != "N": #après une victoire si le joueur veut arrêter
    suite = ""
    if svgpartie.carte == None:
        svgpartie = choixcarte(svgpartie) #fonction du menu de choix de carte
        svgpartie = affichcarte_init(svgpartie) #fonction d'affichage de la carte
    else:
        affichecarte(svgpartie)
        
    mvt = ""

    while svgpartie.victoire == False and mvt.upper() != "QUIT": #on boucle jusqu'à la victoire ou si le joueur demande à arrêter

        mvt = input("dans quelle direction se déplacer? ")
    
        if mvt.upper() == "HELP": #rappel des règles
            aide()
            continue
        elif mvt.upper() == "QUIT": #arrêt volontaire en cours de partie
            suite = "N"
            continue

        #séparation entre mouvement simple et multiple
        if len(mvt) == 1:
            svgpartie = mouvement(svgpartie, mvt)
        elif len(mvt) > 1:
            svgpartie = mouvementlong(svgpartie, mvt)

        affichecarte(svgpartie)

        svgpartie.save()

    if svgpartie.victoire == True: #contrôle de victoire
        print("Félicitations! Vous êtes sorti!")
        svgpartie.clear()
        while suite.upper() != "N" and suite.upper() != "Y": #demande de nouvelle partie
            suite = input("Voulez vous refaire une partie? Y/N ")

svgpartie.save()