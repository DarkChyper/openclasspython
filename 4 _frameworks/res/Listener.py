#!/usr/bin/env python
# coding: utf-8

# Externe
from socket     import *
from threading  import Thread
# Interne


########## CLASSE LISTENER ##########


class Listener(Thread):
    """Thread chargé d'écouter le serveur."""

    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        """Client"""
        self.connexion = client.connexion
        """Connexion du client au serveur"""
        self.id_ = client.id_
        """Identifiant du client"""


    def run(self):
        while True:
            try:
                msg_recu = self.connexion.recv(1024)
                self._traiter_message(msg_recu.decode())
            except (ConnectionAbortedError, OSError):
                self.client.terminer()

    def _traiter_message(self, msg_recu):
        """
            Contrôle si le message reçu provient bien du joueur courant
            Les données sont du format suivant :
            id:1:map:OOOOOOO(...)
        """
        parse = msg_recu.split(":")

        # Le serveur envoie un message
        if parse[0] == 'Msg':
            self.client.message_label = parse[1]
        # Le serveur envoie une mise à jour de la map...
        if parse[0] == 'Id' and parse[2] == 'Map':
            joueur_courant_id = int(parse[1])
            map_ = parse[3]

            print('map recue')
            # ...on met à jour la map
            self.client.map_label = map_

            # ...on indique si c'est au tour du client
            if joueur_courant_id == self.id_:
                self.client.message_label = "C'est à votre tour"


########## FONCTIONS LISTENER ##########