#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Programme principal qui fait tourner le serveur du jeu
	de labyrinthe pour OpenClassRooms
"""

# Imports externes
from socket import *
from time import *

# Imports internes
from maze_pckg.serv_function import *
from maze_pckg.serv_class import *

# Début du programme
def main():
	"""
		Coeur du serveur, tant que l'on ne quitte pas ce main,
		on reste dans le jeu
	"""
	# Initialisation du serveur
	initGame()
	
	# démarrage du serveur
	connexion = Connexion()

	# On lance le thread pour accepter les nouveaux clients
	new = NewClient()

	# On lance le thread principal du serveur
	thread_game = Partie()
	thread_game.start()
	thread_game.join()

	



if __name__ == "__main__":
    main()