#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Module comprenant les fonctions principales du serveur
"""

# Imports internes
from .serv_class import *

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
			Data.maze = mazes[int(choix)-1]
			break


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


def majPseudo(self, client, pseudo):
	"""Fonction pour mettre a jour le pseudo d'un joueur"""
	for i in Data.connectes :
		if Data.connectes[i][0] == client:
			Data.connectes[i][1] = pseudo
			break