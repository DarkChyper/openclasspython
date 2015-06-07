#!/usr/bin/env python
# Coding: utf-8

# Interne
from res.settings   import *

class Joueur:
    """
        Classe objet gérant le joueur (robot) dans ses déplacements.

        L'objet Map repose sur une liste à 2 dimensions, chaque déplacement
        a été développé de sorte que même s'il est trop grand,
        le joueur va le plus loin possible.

        Pour bénéficier de cet avantage, il faut ignorer les exceptions de type IndexError.
        Sinon, il faut catcher les IndexError et utiliser un système de backup de Map.
    """

    def __init__(self, socket, lig_joueur, col_joueur, id_):
        self._lig_joueur = lig_joueur
        """Position de la ligne courante du joueur"""
        self._col_joueur = col_joueur
        """Position de la colonne courante du joueur"""
        self.id_ = id_
        """Identifiant du joueur"""
        self.socket = socket
        """Socket permettant de communiquer avec le client joueur"""

    def se_deplacer(self, map_, type_):
        """
            Effectue un déplacement vers l'Ouest en fonction de la position
            courante du joueur et de la map.
            # ToDo : expliquer le système des dimensions
        """

        # On efface le robot sur la map
        map_[self._lig_joueur][self._col_joueur] = representation['vide']

        # Paramétrage du déplacement
        if type_ == 'o':
            idx_ligne_prochain = self._lig_joueur
            idx_col_prochain = self._col_joueur - 1
        if type_ == 'n':
            idx_ligne_prochain = self._lig_joueur - 1
            idx_col_prochain = self._col_joueur
        if type_ == 'e':
            idx_ligne_prochain = self._lig_joueur
            idx_col_prochain = self._col_joueur + 1
        if type_ == 's':
            idx_ligne_prochain = self._lig_joueur + 1
            idx_col_prochain = self._col_joueur

        # Si c'est un mur ou un autre joueur , on arrête
        if map_[idx_ligne_prochain][idx_col_prochain] in ( representation['mur'], representation['autre_robot'] ):
            map_[self._lig_joueur][self._col_joueur] = representation['autre_robot']
            print('Mur\nProchaine ligne : {}\nProchaine colonne : {}'.format(idx_ligne_prochain,idx_col_prochain)) # DEBUG
            raise(IndexError)
        # Pour le reste, on avance
        else:
            map_[idx_ligne_prochain][idx_col_prochain] = representation['autre_robot']
            self._lig_joueur, self._col_joueur = idx_ligne_prochain, idx_col_prochain

        return map_

    def _retablir_porte(self, map_):
        """
            Remet en place l'éventuelle porte écrasée par le joueur
        """

        # Si une porte a été écrasée...
        if self._porte_courante != None:
            # Variables plus intelligibles
            idx_ligne_porte = self._porte_courante[0]
            idx_col_porte = self._porte_courante[1]

            # ...et qu'elle n'est plus écrasée, on la rétablit
            if map_[idx_ligne_porte][idx_col_porte] != representation['robot_courant']:
                map_[idx_ligne_porte][idx_col_porte] = representation['porte']
                self._porte_courante = None

        return map_

    def envoi_map_client(self, map_, joueur):
        """
            Envoie un ID et la map formatée au client
            Selon l'utilisation, l'ID peut être le tout premier envoyé au joueur
            ou l'ID du joueur_courant de la map
        """

        # On met en évidence le joueur sur la map avec 'X'
        map_.representation_map[self._lig_joueur][self._col_joueur] = representation['robot_courant']

        # On envoie la map au client
        to_send = "Id:{}:Map:{}".format( joueur, map_.__repr__() )
        self.socket.send(to_send.encode())

        # On rétablit le joueur avec 'x'
        map_.representation_map[self._lig_joueur][self._col_joueur] = representation['autre_robot']

    def envoi_message_client(self, balise, msg):
        """
            Envoi un message au client
        """
        try:
            to_send = "{}:{}".format(balise, msg)
            self.socket.send(to_send.encode())
        except:
            pass


    def fermer_connexion(self):
        """
            Si le client est toujours connecté,
            on le prévient et on ferme la connexion
        """
        try:
            self.envoi_message_client("Sys","quit")
            self.socket.close()
        except:
            pass