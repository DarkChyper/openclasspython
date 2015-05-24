#!/usr/python3.4
# -*- coding: utf8 -*-

"""
	Fichier contenant les fonction nécessaires au jeu de 
	labyrinthe pour OpenClassRooms
"""

import os
import pickle
from roboc_cls import *

"""
	Maze est une class qui crée l'objet Maze
	mazes est une liste contenant des objets Maze
	maze est un objet de type Maze
"""

def initMazes():
	""" 
		On récupère les cartes au format txt dan le dossier ./cartes
		On les charge dans le jeu sous forme d'une liste d'objets maze
		On retourne cette liste au programme principale
	"""
	mazes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("cartes", nom_fichier)
			nom_maze = nom_fichier[:-4].lower()
			with open(chemin, "r") as fichier:
				grille = fichier.read()
				# On va construire l'objet Maze à partir
				# du nom de la carte, de son chemin d'accès et de son contenu
				mazes.append(Maze(nom_maze,chemin,False,grille))
	return mazes

def intro():
	"""
		Affichage de l'introduction du jeu
		qui pourra être étoffée par la suite
	"""
	print("Bienvenue dans le labyrinthe !")
	return askName()

def askName():
	"""
		Demande du pseudonyme au joueur 
		et le retourne si celui-ci est non nul ET plus petit que 20 caratères
	"""
	while 1:
		try:
			pseudo = raw_input("Quel est votre nom/Pseudo ? ")
			assert pseudo <> "" and len(pseudo) < 20 
		except AssertionError:
			print("Votre pseudo ne peut être vide et doit faire moins de 20 caractères")
		else:
			return pseudo

def verifSvg(pseudo,mazes):
	"""
		Vérifie la présence d'un éventuel fichier "pseudo.maze" 
			> Charge le fichier si il le trouve,
			> Demande de choisir un labyrinthe si il n'en trouve pas
			  ou si le joueur a sauvegardé à la fin d'un labyrinthe.
			> Sauvegarde la parie 
			> retourne le labyrinthe en cours
	"""
	fichier = pseudo + ".maze"
	try:
		with open(fichier, 'rb') as monFichier:
			mazeDico = pickle.Unpickler(monFichier)
			maze = Maze(mazeDico['nom'],mazeDico['path'],mazeDico['door'],mazeDico['grille'])
			print("Reprise de la partie sauvegardée.")
			return maze
	except IOError:
		print("New Challenger !!!")
		return selectMaze(mazes)

def selectMaze(mazes):
	"""
		Affiche au joueur le choix des labyrinthes
	"""
	print("Voici la liste des labyrinthes disponibles :")
	x = 1
	liste = list()
	for maze in range(len(mazes)):
		print(" {}. {}".format(x, mazes[maze].nom))
		liste.append(str(x))
		x += 1

	while 1:
		choix = raw_input("Quel Labyrinthe voulez-vous résoudre ? ")
		if choix in liste:
			return mazes[int(choix)]

def svg(pseudo, maze):
	"""
		Sauvegarde la partie en cours dans le fichier "pseudo.maze"
	"""
	mazeDico = dict()
	mazeDico['nom'] = maze.nom
	mazeDico['path'] = maze.path
	mazeDico['door'] = maze.door
	mazeDico['grille'] = maze.grille
	fichier = pseudo + ".maze"

	with open(fichier, 'wb') as monFichier :
		mon_pickler = pickle.Pickler(monFichier)
		mon_pickler.dump(mazeDico)


def action(pseudo, maze):
	"""
	"""
	choix = afficheGrille(maze)
	if choix == "quit":
		return choix
	return resolution(choix, maze)




def afficheGrille(maze):
	"""
		On affiche la grille et on propose au joueur un choix
	"""
	liste = [1,2]
	while 1:
		print("\n\nAffichage de la grille :\n")
		print maze.grille
		print("\n Q pour quitter")
		print("H pour l'aide")
		choix = raw_input("Que voulez-vous faire ? ")
		if len(choix) in liste:
			if len(choix) == 2:
				print("A Faire") # a faire
			elif choix.lower() == "q":
				return "quit"
			elif choix.lower() == "h":
				afficheHelp()

def afficheHelp():
	"""
		Affichage d'une aide pour le joueur
	"""
	print("\n\n\n\n")
	print("Aide :")
	print("------")
	print("   N pour aller vers le haut de l'écran")
	print("   S pour aller vers le bas de l'écran")
	print("   E pour aller vers la droite de l'écran")
	print("   O pour aller vers la gauche de l'écran")
	print("\n")
	print("   Indiquez un chiffre pour avancer de plusieures cases")
	print("     > N7 avance vers le haut de l'écran de 7 cases")
	print("\n")
	print("   Q pour quitter le jeu")
	print("   H pour afficher cet écran")
	print("\n")



