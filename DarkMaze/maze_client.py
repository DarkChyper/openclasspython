#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
import socket
from threading import Thread, RLock

# Imports internes
from maze_pckg.client_affichage import *
from maze_pckg.client_class import *
from maze_pckg.client_function import *

# Début du programme
def main():
	# On demande au joueur de s'identifier
	Pseudo()

	# Connexion au serveur de jeu
	Connexion()

	# Préparation des processus
	thread_send = ConnexionWrite()
	thread_receiv = ConnexionRead()
	thread_affiche = Affichage()

	# Lancement des processus
	thread_send.start()
	thread_receiv.start()
	thread_affiche.start()

	# Attente de fin des processus
	thread_send.join()
	thread_receiv.join()
	thread_affiche.join()



if __name__ == "__main__":
    main()


