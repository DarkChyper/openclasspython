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

	Pseudo()

	Connexion()

	thread_send = ConnexionWrite()
	thread_receiv = ConnexionRead()
	thread_affiche = Interface()

	thread_send.start()
	thread_receiv.start()
	thread_affiche.start()

	thread_send.join()
	thread_receiv.join()
	thread_affiche.join()



if __name__ == "__main__":
    main()


