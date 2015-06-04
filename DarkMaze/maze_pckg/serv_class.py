#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Module contenant les class principales du jeu côté serveur
"""


# Imports externes
import os
import socket
import select
from threading import Thread, RLock

# Imports internes
from .serv_function import *


class Data():
	"""
		classe contenant les données globales
	"""
	hote = ''
	port = 10666
	connexion = None
	addClient = True # passer a False quand la partie commencera
	maze = None #contient les données du labyrinthe en cours, class Maze
	getClient = True
	clients_connectes = []


class Maze:
	def __init__(self, nom_carte, grille):
		"""initialisation d'un labyrinthe 
		"""

		self.nom = nom_carte
		self.grille = self.strToList(grille)
		self.dim = self.defDimensions(grille)

	def strToList(self, grille):
		"""
			Construit le labyrinthe à partir d'une chine de caractère
			en un tableau à 2 dimensions représenté par une liste de listes
		"""
		maze = []
		ligne = []
		for char in grille:
			if char == "\n":
				# si on détecte un saut de ligne, on met notre liste "ligne" à la fin de notre liste labyrinthe
				# et on remet la ligne à zéro 
				maze.append(ligne)
				ligne = []
			else :
				ligne.append(char)

		return maze # renvoi le labyrinthe construit

	def defDimensions(self, grille):
		"""
			On parcourt toute la grille pour connaitre sa largeur x et sa hauteur y 
		"""
		y = 0
		x = 0
		for car in grille:
			if car == "\n":
				y += 1
				defX = x-2
				x = 0
			x += 1
		return (defX,y)

	def __str__(self):
		"""
			affichage de la grille
		"""
		sortie = ""
		for j in range(self.dim[1]):
			for i in range(self.dim[0]):
				sortie += self.grille[j][i]
			sortie += "\n"
		return sortie


class Connexion(Data):
	"""
		ensemble des méthodes concernant les connexion TCP
	"""
	def __init__(self):
		Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Data.connexion.bind((Data.hote, Data.port))
		Data.connexion.listen(5)
		print("Le serveur écoute à présent sur le port {}".format(Data.port))


class NewClient(Thread, Data):
	"""	Classe définissant le thread qui va ajouter des nouvelles connexions tant que c'est possible"""

	def __init__(self):
		Thread.__init__(self)

	def run(self):
		"""Code à exécuter pendant l'exécution du thread."""
		pass
