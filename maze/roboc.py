#!/usr/python3.4
# -*- coding: utf8 -*-

"""
	Programme principale du jeu de Labyrinthe pour OpenClassRooms
	Code écrit par Simon Lhoir aka Dark-Chyper
		> Le joueur doit indiquer son pseudonyme, ainsi il peut y 
		  avoir plusieures parties d'enregistrées sur la même
		  machine
"""

# Impoortation des modules nécessaires
import os
from roboc_fct import *

# On importe les cartes existantes
cartes = []
for nom_fichier in os.listdir("cartes"):
	if nom_fichier.endswith(".txt"):
		chemin = os.path.join("cartes", nom_fichier)
		nom_carte = nom_fichier[:-4].lower()
		print(nom_carte)
		print(chemin)
		with open(chemin, "r") as fichier:
			contenu = fichier.read()
			print(contenu)
			print type(contenu)

# Fonction d'introduction du jeu
pseudo = intro()

verifSvg(pseudo)