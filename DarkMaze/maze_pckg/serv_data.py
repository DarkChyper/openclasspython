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

	# La partie
	#######################################################################
	nbrJoueursMin = 2
	maze = None #contient les données du labyrinthe en cours, class Maze

	connectes = [] #liste contenant les client dans l'ordre de jeu, définition dans le ReadMe


