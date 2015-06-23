#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# Imports externes
import os
import socket
import select
from threading import Thread, RLock
from random import randrange
from time import *
import re

# Imports internes
from sv_data import *
from sv_maze import *

class Connexion(Data):
	"""
		ensemble des méthodes concernant les connexion TCP
	"""
	def __init__(self):
		Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		while 1:
			try :
				Data.connexion.bind((Data.hote, Data.port))
			except OSError: # si on relance trop vite le serveur et que la connexion est deja utilisée, on boucle
				pass
			else:
				break
		Data.connexion.listen(5)
		print("Le serveur écoute à présent sur le port {}".format(Data.port))

def askPseudo():
	""" Fonction qui oucle tant que tous les joueurs n'ont pas envoyer leur pseudo"""
	while 1: # on boucle tant que tous les joueurs connectes n'ont pas envoyé leur pseudonyme
			sortie = True
			expression = "^(NoName)[0-9]{1:}$"
			for client_a_verifier in Data.connectes:
				pseudo = client_a_verifier[1]
				if re.match(expression, pseudo):
					sortie = False
					break

			if sortie:
				return 0
			else :
				clients_a_lire = []
				try:
					clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
				except select.error:
					pass
				else:
					for client in clients_a_lire: # pour chaque connexion avec le client dans la liste de client à lire
						if Data.connectes[Data.clients_connectes.index(client)][2]:
							msg_recu = client.recv(1024).decode()
							if msg_recu[:3] == "PSD": # si on veut mettre à jour un pseudo
								Data.connectes[Data.clients_connectes.index(client)][1] = msg_recu[3:]


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

def definePosJoueur():
		"""On place le joueur au hasard sur la map"""
		longueur = Data.maze.dim[0]
		largeur = Data.maze.dim[1]
		while 1:
			x = randrange(longueur)
			y = randrange(largeur)
			case = Data.maze.grille[y][x]
			if case != "O" and case != "." and case != "U" :
				dejapris = False
				t = (x,y)
				nbreJoueurs = len(Data.connectes)
				liste = range(nbreJoueurs)
				for joueur in liste:
					T = (Data.connectes[joueur][3],Data.connectes[joueur][4])
					if T == t:
						dejapris = True
				if dejapris == False :
					Data.printd("x={};y={}".format(str(x),str(y)))
					return x, y

def majPseudo(self, client, pseudo):
	"""Fonction pour mettre a jour le pseudo d'un joueur"""
	for i in Data.connectes :
		if Data.connectes[i][0] == client:
			Data.connectes[i][1] = pseudo
			break