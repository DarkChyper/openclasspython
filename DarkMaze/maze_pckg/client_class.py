#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
from threading import Thread, RLock
from time import *

# Imports interne



class Data():
	"""
		Classe qui contient toutes les données nécessaire au client
	"""
	pseudo = ""

	# donnees du réseaux 
	hote = "localhost"
	port = 10666
	connexion = None

	# buffer des messages
	message_recu = ""
	message_send = ""
	message_affiche = []

	# donnees des messages
	typesOK = [INI,STR,UTU,OTU,ETU,MSG,GRI,WIN]
	longMSG = 3      # définit combien de messages sont gardés en mémoire pour l'affichage
	txtGrille = ""   # affichge de la grille
	txtMSG = ""      # affichage des messages du serveur
	txtListe = ""    # affichage de la liste des joueurs


	# données de la partie
	nonEnd = True # Passe a False lorsque la partie se termine
	init = False  # Passe à True quand il y a assez de joueur pour démarrer 
	start = False # Passe à True quand le serveur démarrer la partie
	players = []
	utu = False   # définit si c'est le tour du joueur ou non

	partie = False

	def Messages(tipe, donnees):
		"""
			On définit ici un dictionnaire dont les clefs sont les types de messages
			et les valeurs sont les actions à effectuer, une sorte de switch.
		"""
		messagesTypes = { 
		"INI" = Data.ini(),
		"STR" = Data.str(donnees),
		"UTU" = Data.utu(),
		"OTU" = Data.otu(donnees),
		"MSG" = Data.msg(donnees),
		"GRI" = Data.gri(donnees),
		"WIN" = Data.win(donnees)
		}
		messagesTypes[tipe]

	# modules communs aux différents types
	def gestionMSG(donnees):
		"""Gère la mémoire des messages à afficher au joueur
		Prend en entrée le message à afficher (donnees) et le nombre d'emplacement mémoire Data.longMSG
		Lorsqu'il y a DATA.longMSG messages dans data.message_affiche, on efface le plus ancien qui sera en position 0"""
		taille = len(Data.message_affiche)
		if taille >= Data.longMSG:
			del message_affiche[0] 
		Data.message_affiche.append(donnees) # on place les messages dans le buffer
		msgTemp = ""
		for msg in Data.message_affiche:
			msgTemp += msg = "\n"
		msgTemp = msgTemp(:len(msgTemp) - 1) # on ne garde pas le dernier saut de ligne
		Data.txtMSG = msgTemp # on affiche les nouveaux messages

	def gestionListe(pseudo=None):
		""" Crée et modifie la liste des joueurs à afficher et met en avant celui qui doit jouer"""
		message = ""
		for p in Data.players:
			if pseudo != None and p == pseudo:
				message += ">>> " + pseudo + "\n"
			else: 
				message += pseudo + "\n"
		message = message[:len(message) - 1] # on ne garde pas le dernier saut de ligne
		Data.txtListe = message

	# modules des types possibles
	def ini():
		""" Permet au joueur de lancer la partie """
		Data.init = True

	def str(donnees):
		"""Initialise la partie, récupère la liste des pseudos des joueurs dans l'ordre du tour par tour"""
		split = str.split(donnees, "|")
		for word in split:
			Data.players.append(word)
		gestionListe()
		Data.start = True

	def utu():
		"""modifie le booleen du tour du joueur à True pour enclencher son tour"""
		Data.utu = True
		gestionListe(Data.pseudo)

	def otu(donnees):
		""" Gére la réception d'un message indiquant à qui est le tour de jeu"""
		message = "Début du tour de {}".format(donnees)
		gestionMSG(message) # affichage du message
		gestionListe(donnees) # modification dans la liste des joueurs pour mettre en avant qui est en train de jouer

	def etu(donnees):
		""" Affiche la fin du tour d'un autre joueur"""
		message = "Fin du tour de {}".format(donnees)
		gestionMSG(message) # affichage du message
		gestionListe()

	def msg(donnees):
		""" Transmet le message à l'affichage """
		gestionMSG(donnees)

	def gri(donnees):
		""" Transmet la grille à l'affichage """
		Data.txtGrille = donnees

	def win(donnees):
		""" Affiche qui à gagner et enclenche la fin de la partie """
		if donnees == Data.pseudo:
			message = "Félicitation, vous avez gagné !!"
		else:
			message = "Désolé, vous avez perdu.\n{} est sorti du labyrinthe avant vous.".format(donnees)
		gestionMSG(message)

		Data.nonEnd = False # on arrête la partie

class ConnexionRead(Thread, Data):
	"""
		Class qui va lire les données en provenance du serveur
	"""
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		while Data.nonEnd:
			# On commence par vérifier si il y a des messages en arrivée
			Data.msg_recu = connexion_avec_serveur.recv(1024)

			# On traite le message si il n'est pas vide
			if Data.msg_recu != "":
				msgBrut = Data.msg_recu.decode()
				if msgBrut[:3] in Data.typesOK:
					leType = msgBrut[:3]
					donnees = msgBrut[2:]
					Data.Messages(leType, donnees)

			# On attend 50 ms
			sleep(0.05)

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