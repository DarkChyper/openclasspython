#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from roboc_server_class import *

network = Network()

listenclients = NewClient()
msgclients = DataExchange()

listenclients.start()
msgclients.start()

#join est bloquant jusqu'à la fermeture les 2 processus
listenclients.join()
msgclients.join()

network.decotot()
