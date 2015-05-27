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
		#print("choix {}".format(choix))

		
		if choix[0].lower() == "n":
			xToPos = [self.posX[0],self.posX[1] - choix[1]]
		elif choix[0].lower() == "e":
			xToPos = [self.posX[0] + choix[1],self.posX[1]]
		elif choix[0].lower() == "s":
			xToPos = [self.posX[0],self.posX[1] + choix[1]]
		elif choix[0].lower() == "o":
			xToPos = [self.posX[0] - choix[1],self.posX[1]]
		else :
			print("Erreur de mouvement !")
			return "KO"
		#print("self.posX {}".format(self.posX))
		#print("xToPos {}".format(xToPos))

		# On vérifie que la nouvelle position est dans la grille
		#print("On verifie si on sort de la grille")
		if xToPos[0] > self.dim[0] or xToPos[0] < 1 or xToPos[1] > self.dim[1] or xToPos[1] < 1:
			return "KO"

		#print("on avance pas à pas ppour voir si il y a une collision ou pas")
		# On avance case en case poir savoir si on rencontre un mur
		posX = list(self.posX)
		retour = None
		if choix[0].lower() == "n": # si on monte
			while xToPos[1] <> posX[1]:
				retour = self.verifCollision( [ posX[0],posX[1] - 1 ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[1] -= 1
			# on n'a pas rencontré de mur
		elif choix[0].lower() == "e": # si on va à droite
			while xToPos[0] <> posX[0]:
				retour = self.verifCollision( [ posX[0] + 1,posX[1] ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[0] += 1
			# on n'a pas rencontré de mur
		elif choix[0].lower() == "s": # si on va en bas
			while xToPos[1] <> posX[1]:
				retour = self.verifCollision( [ posX[0],posX[1] + 1 ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[1] += 1
			# on n'a pas rencontré de mur
		elif choix[0].lower() == "o" : # si on va vers la gauche
			while xToPos[0] <> posX[0]:
				retour = self.verifCollision( [ posX[0] - 1,posX[1] ] ) # la verification se fait sur un tupple contenant la position du robot + pas
				if retour == "KO":
					return "KO"
				posX[0] -= 1
			# on n'a pas rencontré de mur
		else:
			print("Erreur de mouvement !")
			return "KO"

		# On vérifie que ce n'est pas la sortie
		#print("sortie {} xToPos {}".format(self.sortie,xToPos))
		if xToPos[0] == self.sortie[0] and xToPos[1] == self.sortie[1]:
			return "WIN"

		# si on arrive ici il faut modifier la grille
		self.grille = self.modifGrille(xToPos)

		# On vérifie si la case cible est une porte
		if retour == "DOOR":
			self.door = True

		self.posX = xToPos

		return "OK"

	def verifCollision(self, positionATester):
		"""
			Reçoit un tupple contenant la position à tester
			On déroule la grille et retourne KO si on rencontre un mur à la position 
			ou OK si ce n'est pas un mur
		"""
		y = 1
		x = 1
		#print("Position à tester {}".format(positionATester))
		for car in self.grille:
			#print("x = {} y = {}".format(x,y))
			if x == positionATester[0] and y == positionATester[1]:
				if car == "O":
					#print("position {} {} caractere {}".format(x,y,car))
					return "KO" # si la position à tester est un mur on renvoi KO
				elif car == ".":
					return "DOOR" # si on est sur une porte on l'indique
				else:
					return "OK" # sinon on renvoi OK
			if car == "\n":
				y += 1
				x = 0
			x += 1

	def modifGrille(self, xToPos):
		"""
			on parcourt la grille en remplacant la position du robot et en réaffichant les portes au besoin
			renvoie la grille modifiée
		"""
		newGrille = str()
		y = 1
		x = 1
		#print("Ancienne position du robot {}".format(self.posX))
		#print("Nouvelle position du robot {}".format(xToPos))
		for car in self.grille:
			#print("x={} y={}".format(x,y))
			if car == "\n":
				#print("Saut de ligne {}".format(y))
				newGrille += car
				y += 1
				x = 0
			elif xToPos[0] == x and xToPos[1] == y : # on détecte la case de fin de mouvement du robot pour l'écrire
				#print("On ajoute le robot")
				newGrille += "X"
					
			elif car == "X": # on détecte la case de l'ancien emplacement du robot
				#print("On efface le robot")
				if self.door == True: # si c'était une porte on l'affiche et on indique que le robot n'est plus sur une porte
					newGrille += "."
					self.door = False
				else:
					newGrille += " "# sinon c'est un couloir que l'on affiche
					
			else:
				newGrille += car
			x += 1

		return newGrille


		






