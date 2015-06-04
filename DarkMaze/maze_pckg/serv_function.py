#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Module comprenant les fonctions principales du serveur
"""

# Imports internes
from .serv_class import *

def initGame():
	""" On initilise le jeu en demandant de choisir la carte à jouer"""
	mazes = initMazes()
	print("Voici la liste des labyrinthes disponibles :")
	x = 1
	liste = list()
	for maze in range(len(mazes)):
		print(" {}. {}".format(x, mazes[maze].nom))
		liste.append(str(x))
		x += 1

	while 1:
		choix = input("Quel Labyrinthe voulez-vous résoudre ? ")
		if choix in liste:
			Data.maze = mazes[int(choix)-1]
			break


def initMazes():
	""" 
		On récupère les cartes au format txt dan le dossier ./maze_cartes
		On les charge dans le jeu sous forme d'une liste d'objets maze
		On retourne cette liste au programme principale
	"""
	mazes = []
	for nom_fichier in os.listdir("maze_cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("maze_cartes", nom_fichier)
			nom_maze = nom_fichier[:-4].lower()
			with open(chemin, "r") as fichier:
				grille = fichier.read()
				maze = Maze(nom_maze,grille)
				mazes.append(maze)
	return mazes


def getClient():
	client_temp = []
	while Data.getClient:
		# On va vérifier que de nouveaux clients ne demandent pas à se connecter
		connexions_demandees, wlist, xlist = select.select([Data.connexion], [], [], 0.05)
		
		for connexion in connexions_demandees:
			connexion_avec_client, infos_connexion = connexion.accept()
			# On ajoute le socket connecté à la liste des clients
			Data.clients_connectes.append(connexion_avec_client)
			client_temp.append(connexion_avec_client)


		# on compte combien il y a de client(s) connecté(s)
		nombre = len(Data.clients_connectes)
		if nombre > 1:
			# on commence par dire aux connectes qu'ils peuvent commencer la partie
			for client in client_temp:
				message = "Il y a " + str(nombre) + " connectés sur le serveur\nTapez c pour commencer la partie"
				client.send(message.encode())
			client_temp = []

			# on essaye de voir si un joueur a lancer la partie
			clients_a_lire = []
			try:
				clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
			except select.error:
				pass
			else:
				for client in clients_a_lire:
					msg_recu = client.recv(1024).decode()
					if msg_recu.lower() == "c":
						Data.getClient = False
	print("Le jeu commence !")