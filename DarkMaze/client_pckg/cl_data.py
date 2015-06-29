#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
Contient les données de connexion, les verrous Rlock, les boolées et variables d'une partie côté client
"""

# Imports externes
import socket
from threading import Thread, RLock
from time import *
from tkinter import *

# Imports internes


class Data():
	"""
		Classe qui contient toutes les données nécessaire au client
	"""
	debug = True
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
	typesOK = ["INI","STR","WTU","ETU","MSG","GRI","WIN"]
	longMSG = 5      # définit combien de messages sont gardés en mémoire pour l'affichage
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
	isutu = False   # définit si c'est le tour du joueur ou non

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
			"WTU":Data.wtu,
			"ETU":Data.etu,
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
		#msgTemp = msgTemp[:longueur] # on ne garde pas le dernier saut de ligne
		with Data.verrou_msg:
			Data.txtMSG = msgTemp # on affiche les nouveaux messages

	def gestionListe():
		""" Crée et modifie la liste des joueurs à afficher et met en avant celui qui doit jouer"""
		message = ""
		for p in Data.players:
			if Data.donnees != "" and p == Data.donnees:
				message += ">>> " + p + "\n"
			else:
				message += p + "\n"
		message = message[:len(message) - 1] # on ne garde pas le dernier saut de ligne
		with Data.verrou_liste:
			Data.txtListe = message

	# modules des types possibles
	def ini():
		""" Permet au joueur de lancer la partie """
		Data.init = True

	def str():
		"""Initialise la partie, récupère la liste des pseudos des joueurs dans l'ordre du tour par tour"""
		Data.init = False
		with Data.verrou_msg :
			Data.gestionMSG("******************")
			Data.gestionMSG("DEBUT DE LA PARTIE")
			Data.gestionMSG("******************")
		split = str.split(Data.donnees, ";")
		for word in split:
			Data.players.append(word)
		Data.donnees = ""
		Data.gestionListe()
		Data.start = True

	def wtu():
		""" Gére la réception d'un message indiquant à qui est le tour de jeu"""
		Data.gestionListe()
		if Data.donnees == Data.pseudo:
			Data.isutu = True
			
			message = "C'est le début de votre tour !"
			Data.gestionMSG(message) # affichage du message
		else:
			Data.isutu = False
			message = "C'est le début du tour de {} !".format(Data.donnees)
			Data.gestionMSG(message) # affichage du message

	def etu():
		""" Affiche la fin du tour d'un autre joueur"""
		message = "Fin du tour de {}".format(Data.donnees)
		Data.gestionMSG(message) # affichage du message
		Data.gestionListe()

	def msg():
		""" Transmet le message à l'affichage """
		Data.gestionMSG(Data.donnees)

	def gri():
		""" Transmet la grille à l'affichage """
		Data.txtGrille = Data.donnees

	def win():
		""" Affiche qui à gagner et enclenche la fin de la partie """
		if Data.donnees == Data.pseudo:
			Data.donnees = "Félicitation, vous avez gagné !!"
			Data.isutu = False
		else:
			Data.donnees = "Désolé, vous avez perdu.\n{} est sorti du labyrinthe avant vous.".format(Data.donnees)
		Data.gestionMSG(Data.donnees)
		Data.gestionMSG("****************")
		Data.gestionMSG("FIN DE LA PARTIE")
		Data.gestionMSG("****************")

	def exi():
		""" Affiche qui a quitté la partie """
		message = "{} a quitté la partie".format(Data.donnees)
