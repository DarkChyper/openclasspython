#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_client_class import *
from roboc_client_interf import *

network = Network()

#initialisation des threads
#datasend = DataSend()
datareceive = DataReceive()
affichage = Affichage()

#lancement des threads
#datasend.start()
affichage.start()
datareceive.start()

#attente de l'arrêt des thread
#datasend.join()
datareceive.join()
affichage.join()

network.deco()


