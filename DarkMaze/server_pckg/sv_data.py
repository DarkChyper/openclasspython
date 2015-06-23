#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# Imports externes
import os
import socket
import select
from threading import Thread, RLock

# Imports internes

class Data():
	"""
		classe contenant les données globales
	"""
	DEBUG = True

	# Le réseau 
	#######################################################################
	hote = ''
	port = 10666
	connexion = None

	# Booleens
	#######################################################################
	addClient = True # passer a False quand la partie commencera
	nonEnd = True # passera à False quand la partie se terminera

	# Options systeme du jeu
	#######################################################################
	listeMsgOkNonJoueur = ["PSD","MSG","EXI"] 				# définit quelles actions le joueur peut faire durant le tour d'un concurent
	listeMsgOk = ["PSD","MSG","MVT","MUR", "CRE", "EXI"]	# définit quelles actions le joueur peut faire durant son tour


	# La partie
	#######################################################################
	nbrJoueursMin = 1
	maze = None #contient les données du labyrinthe en cours, class Maze

	connectes = [] #liste contenant les clients dans l'ordre de jeu, définition dans le ReadMe
	clients_connectes = [] # liste contenant les infos de connexion de chaque joueur dans l'ordre de connexion

	# Les méthodes 
	#######################################################################
	def listePseudo():
		pseudo = ""
		pseudo += "STR"
		nbre = len(Data.clients_connectes)
		liste = range(nbre)
		for cl in liste:
			pseudo += Data.connectes[cl][1] 
			pseudo += ";"
		return pseudo

	def printd(message):
		if Data.DEBUG:
			print(message)
			

class Connexion(Data):
	"""
		ensemble des méthodes concernant les connexion TCP
	"""
	def __init__(self):
		Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		while 1:
			try :
				Data.connexion.bind((Data.hote, Data.port))
			except OSError: # si on relance trop vite le serveur et que la connexion est deja utilisée, on boucle
				pass
			else:
				break
		Data.connexion.listen(5)
		print("Le serveur écoute à présent sur le port {}".format(Data.port))
		