#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# Imports externes
import os
import sys
import socket
import select

# Imports internes
from .serv_class import *

"""
	serv_function.py contient les fonctions basiques du serveur
"""

def initGame():
	""" On initilise le jeu en demandant de choisir la carte à jouer"""
	mazes = initMazes()
	print("Voici la liste des labyrinthes disponibles :")
	x = 1
	liste = list()
	for maze in range(len(mazes)):
		print(" {}. {}".format(x, mazes[maze].nom))
		liste.append(str(x))
		x += 1

	while 1:
		choix = input("Quel Labyrinthe voulez-vous résoudre ? ")
		if choix in liste:
			return mazes[int(choix)-1]


def initMazes():
	""" 
		On récupère les cartes au format txt dan le dossier ./maze_cartes
		On les charge dans le jeu sous forme d'une liste d'objets maze
		On retourne cette liste au programme principale
	"""
	mazes = []
	for nom_fichier in os.listdir("maze_cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("maze_cartes", nom_fichier)
			nom_maze = nom_fichier[:-4].lower()
			with open(chemin, "r") as fichier:
				grille = fichier.read()
				maze = Maze(nom_maze,grille)
				mazes.append(maze)
	return mazes

def fermer_programme(signal, frame, connexion_principale):
	""" 
		Gère la fin du progrmme par signla du système.
		envoi un message de clôture aux utilisateurs,
		ferme proprement les connexions

	"""
	# A écrire
	connexion_principale.close()
	sys.exit(0)