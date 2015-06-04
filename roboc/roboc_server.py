#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_server_class import *
from roboc_server_jeu import *

#ouverture de la connection
network = Network()

préparation Threads et classes
listenclients = NewClient()
msgclients = DataExchange()
carte = Carte()
partie = Partie()

#définition des paramètres de la partie
carte.Definition()
carte.ChargeCarte()

#début d'écoute
listenclients.start()
msgclients.start()

#fin d'écoute des nouveaux clients et début de la partie
partie.start()

#join est bloquant jusqu'à la fermeture des processus
listenclients.join()
msgclients.join()
partie.join()

network.decotot()
