#!/usr/python3.4
# -*- coding: utf8 -*-

"""
	Fichier contenant les fonction nécessaires au jeu de 
	labyrinthe pour OpenClassRooms
"""

import os
from roboc_cls import *

def initCartes():
	""" 
		On récupère les cartes au format txt dan le dossier ./cartes
		On les charge dans le jeu sous forme d'une liste d'objets maze
		On retourne cette liste au programme principale
	"""
	cartes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("cartes", nom_fichier)
			nom_carte = nom_fichier[:-4].lower()
			with open(chemin, "r") as fichier:
				grille = fichier.read()
				# On va construire l'objet Maze à partir
				# du nom de la carte, de son chemin d'accès et de son contenu
				cartes.append(Maze(nom_carte,chemin,grille))
	return cartes

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

def verifSvg(pseudo):
	"""
		Vérifie la présence d'un éventuel fichier "pseudo.maze" 
			> Charge le fichier si il le trouve,
			> Demande de choisir un labyrinthe si il n'en trouve pas
			  ou si le joueur a sauvegardé à la fin d'un labyrinthe.
			> Sauvegarde la parie 
			> retourne le labyrinthe en cours
	"""

