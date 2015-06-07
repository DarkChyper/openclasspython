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

    def __init__(self, map_):
        self._position_courante = (0,0)
        """_position_courante (ligne, colonne): Position courante du joueur"""

        self._porte_courante = None
        """_porte_courante: Position d'une porte écrasée par le joueur"""

        self._evaluer_position_joueur(map_)

    def se_deplacer(self, map_, type_):
        """
            Effectue un déplacement vers l'Ouest en fonction de la position
            courante du joueur et de la map.

            Vers l'Est, on joue sur les ordonnées (2nde dimension)
            en reculant (-).
        """

        # On efface le robot sur la map
        map_[self._position_courante[0]][self._position_courante[1]] = representation['vide']


        # Paramétrage du déplacement
        if type_ == 'o':
            idx_ligne_prochain = self._position_courante[0]
            idx_col_prochain = self._position_courante[1] - 1
        if type_ == 'n':
            idx_ligne_prochain = self._position_courante[0] - 1
            idx_col_prochain = self._position_courante[1]
        if type_ == 'e':
            idx_ligne_prochain = self._position_courante[0]
            idx_col_prochain = self._position_courante[1] + 1
        if type_ == 's':
            idx_ligne_prochain = self._position_courante[0] + 1
            idx_col_prochain = self._position_courante[1]

        # ...est un mur, on arrête
        if map_[idx_ligne_prochain][idx_col_prochain] == representation['mur']:
            map_[self._position_courante[0]][self._position_courante[1]] = representation['robot_courant']
            print('Mur\nProchaine ligne : {}\nProchaine colonne : {}'.format(idx_ligne_prochain,idx_col_prochain)) # DEBUG
            raise(IndexError)
        # ...est la sortie, on se positionne dessus, on arrête
        elif map_[idx_ligne_prochain][idx_col_prochain] == representation['sortie']:
            map_[idx_ligne_prochain][idx_col_prochain] = representation['robot_courant']
            print('sortie') # DEBUG
            raise(IndexError)

        # ...est une porte
        if map_[idx_ligne_prochain][idx_col_prochain] == representation['porte']:
            # ...on sauvegarde la porte
            self._porte_courante = (idx_ligne_prochain, idx_col_prochain)

        # On se déplace
        map_[idx_ligne_prochain][idx_col_prochain] = representation['robot_courant']

        self._evaluer_position_joueur(map_)
        _map = self._retablir_porte(map_)
        return idx_ligne_prochain, idx_col_prochain, map_

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

    def _evaluer_position_joueur(self, map_):
        """
            Met à jour la position du joueur en fonction de la map.

            Ne fonctionne que s'il y a un et un seul robot au sein de la map.
        """

        # Pour chacune des lignes...
        for row, i in enumerate(map_):
            # ...on cherche l'indice de la colonne...
            try:
                column = i.index(representation['robot_courant'])
            # ...si le robot n'y est pas, on continue la recherche
            except ValueError:
                continue

            # ...et  on la trouve, on la mémorise
            nouvelles_position = (row, column)
            self._position_courante = nouvelles_position