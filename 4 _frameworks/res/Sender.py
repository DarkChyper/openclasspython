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
            msg = "Id:{}:Type:{}:Lg:{}".format(self.id_, msg_a_envoyer[0], msg_a_envoyer[1])
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

        # Si le premier caractère est correct
        if len(entree) != 0 and entree[0] in touches.values():
            type_deplacement = entree[0]

            # Si le reste est un nombre
            try:
                lg = int(entree[1:])
            except:
                # Si aucune longueur n'est indiquée ou égale à 0
                if entree[1:].strip() == '' or entree[1:].strip() == '0':
                    lg = 1
                else:
                    return None

            return type_deplacement, lg

        return None