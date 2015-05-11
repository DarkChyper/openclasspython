#!/usr/python3.4
# -*-coding:utf_8 -*

from donnee import *
from fonctions import *

""" pendu.py est un simple jeu de pendu en ligne de commande
	Le joueur renseigne son pseudo et essaye de trouver les mots
	proposés par l'ordinateur, lettre par lettre, en moins de 
	8 tentatives sinon il est "pendu" 
"""

""" Déclaration des variables
"""
# Initialisation du dictionnaire des scores
scores = dict()

""" Main
"""
print("Bienvenue dans le jeu de pendu.\n")

# On demande au joueur de renseigner son nom/pseudo
pseudo = askName()

# Vérification de la présence du fichier des scores 
# et de la présence du joueur ou non
scores = initScores(pseudo)
affPlayerScores(scores, pseudo)