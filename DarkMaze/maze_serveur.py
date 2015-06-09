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

	initGame()

	connexion = Connexion()

	getClient()
	while 1:
		clients_a_lire = []
		try:
			clients_a_lire, wlist, xlist = select.select(Data.clients_connectes,[], [], 0.05)
		except select.error:
			send = input("> ")
			if send != "":
				send = send.encode()
				client.send(send)
		else:
			# On parcourt la liste des clients à lire
			for client in clients_a_lire:
				# Client est de type socket
				msg_recu = client.recv(1024)
				# Peut planter si le message contient des caractères spéciaux
				msg_recu = msg_recu.decode()
				print("Reçu {}".format(msg_recu))
				send = input("> ")
				if send != "":
					send = send.encode()
					client.send(send)
				
		sleep(0.05)


if __name__ == "__main__":
    main()