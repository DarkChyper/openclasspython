#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# Imports externes :
import socket
import select

"""
	Module qui contient les fonctions propre au serveur
	Initialisation de la connexion
	Initialisation des connexions des joueurs
	Les échanges de la partie
	Gestion des déconnexions
"""

def initServ():
	hote = ''
	port = 10666

	connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connexion_principale.bind((hote, port))
	connexion_principale.listen(5)

	print("Le serveur écoute à présent sur le port {}".format(port))

	return connexion_principale

def getClient(connexion_principale):
	attente_client = True
	clients_connectes = []
	affiche = True
	while attente_client:
		# On va vérifier que de nouveaux clients ne demandent pas à se connecter
		connexions_demandees, wlist, xlist = select.select([connexion_principale], [], [], 0.05)
		
		for connexion in connexions_demandees:
			connexion_avec_client, infos_connexion = connexion.accept()
			# On ajoute le socket connecté à la liste des clients
			print(infos_connexion)
			print(connexion_avec_client)
			clients_connectes.append(connexion_avec_client)

		# on compte combien il y a de client(s) connecté(s)
		nombre = len(clients_connectes)
		
		if nombre > 1 and affiche:
			for i in clients_connectes:
				print(i)
				print("\n\n")
			affiche = False