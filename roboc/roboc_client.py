#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_client_class import *
from roboc_client_interf import *

network = Network()

#initialisation des threads
datareceive = DataReceive()
affichage = Affichage()

#lancement des threads
datareceive.start()
affichage.start()

#attente de l'arrêt des thread
datareceive.join()
affichage.join()

network.deco()


