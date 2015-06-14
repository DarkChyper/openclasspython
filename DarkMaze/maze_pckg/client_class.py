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
	debug = False
	pseudo = ""

	# donnees du réseaux 
	##################################################################################
	hote = "localhost"
	port = 10666
	connexion = None

	# buffer des messages
	##################################################################################
	message_recu = ""
	message_send = ""
	message_affiche = []

	# les locks
	##################################################################################
	verrou_send = RLock()
	verrou_receiv = RLock()
	verrou_grille = RLock()
	verrou_msg = RLock()
	verrou_liste = RLock()

	# donnees des messages
	##################################################################################
	typesOK = ["INI","STR","UTU","OTU","ETU","MSG","GRI","WIN"]
	longMSG = 3      # définit combien de messages sont gardés en mémoire pour l'affichage
	txtGrille = ""   # affichge de la grille
	txtMSG = ""      # affichage des messages du serveur
	txtListe = ""    # affichage de la liste des joueurs
	donnees = ""

	# données de la partie
	##################################################################################
	nonEnd = True # Passe a False lorsque la partie se termine
	init = False  # Passe à True quand il y a assez de joueur pour démarrer 
	start = False # Passe à True quand le serveur démarrer la partie
	exit = False  # Passe à True quand le joueur décide de quitter la partie
	players = []
	utu = False   # définit si c'est le tour du joueur ou non

	# Méthodes
	##################################################################################

	def Messages(tipe, donnees):
		"""
			On définit ici un dictionnaire dont les clefs sont les types de messages
			et les valeurs sont les actions à effectuer, une sorte de switch.
		"""
		with Data.verrou_receiv:
			Data.donnees = donnees
			messagesTypes = { 
			"INI":Data.ini,
			"STR":Data.str,
			"UTU":Data.utu,
			"OTU":Data.otu,
			"MSG":Data.msg,
			"GRI":Data.gri,
			"WIN":Data.win,
			"EXI":Data.exi
			}
			messagesTypes[tipe]()
			Data.donnee = ""

	def gestionMSG(message):
		"""Gère la mémoire des messages à afficher au joueur
		Prend en entrée le message à afficher (donnees) et le nombre d'emplacement mémoire Data.longMSG
		Lorsqu'il y a DATA.longMSG messages dans data.message_affiche, on efface le plus ancien qui sera en position 0"""
		taille = len(Data.message_affiche)
		if taille >= Data.longMSG:
			del Data.message_affiche[0] 
		Data.message_affiche.append(message) # on place les messages dans le buffer
		msgTemp = ""
		for msg in Data.message_affiche:
			msgTemp += msg 
			msgTemp += "\n"
		longueur = len(msgTemp) - 1
		msgTemp = msgTemp[:longueur] # on ne garde pas le dernier saut de ligne
		Data.txtMSG = msgTemp # on affiche les nouveaux messages
		printd(Data.txtMSG)

	def gestionListe():
		""" Crée et modifie la liste des joueurs à afficher et met en avant celui qui doit jouer"""
		message = ""
		for p in Data.players:
			if Data.donnees != "" and p == Data.donnees:
				message += ">>> " + p + "\n"
			else:
				message += p + "\n"
		message = message[:len(message) - 1] # on ne garde pas le dernier saut de ligne
		Data.txtListe = message

	# modules des types possibles
	def ini():
		printd("On a recu INI")
		""" Permet au joueur de lancer la partie """
		Data.init = True

	def str():
		"""Initialise la partie, récupère la liste des pseudos des joueurs dans l'ordre du tour par tour"""
		print("On a recu STR")
		split = str.split(Data.donnees, "|")
		for word in split:
			Data.players.append(word)
		Data.gestionListe()
		Data.start = True

	def utu():
		"""modifie le booleen du tour du joueur à True pour enclencher son tour"""
		printd("On a recu UTU")
		Data.utu = True
		Data.gestionListe(Data.pseudo)
		message = "C'est le début de votre tour !"
		Data.gestionMSG(message) # affichage du message

	def otu():
		""" Gére la réception d'un message indiquant à qui est le tour de jeu"""
		printd("On a recu OTU {}".format(Data.donnees))
		message = "Début du tour de {}".format(Data.donnees)
		Data.gestionMSG(message) # affichage du message
		Data.gestionListe() # modification dans la liste des joueurs pour mettre en avant qui est en train de jouer

	def etu():
		""" Affiche la fin du tour d'un autre joueur"""
		printd("On a recu ETU {}".format(Data.donnees))
		message = "Fin du tour de {}".format(Data.donnees)
		Data.gestionMSG() # affichage du message
		Data.gestionListe()

	def msg():
		printd("On a recu MSG {}".format(Data.donnees))
		""" Transmet le message à l'affichage """
		print("Gestion du message")
		Data.gestionMSG()

	def gri():
		printd("On a recu GRI {}".format(Data.donnees))
		""" Transmet la grille à l'affichage """
		Data.txtGrille = donnees

	def win():
		""" Affiche qui à gagner et enclenche la fin de la partie """
		printd("On a recu WIN {}".format(Data.donnees))
		if Data.donnees == Data.pseudo:
			Data.donnees = "Félicitation, vous avez gagné !!"
		else:
			message = "Désolé, vous avez perdu.\n{} est sorti du labyrinthe avant vous.".format(Data.donnees)
		Data.gestionMSG()

	def exi():
		""" Affiche qui a quitté la partie """
		message = "{} a quitté la partie".format(Data.donnees)


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
					printd(msgBrut)
					if msgBrut[:3] in Data.typesOK:
						leType = msgBrut[:3]
						donnees = msgBrut[3:]
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
			with Data.verrou_send:
				if Data.message_send != "":
					message = Data.message_send.encode()
					Data.connexion.send(message)
					Data.message_send = ""

			sleep(0.08)

def printd(donnees):
	"""Affichage de débogage """
	if Data.debug:
		print(donnees)