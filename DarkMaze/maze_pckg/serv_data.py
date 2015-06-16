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
	nbrJoueursMin = 2
	maze = None #contient les données du labyrinthe en cours, class Maze

	connectes = [] #liste contenant les clients dans l'ordre de jeu, définition dans le ReadMe
	clients_connectes = [] # liste contenant les infos de connexion de chaque joueur dans l'ordre de connexion

	# Les méthodes 
	#######################################################################
	def listePseudo(self):
		pseudo = ""
		pseudo += "STR"
		for cl in Data.connectes:
			pseudo += Data.connectes[cl][1] 
			pseudo += ";"
		return pseudo


