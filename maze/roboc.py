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
mazes = initMazes()

# Fonction d'introduction du jeu
pseudo = intro()

# On récupère le labyrinthe de la partie
maze = verifSvg(pseudo,mazes) 

# On boucle tant que le joueur ne décide pas d'arrêter
while 1:
	"""
		On commence par sauvergarder la partie, ce sera le cas à chaque fois que le joueur fera une action sauf quitter
		On affiche la grille.
		On propose au joueur de se déplacer
		On résoud le "coup"
			> On boucle
			< On sort
	"""
	svg(pseudo, maze)

	resolution = action(pseudo, maze)
	
	if resolution == "quit":
		print("A bientôt {}".format(pseudo))
		break

# Si on est ici c'est que le joueur a décidé d'arrêter
svg(pseudo, maze)


