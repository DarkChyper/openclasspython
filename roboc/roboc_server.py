#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_server_class import *
from roboc_server_jeu import *

network = Network()

listenclients = NewClient()
msgclients = DataExchange()
partie = Partie()

listenclients.start()
msgclients.start()

tempo = True
while tempo == True:
    if len(Data.clients_connectes) > 0:
        carte = Carte()
        tempo = False
        
tempo = True
while tempo == True:
    DataCarte.numcarte = Data.choix
    if DataCarte.numcarte != "":
        Carte.ChargeCarte()
        tempo = False

partie.start()

#join est bloquant jusqu'à la fermeture les 2 processus
listenclients.join()
msgclients.join()
partie.join()

network.decotot()
