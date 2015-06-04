#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
from threading import Thread, RLock

# Imports interne



class Data():
	"""
		Classe qui contient toutes les données nécessaire au client
	"""
	hote = "localhost"
	port = 10666
	connexion = None
	nonEnd = True # Passe a False lorsque la partie se termine
	message_recu = ""
	message_send = ""
	partie = False

class ConnexionRead(Thread, Data):
	"""
		Class qui va lire les données en provenance du serveur
	"""
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while Data.nonEnd:
			pass


class ConnexionWrite(Thread, Data):
	"""
		Class qui va envoyer des messages au serveur
	"""
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while Data.nonEnd:
			if Data.message_send != "":
				message = Data.message_send.encode()
				Data.connexion.send(message)
				Data.message_send = ""