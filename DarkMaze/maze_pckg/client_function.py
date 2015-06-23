#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
import socket
from time import *

# Imports internes
from .client_class import *
from .client_affichage import *

def Pseudo():
	"""
		On va demander au joueur de s'identifier
	"""
	while 1:
		pseudo = input("Quel est votre pseudonyme ? : ")
		if pseudo != "":
			Data.pseudo = pseudo
			break

def Connexion():
	"""
		Fonction qui lance la connexion au serveur
	"""

	Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	Data.connexion.connect((Data.hote, Data.port))
	print("Connexion établie avec le serveur sur le port {}".format(Data.port))
	sleep(1)
	message = "PSD" + Data.pseudo
	message = message.encode()
	Data.connexion.send(message)

def Deconnexion(turn=False):
	if turn:
		with Data.verrou_send:
			Data.message_send = "EXI" + Data.pseudo
			sleep(1)
	Data.nonEnd = False
	sleep(2)
	Data.connexion.close()
	


def printd(donnees):
	""" Affichage de débogage """
	if Data.debug:
		print(donnees)
