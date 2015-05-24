#!/usr/python3.4
# -*- coding: utf8 -*-

"""
	Fichier contenant les class utilisées pour le jeu de labyrinthe
	pour OpenClassRooms
"""
class Maze:
	"""
		La classe qui crée un labyrinthe avec toutes ses caractéristiques
		Comme son nom, la position de chaque élément et la grille à afficher
	"""
	def __init__(self, nom_carte, chemin, door, grille):
		"""initialisation d'un labyrinthe avec
			son nom et le chemin où on le trouve
			la grille du jeu, a afficher et modifier
			la position modifiable de x le petit robot
			les dimensions non modifiables du labyrinthe
			un booleen qui indique si le robot est sur une porte ou non (afin de la réafficher après mouvement)
		"""

		self.nom = nom_carte
		self.path = chemin
		self.grille = grille
		self.posX = self.defPosX(grille)
		self.door = door # Devient True si le robot est sur une porte sinon est False
		self.dim = self.defDimensions(grille)

	def __str__(self):
		"""
			Permet un affichage maîtrisé de notre labyrinthe
		"""
		return "Maze : {}\n{}\n\nDimensions du labyrinthe : {}\nPosition du Robot : {}\nGrille :\n{}".format(self.nom,self.path,self.dim,self.posX,self.grille)

	def defPosX(self,grille):
		"""
			On parcourt la grille jusqu'à trouver "x" et on retourne alor la liste des coordonnées
		"""
		y = 1
		x = 1
		for car in grille:
			if car == "X":
				return [x,y]
			if car == "\n":
				y += 1
				x = 0
			x += 1

	def defDimensions(self, grille):
		"""
			On parcourt toute la grille pour connaitre sa largeur x et sa hauteur y 
		"""
		y = 1
		x = 1
		for car in grille:
			if car == "\n":
				y += 1
				defX = x-1
				x = 0
			x += 1
		return (defX,y)



