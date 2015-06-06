#!/usr/bin/env python
# coding: utf-8

# Externe
from socket     import *
from threading  import Thread
# Interne
from res.func       import *

class Listener(Thread):
    """Thread chargé d'écouter le serveur."""

    def __init__(self, connexion, id_):
        Thread.__init__(self)
        self.connexion = connexion
        """Connexion du client au serveur"""
        self.id_ = id_
        """Identifiant du client"""

    def run(self):
        while True:
            try:
                msg_recu = self.connexion.recv(1024)
                traiter_message()
            except:
                exit(0)