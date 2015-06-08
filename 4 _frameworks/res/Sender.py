#!/usr/bin/env python
# coding: utf-8

# Externe
from socket         import *
# Interne
from res.settings   import *


########## CLASSE SENDER ##########


class Sender:
    """Classe chargée d'envoyer les entrées utilisateur au serveur"""

    def __init__(self, client):
        self.client = client
        """Client"""
        self.connexion = client.connexion
        """Connexion du client au serveur"""
        self.id_ = client.id_
        """Identifiant du client"""

    def send(self, msg_a_envoyer):
        msg_a_envoyer = msg_a_envoyer.get()

        # On quitte
        if msg_a_envoyer == touches['quit']:
            self.client.terminer()

        # On envoie le début de partie
        if msg_a_envoyer == touches['commencer']:
            print(msg_a_envoyer)
            self.connexion.send(msg_a_envoyer.encode())
            print("Message envoyé : {}".format(msg_a_envoyer)) # DEBUG
            return None

        msg_a_envoyer = self._entree_correcte(msg_a_envoyer)
        if msg_a_envoyer != None:
            msg = "Id:{}:Type:{}".format(self.id_, msg_a_envoyer)
            try:
                self.connexion.send(msg.encode())
                print("Message envoyé : {}".format(msg_a_envoyer)) # DEBUG
                self.client.message_label = "Ce n'est plus à votre tour"
            except (ConnectionAbortedError, OSError):
                self.client.terminer()

    def _entree_correcte(self, entree):
        """
            Renvoie le type de déplacement et la longueur
            ou None si l'entrée est incorrecte.
            Si l'utilisateur demande de l'aide, on renvoie entree
        """

        if entree[0] in touches.values() and ( len(entree[1:]) == 0 or entree[1] in touches.values() ):
            return entree

        return None