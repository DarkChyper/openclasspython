#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
	Roboc_serveur.py est le serveur faisant tourner le jeu de labyrinthe 
	pour OpenClassRooms
"""

# Imports externes
import signal
import socket
import select
import os

import time
import datetime

from threading import Thread, RLock
import random

# Imports internes
from maze_lib.serv_function import *
from maze_lib.serv_class import *
from maze_lib.serv_serv import *

def main():
	"""
		Coeur du serveur, tant que l'on ne quitte pas ce main,
		on reste dans le jeu
	"""
	maze = initGame()

	connexion_principale = initServ()

	clients = getClient(connexion_principale)


if __name__ == "__main__":
    main()