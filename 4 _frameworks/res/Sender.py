#!/usr/bin/env python
# coding: utf-8

# Externe
from socket         import *
from threading      import Thread, RLock
# Interne
from res.func       import *
from res.settings   import *

verrou = RLock()

class Sender(Thread):
    """Thread chargé d'envoyer les entrées utilisateur au serveur"""

    def __init__(self, connexion, id_):
        Thread.__init__(self)
        self.connexion = connexion
        """Connexion du client au serveur"""
        self.id_ = id_
        """Identifiant du client"""

    def run(self):
        msg_a_envoyer = ""
        while True:
            with verrou:
                msg_a_envoyer = input("> ")

            print(msg_a_envoyer)

            # On quitte
            if msg_a_envoyer == touches['quit']:
                self.terminer()

            # On envoie le début de partie
            if msg_a_envoyer == touches['commencer']:
                self.connexion.send(msg_a_envoyer.encode())
                continue

            msg_a_envoyer = entree_correcte(msg_a_envoyer)
            if msg_a_envoyer != None:
                msg = "id:{}:type:{}:lg:{}".format(msg_a_envoyer[0], msg_a_envoyer[1])
                self.connexion.send(msg.encode())

    def terminer(self):
        print('terminer') # DEBUG
        self.connexion.close()
        exit(0)