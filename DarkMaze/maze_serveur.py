#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Programme principal qui fait tourner le serveur du jeu
	de labyrinthe pour OpenClassRooms
"""

# Imports externes

# Imports internes
from maze_pckg.serv_function import *
from maze_pckg.serv_class import *

# Début du programme
def main():
	"""
		Coeur du serveur, tant que l'on ne quitte pas ce main,
		on reste dans le jeu
	"""

	initGame()

	connexion = Connexion()

	getClient()

if __name__ == "__main__":
    main()