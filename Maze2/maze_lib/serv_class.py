#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	serv_class.py contient les classes utiles pour le serveur de jeu
"""

class Joueur:
	"""
		Définition d'un joueur dans la partie.
			Contient le nom du joueur,
			Sa connexion
			La position de son robot
			La presence d'une porte sous le robot
	"""
	def __init__(self, player, connexion, position, door):
		"""
			Constructeur
		"""
		self.player = player
		self.ip = connexion
		self.position = position # qui doit être une liste de 2 valeures
		self.door = door # qui sera initailisée à False

class Maze:
	def __init__(self, nom_carte, grille):
		"""initialisation d'un labyrinthe avec
			son nom et le chemin où on le trouve
			la grille du jeu, a afficher et modifier
			la position modifiable de x le petit robot
			les dimensions non modifiables du labyrinthe
			un booleen qui indique si le robot est sur une porte ou non (afin de la réafficher après mouvement)
		"""

		self.nom = nom_carte
		self.grille = self.strToList(grille)
		self.joueurs = []

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

	def addJoueur(self, joueur):
		"""
			Permet d'ajouter un joueur de class Joueur au labyrinthe
		"""
		self.joueurs.append(joueur)
