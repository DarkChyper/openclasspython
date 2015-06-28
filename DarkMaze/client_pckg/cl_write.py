#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Définition du Thread d'écriture.
	Une fois la partie lancée, il va envoyé les messages 
	contenus dans le buffer Data.message_send vers le serveur de jeu.
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

class ConnexionWrite(Thread, Data):
	"""
		Class qui va envoyer des messages au serveur
	"""
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while Data.nonEnd:
			with Data.verrou_send:
				if Data.message_send != "":
					printd("SEND => {}".format(Data.message_send))
					message = Data.message_send.encode()
					Data.connexion.send(message)
					Data.message_send = ""

			sleep(0.08)
			if not Data.nonEnd:
				printd("WRITE => {}".format(Data.nonEnd))