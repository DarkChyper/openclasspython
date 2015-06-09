#!/usr/bin/env python
# coding: utf-8

# Externe
from socket         import *
# Interne
from res.settings   import *


########## CLASSE SENDER ##########


class Sender:
    """
        Classe chargée de contrôler et
        d'envoyer les entrées utilisateur au serveur
    """

    def __init__(self, client):
        self.client = client
        """Client"""
        self.connexion = client.connexion
        """Connexion du client au serveur"""
        self.id_ = client.id_
        """Identifiant du client"""

    def send(self, msg_a_envoyer):
        """
            Définit les actions à faire en fonction de l'entrée utilisateur
        """

        msg_a_envoyer = msg_a_envoyer.get()

        # On quitte
        if msg_a_envoyer == touches['quit']:
            self.client.terminer()

        # On envoie le début de partie
        if msg_a_envoyer == touches['commencer']:
            print(msg_a_envoyer)
            self.connexion.send(msg_a_envoyer.encode())
            return None

        msg_a_envoyer = self._entree_correcte(msg_a_envoyer)
        if msg_a_envoyer != None:
            msg = "Id:{}:Type:{}".format(self.id_, msg_a_envoyer)
            try:
                self.connexion.send(msg.encode())
                self.client.message_label = "Ce n'est plus à votre tour"
            except (ConnectionAbortedError, OSError):
                self.client.terminer()

    def _entree_correcte(self, entree):
        """
            Renvoie le type de déplacement ou None si l'entrée est incorrecte.
        """
        # On détermine si c'est une action spéciale
        premier_caractere_ok = len(entree) == 2 and entree[0] in ( touches['murer'], touches['percer'] )
        second_caractere_ok = len(entree) == 2 and entree[1] in ( touches['ouest'], touches['nord'], touches['est'], touches['sud'] )

        est_action_speciale =  premier_caractere_ok and second_caractere_ok

        if ( len(entree) == 1 and entree[0] in touches.values() ) or est_action_speciale:
            return entree

        return None