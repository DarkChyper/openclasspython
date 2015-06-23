#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""

"""


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



class NewClient(Data):
	"""	Classe définissant le thread qui va ajouter des nouvelles connexions tant que c'est possible"""

	def __init__(self):
		liste_temp = []
		i = 0 # compteur de joueur connectes pour éviter d'avoir plusieurs pseudonymes par defaut identiques
		while Data.addClient:
			# On va vérifier que de nouveaux clients ne demandent pas à se connecter
			connexions_demandees, wlist, xlist = select.select([Data.connexion], [], [], 0.05)

			for connexion in connexions_demandees:
				connexion_avec_client, infos_connexion = connexion.accept()
				joueur = []
				joueur.append(connexion_avec_client)
				joueur.append("NoName{}".format(str(i))) # le pseudonyme sera définit plus tard
				i += 1
				joueur.append(True) 
				x, y = definePosJoueur() # on place au hasard le joueur
				joueur.append(x)
				joueur.append(y)
				joueur.append(False) # le joueur ne peut être placé sur une porte dès le début.
				Data.connectes.append(joueur)
				liste_temp.append(connexion_avec_client) # une liste des clients temporaire pour envoyer une seule fois le message "La partie peut commencer"
				Data.clients_connectes.append(connexion_avec_client) 

			nombre = len(Data.connectes)
			if nombre >= Data.nbrJoueursMin: # on ne peut lancer la partie que si il y a au moins n joueurs
				for temp in liste_temp:
					message = ""
					message = "MSGIl y a " + str(nombre) + " connectés sur le serveur\nCliquez sur \"Commencer\" pour commencer la partie"
					temp.send("INI".encode())
					sleep(2)
					temp.send(message.encode())
				liste_temp = []

				# On vérifie si un joueur déja connecté veut lancer la partie
				clients_a_lire = []
				try:
					clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
				except select.error:
					pass
				else:
					for client in clients_a_lire: # pour chaque connexion avec le client dans la liste de client à lire
						if Data.connectes[Data.clients_connectes.index(client)][2]:
							msg_recu = client.recv(1024).decode()
							Data.printd(msg_recu)
							if msg_recu[:3] == "INI":
								Data.addClient = False
								break
							if msg_recu[:3] == "PSD": # si on veut mettre à jour un pseudo
								Data.connectes[Data.clients_connectes.index(client)][1] = msg_recu[3:]
		# on attend l'arrivée des pseudosnymes de tous les joueurs connectés
		null = askPseudo()
