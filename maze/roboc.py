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
cartes = initCartes()
for x in range(len(cartes)):	
	print cartes[x]
# Fonction d'introduction du jeu
pseudo = intro()

verifSvg(pseudo)