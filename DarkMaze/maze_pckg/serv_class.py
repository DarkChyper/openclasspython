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
from time import *

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

	def murer(self, client, x, y , direction):


		if direction == "N":
			x+= 1
		elif direction == "E":
			y += 1
		elif direction == "S":
			x -= 1
		elif direction == "O":
			y -= 1
		else :
			return False

		if x >= 0 and x <= self.dim[0] and y >= 0 and y <= self.dim[1]:
			if self.grille[y][x] == ".":
				pself.grille[y][x] = "O"
				return True
			else :
				return False
		else:
			return False

	def creuser(self, client, x, y , direction):


		if direction == "N":
			x+= 1
		elif direction == "E":
			y += 1
		elif direction == "S":
			x -= 1
		elif direction == "O":
			y -= 1
		else :
			return False

		if x >= 0 and x <= self.dim[0] and y >= 0 and y <= self.dim[1]:
			if self.grille[y][x] == "O":
				pself.grille[y][x] = "."
				return True
			else :
				return False
		else:
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


class NewClient(Data):
	"""	Classe définissant le thread qui va ajouter des nouvelles connexions tant que c'est possible"""

	def __init__(self):
		liste_temp = []
		i = 0 # compteur de joueur connectes pour éviter d'avoir plusieurs pseudonymes par defaut identiques
		while Data.addClient:
			# On va vérifier que de nouveaux clients ne demandent pas à se connecter
			connexions_demandees, wlist, xlist = select.select([Data.connexion], [], [], 0.05)

			for connexion in connexions_demandees:
				connexion_avec_client, infos_connexion = connexion.accept()
				joueur = []
				joueur.append(connexion_avec_client)
				joueur.append("NoName{}".format(str(i))) # le pseudonyme sera définit plus tard
				i += 1
				joueur.append(True) 
				x, y = self.definePosJoueur() # on place au hasard le joueur
				joueur.append(x)
				joueur.append(y)
				joueur.append(False) # le joueur ne peut être placé sur une porte dès le début.
				Data.connectes.append(joueur)
				liste_temp.append(connexion_avec_client) # une liste des clients temporaire pour envoyer une seule fois le message "La partie peut commencer"
				Data.clients_connectes.append(connexion_avec_client) 

			nombre = len(Data.connectes)
			if nombre >= Data.nbrJoueursMin: # on ne peut lancer la partie que si il y a au moins n joueurs
				for temp in liste_temp:
					temp.send("INI".encode())
					sleep(5)
					message = ""
					message = "MSGIl y a " + str(nombre) + " connectés sur le serveur\nCliquez sur \"Commencer\" pour commencer la partie"
					temp.send(message.encode())
				liste_temp = []

				# On vérifie si un joueur déja connecté veut lancer la partie
				clients_a_lire = []
				try:
					clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
				except select.error:
					pass
				else:
					for client in clients_a_lire: # pour chaque connexion avec le client dans la liste de client à lire
						msg_recu = client.recv(1024).decode()
						Data.printd(msg_recu)
						if msg_recu[:3] == "INI":
							Data.addClient = False
							break
						if msg_recu[:3] == "PSD": # si on veut mettre à jour un pseudo
							nbre = len(Data.clients_connectes)
							nbre_range = range(nbre)
							for cl in nbre_range:
								if Data.connectes[cl][0] == client:
									Data.connectes[cl][2] = msg_recu[3:]


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
				nbreJoueurs = len(Data.connectes)
				liste = range(nbreJoueurs)
				for joueur in liste:
					T = (Data.connectes[joueur][3],Data.connectes[joueur][4])
					if T == t:
						dejapris = True
				if dejapris == False :
					Data.printd("x={};y={}".format(str(x),str(y)))
					return x, y


