#!/usr/bin/env python
# coding: utf-8

# Externe
from socket         import *
from threading      import Thread
# Interne
from res.func       import *
from res.Listener   import Listener
from res.Sender     import Sender

class Client:

    def __init__(self):
        self.connexion = init_connexion_serveur()
        """Connexion avec le serveur"""

        self.id_ = obtenir_id(self.connexion, self.connexion.recv(1024).decode())
        """Identifiant du joueur du client"""

        self.listener = Listener(self.connexion, self.id_)
        """Écoute le serveur"""

        self.sender = Sender(self.connexion, self.id_)
        """Écoute le joueur"""

        # On démarre les écoutes
        self.listener.start()
        self.sender.start()

        # On attend la fin
        self.listener.join()
        self.sender.join()

    def fermer(self):
        try:
            self.connexion.close()
        except:
            pass