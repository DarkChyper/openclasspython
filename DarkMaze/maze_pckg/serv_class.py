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
from random import randrange

# Imports internes
from .serv_function import *
from .serv_data import *

class Maze(Data):
	"""Classe définissant une carte de labyrinthe avec toutes ses caractéristiques"""

	def __init__(self, nom_carte, grille):
		"""initialisation d'un labyrinthe """

		self.nom = nom_carte
		self.grille = self.strToList(grille)
		self.dim = self.defDimensions(grille) # tupple (x,y)

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
		y = 0
		x = 0
		for car in grille:
			if car == "\n":
				y += 1
				defX = x-2
				x = 0
			x += 1
		return (defX,y)

	def genGrille(self, client):
		lsPos, clPos = self.genPos(client) # retourne une liste de tupple contenant les positions des joueurs et un tupple contenant la position du joueur en cours
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
					grille += self.grille[y][X] # si la case n'est pas prise par un robot
			grille += "\n"

		return grille

	def genPos(self, client):
		""" retourne une liste de tupple des positions des joueurs
			ainsi que le tupple de la position du joueur concerné """
		pass
		liste = []
		for cl in Data.connectes:
			if Data.Connectes[cl][0] == client:
				clPos = (Data.Connectes[cl][3],Data.Connectes[cl][4])
			liste.append((Data.Connectes[cl][3],Data.Connectes[cl][4]))

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

	def mouvement(self, client, x, y, mvt, dist):
		""" Méthode qui vérifie si le mouvement est valide ou non  et modifie la grille au besoin """
		u = int(x)
		v = int(y)

		if mvt == "N":
			v += dist
		elif mvt == "E":
			u += dist
		elif mvt == "S":
			v -= dist
		elif mvt == "O":
			u -= dist
		else :
			return False

		if u >= 0 and u <= self.dim[0] and v >= 0 and v <= self.dim[1]:
			# le mouvement reste dans la grille, on continue

			if self.grille[v][u] == " " or self.grille[v][u] == "." or self.grille[v][u] == "U":
				# le mouvement n'arrive pas sur un obstacle, on continue

				if Data.connetces[client][5]: 
					# si le joueur était sur une porte, on la réaffiche

					self.grille[Data.connectes[client][4]][Data.connectes[client][3]] == "."
					Data.connetces[client][5] = False
				else :
					self.grille[Data.connectes[client][4]][Data.connectes[client][3]] == " "

				if self.grille[v][u] == ".": 
					# si le joueur arrive sur une porte, on la garde en mémoire
					Data.connetces[client][5] = True

				Data.connetces[client][3] == u
				Data.connetces[client][4] == v
				return True

			else: # si le mouvement cible est un mur ou un autre joueur, mouvement impossible
				return False

		else : # la position visée est hors grille, mouvement impossible
			return False



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
		liste_temp = []
		while Data.addClient:
			# On va vérifier que de nouveaux clients ne demandent pas à se connecter
			connexions_demandees, wlist, xlist = select.select([Data.connexion], [], [], 0.05)

			for connexion in connexions_demandees:
				connexion_avec_client, infos_connexion = connexion.accept()
				joueur = []
				joueur.append(infos_connexion)
				joueur.append("NoName") # le pseudonyme sera définit plus tard
				joueur.append(True) 
				x, y = self.definePosJoueur() # on place au hasard le joueur
				joueur.append(x)
				joueur.append(y)
				joueur.append(False) # le joueur ne peut être placé sur une porte dès le début.
				Data.connectes.append(joueur)
				liste_temp.append(infos_connexion) # une liste des clients temporaire pour envoyer une seule fois le message "La partie peut commencer"
				Data.clients_connectes.append(infos_connexion) 

			nombre = len(Data.connectes)
			if nombre >= Data.nbrJoueursMin: # on ne peut lancer la partie que si il y a au moins n joueurs
				for temp in liste_temp:
					client.send("INI".encode())
					message = "MSGIl y a " + str(nombre) + " connectés sur le serveur\nCliquez sur \"Commencer\" pour commencer la partie"
					client.send(message.encode())
				liste_temp = []

				# On vérifie si un joueur déja connecté veut lancer la partie
				clients_a_lire = []
				try:
					clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
				except select.error:
					pass
				else:
					for client in clients_a_lire:
						msg_recu = client.recv(1024).decode()
						if msg_recu[:3] == "INI":
							Data.addClient = False
							break
						if msg_recu[:3] == "PSD"
							self.majPseudo(client, msg_recu[3:])
	def definePosJoueur(self):
		"""On place le joueur au hasard sur la map"""
		longueur = Data.maze.dim[0]
		largeur = Data.maze.dim[1]
		while 1:
			x = randrange(longueur)
			y = randrange(largeur)
			case = Data.maze.grille[y][x]
			if case != "O" and case != "." and case != "U" :
				dejapris = False
				t = (x,y)
				for joueur in Data.connectes:
					T = (Data.connectes[joueur][3],Data.connectes[joueur][4])
					if T == t:
						dejapris = True
				if dejapris == False :
					return x, y