class Partie(Thread, Data):

	def __init__(self):
		""" Déclare les données utiles ppour la partie"""
		Thread.__init__(self)
		self.message = ""
		self.clientAutre = ""
		self.IndiceClientQuiJoue = ""
		self.nbreJoueurs = len(Data.connectes)
		self.liste_indices = range(self.nbreJoueurs)
		self.joueur = False  # Sera utile lors de la gestion d'un chat, déterminera quel pseudo entre clientAutre et IndiceClientQuiJoue
		self.jouer = False 	# Passera à True si le joueur a fait une action terminant son tour, 
						# puis repassera a false pour le joueur suivant

	def run(self):
		""" Thread qui gère toute la partie en cours """

		# on commence par envoyer à tous les joueurs la grille de jeu
		self.EnvoieGrille()

		#Ensuite on envoi le STR a tous avec la liste des joueurs
		msgListe = Data.listePseudo()
		self.MessageATous(msgListe)

		
		clients_a_lire = []
		# on lance la boucle du jeu
		while Data.nonEnd : 	# On boucle tant que le jeu n'est pas terminé
			for self.IndiceClientQuiJoue in self.liste_indices: # On boucle sur les indices de la liste Data.connectés sans se soucié que le joueur soit connecté ou non

				if Data.connectes[self.IndiceClientQuiJoue][1]: # On ne gère le joueur que si il est encore connecté

					MessageATous("WTU{}".format(Data.connectes[self.IndiceClientQuiJoue][2]))
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
								if self.clientAutre == self.IndiceClientQuiJoue:
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

		sleep(2)
		Data.connextion.close()# on coupe la connexion proprement

	def EnvoieGrille(self):
		""" Méthode qui envoie à tous les joueurs encore connectés la grille avec la position de tous les joueurs
			le joueur à qui l'on envoie la grille est différencié par un X à la place d'un x """
		for iclient in self.liste_indices:
			if Data.connectes[iclient][1]:
				grille = Maze.genGrille(Data.clients_connectes[iclient])
				grille = grille.encode()
				Data.clients_connectes[iclient].send(grille)

	def MessageATous(self, message):
		""" méthode qui envoi à tous les clients encores conectés le message fournnint en entrée"""
		for client in self.liste_indices:
			if Data.connectes[client][1]: # on vérifie que le joueur l'on envoie qu'aux joueurs encore connectés
				Data.clients_connectes[client].send(message.encode())


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
		if Data.maze.mouvement(self.IndiceClientQuiJoue, Data.connectes[self.IndiceClientQuiJoue][3], Data.connectes[self.IndiceClientQuiJoue][4], self.message[0]):
			# on envoie la nouvelle grille à tout le monde
			EnvoieGrille()

			if (Data.connectes[self.IndiceClientQuiJoue][3],Data.connectes[self.IndiceClientQuiJoue][4]) == Data.maze.dim:
				message = "WIN" + Data.connectes[self.IndiceClientQuiJoue][2]
				self.MessageATous(message)
				Data.nonEnd = False
				self.jouer = True
			else :	
				# on termine le tour du joueur
				message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][2]
				self.MessageATous(message)
				self.EnvoieGrille()
		else :
			message = "MSG" + "Mouvement Impossible"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			sleep(0.5)
			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][2]
			messageATous(message)


		pass

	def mur(self):
		self.jouer = True
		if Data.maze.murer(self.IndiceClientQuiJoue, Data.connectes[self.IndiceClientQuiJoue][3], Data.connectes[self.IndiceClientQuiJoue][4], self.message[0], self.message[1]):
			message = "MSG" + "La porte a été murée"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			sleep(0.5)
			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][2]
			self.MessageATous(message)
			sleep(0.5)
			self.EnvoieGrille
		else:
			message = "MSG" + "Murage impossible"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			sleep(0.5)
			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][2]
			self.MessageATous(message)
		

	def cre(self):
		self.jouer = True
		if Data.maze.creuser(self.IndiceClientQuiJoue, Data.connectes[self.IndiceClientQuiJoue][3], Data.connectes[self.IndiceClientQuiJoue][4], self.message[0], self.message[1]):
			message = "MSG" + "Une porte a été crée"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			sleep(0.5)
			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][2]
			self.MessageATous(message)
			sleep(0.5)
			self.EnvoieGrille
		else:
			message = "MSG" + "Construction d'une porte impossible."
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			sleep(0.5)
			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][2]
			self.MessageATous(message)

	def Sortie(self):
		""" Verifie si il y a encore un joueur de connecté
			renvoir False si il y a au moins une personne de connectée, True sinon"""
		nbre = 0
		for l in Data.connectes:
			if Data.connectes[l][1]:
				return False
		return True


