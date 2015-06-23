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
from .sv_maze import *

class Partie(Thread, Data):

	def __init__(self):
		""" Déclare les données utiles ppour la partie"""
		Thread.__init__(self)
		self.message = ""
		self.clientAutre = ""
		self.clients_a_lire = []
		self.IndiceClientQuiJoue = ""
		self.nbreJoueurs = len(Data.connectes)
		self.liste_indices = range(self.nbreJoueurs)
		self.joueur = False  # Sera utile lors de la gestion d'un chat, déterminera quel pseudo entre clientAutre et IndiceClientQuiJoue
		self.jouer = False 	# Passera à True si le joueur a fait une action terminant son tour, 
						# puis repassera a false pour le joueur suivant

	def run(self):
		""" Thread qui gère toute la partie en cours """
		sleep(2)
		# on commence par envoyer à tous les joueurs la grille de jeu
		print("On envoie la grille à tout le monde")
		self.EnvoieGrille()

		sleep(2)

		#Ensuite on envoi le STR a tous avec la liste des joueurs
		msgListe = Data.listePseudo()
		self.MessageATous(msgListe)

		sleep(2)

		# on lance la boucle du jeu
		while Data.nonEnd : 	# On boucle tant que le jeu n'est pas terminé
			for self.IndiceClientQuiJoue in self.liste_indices: # On boucle sur les indices de la liste Data.connectés sans se soucié que le joueur soit connecté ou non
				# on test si le joueur est encore connecté
				try:
					Data.connectes[self.IndiceClientQuiJoue][0].send("PING".encode())
				except socket.error:
					print("Joueur déconnecté")

				if Data.connectes[self.IndiceClientQuiJoue][2]: # On ne gère le joueur que si il est encore connecté

					# On indique à tous les joueur lequel est en train de jouer
					self.MessageATous("WTU{}".format(Data.connectes[self.IndiceClientQuiJoue][1]))

					# on initialise le tour du joueur
					self.jouer = False 
					dataClientQuiJoue = [Data.connectes[self.IndiceClientQuiJoue][0]]


					while  self.jouer != True: # tant que le joueur n'a pas fait d'action terminant son tour, on boucle pour lire tout le monde

						nouveaux_a_lire = []
						try:
							nouveaux_a_lire, wlist, xlist = select.select(dataClientQuiJoue, [], [], 0.05)
						except select.error:
							print("rien a lire")
							continue
						else: 
							Data.joueur = True

							for self.clientAutre in nouveaux_a_lire:
								msg_recu = self.clientAutre.recv(1024).decode()
								if msg_recu[:3] in Data.listeMsgOk:
										self.MessagesIn(msg_recu[:3],msg_recu[3:])
					sleep(1)

			if self.Sortie() : # sera vrai s'il n'y a plus de joueur dans Data.connecté[][1] à True
				Data.nonEnd = False # termine le jeu
			sleep(1)

		sleep(2)
		Data.connextion.close()# on coupe la connexion proprement

	def EnvoieGrille(self):
		""" Méthode qui envoie à tous les joueurs encore connectés la grille avec la position de tous les joueurs
			le joueur à qui l'on envoie la grille est différencié par un X à la place d'un x """
		for iclient in self.liste_indices:
			if Data.connectes[iclient][2]:
				grille = Data.maze.genGrille(Data.clients_connectes[iclient])
				grille = grille.encode()
				Data.connectes[iclient][0].send(grille)

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
				Data.connectes[cl][1] = self.message


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
			self.EnvoieGrille()
			
			sleep(1)

			if (Data.connectes[self.IndiceClientQuiJoue][3],Data.connectes[self.IndiceClientQuiJoue][4]) == Data.maze.sortie:
				message = "WIN" + Data.connectes[self.IndiceClientQuiJoue][1]
				self.MessageATous(message)
				Data.nonEnd = False
				self.jouer = True
			else :	
				# on termine le tour du joueur
				message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][1]
				self.MessageATous(message)
		else :
			message = "MSG" + "Mouvement Impossible"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())

			sleep(1)

			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][1]
			self.MessageATous(message)


	def mur(self):
		self.jouer = True
		if Data.maze.murer(self.IndiceClientQuiJoue, Data.connectes[self.IndiceClientQuiJoue][3], Data.connectes[self.IndiceClientQuiJoue][4], self.message[0]):
			self.EnvoieGrille()

			sleep(1)

			message = "MSG" + "La porte a été murée"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			
			sleep(1)

			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][1]
			self.MessageATous(message)
			
		else:
			message = "MSG" + "Murage impossible"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())

			sleep(1)

			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][1]
			self.MessageATous(message)
		

	def cre(self):
		self.jouer = True
		if Data.maze.creuser(self.IndiceClientQuiJoue, Data.connectes[self.IndiceClientQuiJoue][3], Data.connectes[self.IndiceClientQuiJoue][4], self.message[0]):
			self.EnvoieGrille()

			sleep(1)

			message = "MSG" + "Une porte a été crée"
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())
			
			sleep(1)

			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][1]
			self.MessageATous(message)
			
		else:
			message = "MSG" + "Creusage d'une porte impossible."
			Data.connectes[self.IndiceClientQuiJoue][0].send(message.encode())

			sleep(1)

			message = "ETU" + Data.connectes[self.IndiceClientQuiJoue][1]
			self.MessageATous(message)

	def Sortie(self):
		""" Verifie si il y a encore un joueur de connecté
			renvoir False si il y a au moins une personne de connectée, True sinon"""
		nbre = 0
		for l in Data.connectes:
			if l[2]:
				return False
		return True
		