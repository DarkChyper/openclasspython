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
        partie.start()
        tempo = False

#join est bloquant jusqu'à la fermeture les 2 processus
listenclients.join()
msgclients.join()
partie.join()

network.decotot()
