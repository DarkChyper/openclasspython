#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# Imports externes
import os
import socket
import select
from threading import Thread, RLock
from random import randrange
from time import *
import re

# Imports internes
from .sv_data import *
from .sv_function import *


class Maze():
	"""Classe définissant une carte de labyrinthe avec toutes ses caractéristiques"""

	def __init__(self, nom_carte, grille):
		"""initialisation d'un labyrinthe """

		self.nom = nom_carte
		self.grille = self.strToList(grille)
		self.dim = self.defDimensions(grille) # tupple (x,y)
		self.sortie = self.defSortie(self.grille) # tupple (x,y)

	def strToList(self, grille):
		"""
			Construit le labyrinthe à partir d'une chaine de caractères
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
		y = len(self.grille)
		x = len(self.grille[0])
		return (x,y)

	def defSortie(self, grille):
		""" Méthode qui retourne un tupple des coordonnees de la sortie du labyrinthe"""
		x = 0
		y = 0
		for ligne in grille:
			for case in ligne:
				if case == "U":
					return (x,y)
				x += 1
			x = 0
			y += 1

	def genGrille(self, donneesdeconnexion):
		"""
		"""
		lsPos, clPos = self.genPos(donneesdeconnexion) # retourne une liste de tupple contenant les positions des joueurs et un tupple contenant la position du joueur en cours
		longueur = range(self.dim[0])
		largeur = range(self.dim[1])

		grille = ""

		for y in largeur:
			for x in longueur:
				if (x,y) in lsPos: # Si la case est prise par un robot
					if (x,y) == clPos: # si le robot est ccelui du client à qui l'on envoie la grille
						grille += "X"
					else :
						grille += "x" # si le robot n'est pas celui du client à qui l'on envoie la grille
				else :
					grille += self.grille[y][x] # si la case n'est pas prise par un robot
			grille += "\n"

		return "GRI" + grille

	def genPos(self, client):
		""" retourne une liste de tupple des positions des joueurs
			ainsi que le tupple de la position du joueur concerné """
		pass
		liste = []
		nbre = len(Data.connectes)
		rnbre = range(nbre)
		for cl in rnbre:
			if Data.connectes[cl][0] == client:
				clPos = (Data.connectes[cl][3],Data.connectes[cl][4])
			if Data.connectes[cl][2]:
				# on n'affiche le robot que si le joueur est encore connecté
				liste.append((Data.connectes[cl][3],Data.connectes[cl][4]))

		return liste, clPos

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

	def mouvement(self, client, x, y, mvt):
		""" Méthode qui vérifie si le mouvement est valide ou non  et modifie la grille au besoin """
		u = int(x)
		v = int(y)

		if mvt == "N":
			v = v - 1
		elif mvt == "E":
			u += 1
		elif mvt == "S":
			v += 1
		elif mvt == "O":
			u = u - 1
		else :
			return False

		if u >= 0 and u <= self.dim[0] and v >= 0 and v <= self.dim[1]:
			# le mouvement reste dans la grille, on continue

			if self.grille[v][u] == " " or self.grille[v][u] == "." or self.grille[v][u] == "U" :
				# le mouvement n'arrive pas sur un obstacle, on continue
				test = self.nonPris((u,v))
				if not test:
					return False


				if Data.connectes[client][5]: 
					# si le joueur était sur une porte, on la réaffiche

					self.grille[Data.connectes[client][4]][Data.connectes[client][3]] == "."
					Data.connectes[client][5] = False
				else :
					self.grille[Data.connectes[client][4]][Data.connectes[client][3]] == " "

				if self.grille[v][u] == ".": 
					# si le joueur arrive sur une porte, on la garde en mémoire
					Data.connectes[client][5] = True

				Data.connectes[client][3] = u
				Data.connectes[client][4] = v

				return True

			else: # si le mouvement cible est un mur ou un autre joueur, mouvement impossible
				return False

		else : # la position visée est hors grille, mouvement impossible
			return False

	def murer(self, client, x, y , direction):
		""" réalise le murage d'une porte si la ccase visées est bine une porte """

		if direction == "N":
			y -= 1
		elif direction == "E":
			x += 1
		elif direction == "S":
			y += 1
		elif direction == "O":
			x -= 1
		else :
			return False

		if x >= 0 and x <= self.dim[0] and y >= 0 and y <= self.dim[1]:
			if self.grille[y][x] == ".":
				self.grille[y][x] = "O"
				return True
			else :
				return False
		else:
			return False

	def creuser(self, client, x, y , direction):
		""" réalise le creusage d'une porte dans un mur si la case visée est bien un mur """

		if direction == "N":
			y -= 1
		elif direction == "E":
			x += 1
		elif direction == "S":
			y += 1
		elif direction == "O":
			x -= 1
		else :
			return False

		if x >= 0 and x <= self.dim[0] and y >= 0 and y <= self.dim[1]:
			if self.grille[y][x] == "O":
				self.grille[y][x] = "."
				return True
			else :
				return False
		else:
			return False

	def nonPris(self, positionATester):
		""" Prend un tupple de position à tester (x, y
			Parcourt les clients encore connectés et compare les positions des robots
			Si la positionATester == la position d'un autre robot, renvoie False
			Sinon renvoi True"""

		Data.printd("On vérifie que la case cible n'est pas prise par un autre joueur")
		Data.printd(positionATester)

		nbreJoueurs = len(Data.connectes)
		liste_indices = range(nbreJoueurs)
		for client in liste_indices:
			if Data.connectes[client][2]:
				Data.printd("x={} y={}".format(Data.connectes[client][3],Data.connectes[client][4]))
				if (Data.connectes[client][3],Data.connectes[client][4]) == positionATester:
					return False
		return True

