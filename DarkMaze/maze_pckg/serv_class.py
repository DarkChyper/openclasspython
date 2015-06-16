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
		client_temp = ""
		client_joue_temp = ""
		jouer = False 	# Passera à True si le joueur a fait une action terminant son tour, 
						# puis repassera a false pour le joueur suivant

	def run(self):
		""" Thread qui gère toute la partie en cours """
		# on commence par envoyer à tous les joueurs la grille de jeu
		for client in Data.connectes:
			grille = Maze.genGrille(Data.connectes[client][0])
			grille = grille.encode()
			client.send(grille)

		#Ensuite on envoi le STR a tous avec la liste des joueurs
		msgListe = Data.listePseudo()
		self.MessageATous(msgListe)

		# on lance la boucle du jeu
		while Data.nonEnd :
			for temp in Data.connectes:
				self.client_joue_temp = []
				if Data.connectes[self.client_joue_temp][1]: # On ne gère le joueur que si il est encore connecté
					MessageATous("WTU{}".format(Data.connectes[self.client_joue_temp][2]))
					self.jouer = False 
					while  jouer != True: 
						clients_a_lire = []
						try:
							clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
						except select.error:
							pass
						else: # On permer aux utres joueurs d'envoyer des données même pendant le tour d'un autre
							for self.client_temp in clients_a_lire:
								msg_recu = self.client_temp.recv(1024).decode()
								if self.client_temp == self.clien_joue_temp:
									if msg_recu[:3] in Data.listeMsgOk:
										pass
								else:
									if msg_recu[:3] in Data.listeMsgOkNonJoueur:
										Messages(msg_recu[:3],msg_recu[3:]) # on traite le message recu

	def MessageATous(self, message):
		""" méthode qui envoi à tous les clients encores conectés le message fournnint en entrée"""
		for client in Data.connectes:
			if Data.connectes[client][1]: # on vérifie que le joueur l'on envoie qu'aux joueurs encore connectés
				Data.connectes[client][0].send(message.encode())


	def Messages(self, tipe, message):
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

