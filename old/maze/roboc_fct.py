#!/usr/python3.4
# -*- coding: utf8 -*-

"""
	Fichier contenant les fonction nécessaires au jeu de 
	labyrinthe pour OpenClassRooms
"""

import os
from pickle import Pickler, Unpickler
from roboc_cls import *

"""
	Maze est une class qui crée l'objet Maze
	mazes est une liste contenant des objets Maze
	maze est un objet de type Maze
"""

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
			pseudo = input("Quel est votre nom/Pseudo ? ")
			assert pseudo != "" and len(pseudo) < 20 
		except AssertionError:
			print("Votre pseudo ne peut être vide et doit faire moins de 20 caractères")
		else:
			return pseudo


def verifSvg(pseudo):
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
			dico = mazeDico.load()
			maze = Maze(dico['nom'],dico['path'],dico['door'],dico['grille'])
			print("Reprise de la partie sauvegardée.")
			return maze
	except IOError:
		print("New Challenger !!!")
		return selectMaze()

def selectMaze():
	"""
		Initialise les labyrinthes selon les fichiers dans ./cartes/
		Affiche une liste de choix au joueur 
		Renvoi la map selectionnée
	"""
	# On importe les cartes existantes
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

def svg(pseudo, maze):
	"""
		Sauvegarde la partie en cours dans le fichier "pseudo.maze"
	"""
	mazeDico = {
	"nom":maze.nom, 
	"path":maze.path, 
	"door":maze.door,
	"sortie":maze.sortie, 
	"grille":maze.grille
	}
	#mazeDico[nom] = maze.nom
	#mazeDico[path] = maze.path
	#mazeDico[door] = maze.door
	#mazeDico[grille] = maze.grille
	fichier = pseudo + ".maze"

	with open(fichier, 'wb') as monFichier :
		mon_pickler = Pickler(monFichier)
		mon_pickler.dump(mazeDico)

def afficheGrille(maze):
	"""
		On affiche la grille et on propose au joueur un choix
		On vérifie ce choix puis on résoud ce choix.
	"""
	directions = ("n","s","e","o")
	while 1:
		print("\n\nAffichage de la grille :\n")
		print(maze.grille)
		print("\nQ pour quitter")
		print("H pour l'aide")
		choix = input("Que voulez-vous faire ? ")
		if len(choix) >= 1:
			if choix.lower() == "q":
				return "quit"
			elif choix.lower() == "h":
				afficheHelp()
			elif choix.lower()[0] in directions:
				if len(choix) >= 2:
					try:
						distance = int(choix[1:])
					except ValueError:
						print("Valeur de distance incorrecte !")
					else:
						# Le joueur a défini une direction et une distance valide
						return (choix[0],int(choix[1:]))
				else:
					# Le joueur a definit une direction valide et avance par defaut de 1
					return (choix[0],1)

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

def resolution(choix, maze):
	"""
		Résoud le déplacement du robot si il est possible
		Prend un tupple, le labyrinthe en entrée
		Renvoie un labyrinthe
	"""
	if choix[1] == 0:
		print("Le robot reste à la même place")
		return maze

	resultat = maze.mouvement(choix)

	if resultat == "WIN":
		print("\n\nBravo ! Vous avez gagné !")
		return selectMaze() # Si le joueur a gagné, il choisit un nouveau labyrinthe

	if resultat == "KO":
		print("Mouvement Impossible !!")

	return maze # que le mouvement soit valide ou non, on renvoi l'objet pour continuer