class Partie(Thread, Data):

	def __init__(self):
		""" Déclare les données utiles ppour la partie"""
		Thread.__init__(self)
		message : ""
		clientAutre = ""
		clientQuiJoue = ""
		liste = []
		joueur = False  # Sera utile lors de la gestion d'un chat, déterminera quel pseudo entre clientAutre et clientQuiJoue
		jouer = False 	# Passera à True si le joueur a fait une action terminant son tour, 
						# puis repassera a false pour le joueur suivant

	def run(self):
		""" Thread qui gère toute la partie en cours """

		# on commence par envoyer à tous les joueurs la grille de jeu
		self.EnvoieGrille()

		#Ensuite on envoi le STR a tous avec la liste des joueurs
		msgListe = Data.listePseudo()
		self.MessageATous(msgListe)

		nbreJoueurs = len(Data.connectes)
		clients_a_lire = []
		# on lance la boucle du jeu
		while Data.nonEnd : 	# On boucle tant que le jeu n'est pas terminé
			self.liste = range(nbreJoueurs)
			for self.clientQuiJoue in liste: # On boucle sur les indices de la liste Data.connectés sans se soucié que le joueur soit connecté ou non

				if Data.connectes[self.clientQuiJoue][1]: # On ne gère le joueur que si il est encore connecté

					MessageATous("WTU{}".format(Data.connectes[self.clientQuiJoue][2]))
					self.jouer = False 

					while  self.jouer != True: # tant que le joueur n'a pas fait d'action terminant son tour, on boucle pour lire tout le monde

					
						try:
							nouveaux_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
						except select.error:
							pass
						else: 
							clients_a_lire.append(nouveaux_a_lire) # on récupère les nouvelles personnes à lire que l'on ajoute à ceux que l'on avait déjà

							for self.clientAutre in clients_a_lire:

								msg_recu = self.client_temp.recv(1024).decode()

								# Si le joueur a lire est le joueur en cours
								if self.clientAutre == self.clientQuiJoue:
									Data.joueur = True
									if msg_recu[:3] in Data.listeMsgOk:
										MessagesIn(msg_recu[:3],msg_recu[3:])
								# sinon
								else:
									if msg_recu[:3] in Data.listeMsgOkNonJoueur:
										MessagesIn(msg_recu[:3],msg_recu[3:]) # on traite le message recu

								Data.joueur = False

			if Sortie() : # sera vrai s'il n'y a plus de joueur dans Data.connecté[][1] à True
				Data.nonEnd = False # termine le jeu

	def Envoiegrille(self):
		""" Méthode qui envoie à tous les joueurs encore connectés la grille avec la position de tous les joueurs
			le joueur à qui l'on envoie la grille est différencié par un X à la place d'un x """
		for client in Data.connectes:
			if Data.connectes[client][1]:
				grille = Maze.genGrille(Data.liste_connectes[client])
				grille = grille.encode()
				client.send(grille)

	def MessageATous(self, message):
		""" méthode qui envoi à tous les clients encores conectés le message fournnint en entrée"""
		for client in Data.liste_connectes:
			if Data.connectes[client][1]: # on vérifie que le joueur l'on envoie qu'aux joueurs encore connectés
				Data.liste_connectes[client].send(message.encode())


	def MessagesIn(self, tipe, message):
		""" Traite la réception des messages en provenance des joueurs """
		self.message = message
		messagesTypes = { 
			"MSG":self.msg,	##########
			"PSD":self.psd,	#	#   Types possibles par tous les joueurs
			"EXI":self.exi,	#	######
			"MVT":self.mvt,	#
			"MUR":self.mur,	#	Types possibles par le joueur dont c'est le tour
			"CRE":self.cre	#####
			}
		messagesTypes[tipe]()

	def msg(self):
		""" Fonctionnalité future qui renverra à tous les joueurs connectés le message d'un joueur
			Ne compte pas pour une action du joueur en cours"""
		pass

	def psd(self):
		""" Permet de mettre à jour le pseudonyme d'un joueur,
			utile si un joueur n'a pas eu le temps de le renseigner durant l'initialisation du jeu
			Ne compte pas pour une action du joueur en cours"""
		for cl in Data.connectes:
			if Data.connectes[cl][0] == Data.connectes[self.client_temp][0]:
				Data.connectes[cl][2] = self.message


	def exi(self):
		""" Permet de gérer la déconnection d'un joueur """
		message = "EXI" + self.message
		self.MessageATous(message)
		if self.joueur :
			self.jouer = True

	def mvt(self):
		""" Méthode qui gère le type Mouvement
			On indique que le joueur a effectuée une action, même si le mouvement est impossible"""

		self.jouer = True
		if Data.maze.mouvement(self.ClientQuiJoue, Data.connectes[self.ClientQuiJoue][3], Data.connectes[self.ClientQuiJoue][4], self.message[0], self.message[1]):
			# on envoie la nouvelle grille à tout le monde

			# on termine le tour du joueur
			message = "ETU" + Data.connectes[self.clientQuiJoue][2]
			self.messageATous(message)
			self.Envoiegrille()
		else :


		pass

	def mur(self):
		self.jouer = True
		pass

	def cre(self):
		self.jouer = True
		pass

	def Sortie(self):
		""" Verifie si il y a encore un joueur de connecté
			renvoir False si il y a au moins une personne de connectée, True sinon"""
		nbre = 0
		for l in Data.connectes:
			if Data.connectes[l][1]:
				return False
		return True


