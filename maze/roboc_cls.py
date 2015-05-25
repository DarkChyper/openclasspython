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
	def __init__(self, nom_carte, chemin, door, sortie, grille):
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
		self.sortie = self.defPosSortie(grille) 
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

	def defPosSortie(self,grille):
		"""
			On parcourt la grille jusqu'à trouver "x" et on retourne alor la liste des coordonnées
		"""
		y = 1
		x = 1
		for car in grille:
			if car == "U":
				return (x,y)
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

	def mouvement(self, choix):
		"""

		"""
		# On calcule la position future du robot
		posX = self.posX
		if choix[0] == "N":
			xToPos = [posX[0],posX[1] - choix[1]]
		elif choix[0] == "E":
			xToPos = [posX[0] + choix[1],posX[1]]
		elif choix[0] == "S":
			xToPos = [posX[0],posX[1] + choix[1]]
		else:
			xToPos = [posX[0] - choix[1],posX[1]]

		# On vérifie que la nouvelle position est dans la grille
		if xToPos[0] > dim[0] or xToPos[0] < 1 or xToPos[1] > dim[1] or xToPos[1] < 1:
			return "KO"

		# On avance case en case poir savoir si on rencontre un mur
		retour = None
		if choix[0] == "N": # si on monte
			while xToPos[1] < posX[1]:
				retour = verifCollision( [ posX[0],posX[1] - 1 ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[1] -= 1
			# on n'a pas rencontré de mur
		elif choix[0] == "E": # si on va à droite
			while xToPos[0] > posX[0]:
				retour = verifCollision( [ posX[0] + 1,posX[1] ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[0] += 1
			# on n'a pas rencontré de mur
		elif choix[0] == "S": # si on va en bas
			while xToPos[1] > posX[1]:
				retour = verifCollision( [ posX[0],posX[1] + 1 ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[1] += 1
			# on n'a pas rencontré de mur
		else: # si on va vers la gauche
			while xToPos[0] < posX[0]:
				retour = verifCollision( [ posX[0] - 1,posX[1] ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[0] -= 1
			# on n'a pas rencontré de mur

		# On vérifie si la case est une porte
		if retour == "DOOR":
			self.door = True

		# On vérifie que ce n'est pas la sortie
		if xToPos[0] == self.sortie[0] and xToPos[1] == self.sortie[1]:
			return "WIN"

		# si on arrive ici il faut modifier la grille

	def verifCollision(self, positionATester):
		"""
			Reçoit un tupple contenant la position à tester
			On déroule la grille et retourne KO si on rencontre un mur à la position 
			ou OK si ce n'est pas un mur
		"""
		y = 1
		x = 1
		for car in grille:
			if x == positionATester[0] and y == positionATester[1]:
				if car == "O":
					return "KO" # si la position à tester est un mur on renvoi KO
				elif car == ".":
					return "DOOR" # si on est sur une porte on l'indique
				else:
					return "OK" # sinon on renvoi OK
			if car == "\n":
				y += 1
				x = 0
			x += 1
		






