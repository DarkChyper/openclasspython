#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
import socket

# Imports internes
from .client_class import *

def Connexion():
	"""
		Fonction qui lance la connexion au serveur
	"""

	Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Data.connexion.connect((Data.hote, Data.port))
	print("Connexion établie avec le serveur sur le port {}".format(Data.port))

	message = ""
	while message == "":
		message = Data.connexion.recv(1024).decode()

	print(message)