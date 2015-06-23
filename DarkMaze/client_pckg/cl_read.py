#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
import socket
from threading import Thread, RLock
from time import *
from tkinter import *

# Imports internes
from .cl_partie import *
from .cl_data import *
from .cl_function import *

class ConnexionRead(Thread, Data):
	"""
		Class qui va lire les données en provenance du serveur
	"""
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while Data.nonEnd:
			with Data.verrou_receiv:
				# On commence par vérifier si il y a des messages en arrivée
				Data.msg_recu = Data.connexion.recv(1024)

				# On traite le message si il n'est pas vide
				if Data.msg_recu != "":
					msgBrut = Data.msg_recu.decode()
					
					if msgBrut[:3] in Data.typesOK:
						printd(msgBrut) ##AFFICHAGE DE DEBUG
						leType = msgBrut[:3]
						donnees = msgBrut[3:]
						Data.Messages(leType, donnees)

			# On attend 50 ms
			sleep(0.05)