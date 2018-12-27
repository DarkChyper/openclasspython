#!/usr/bin/env python
# Coding: utf-8

# Interne
from donnees import *

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
        """_position_courante (ligne, colonne)"""

        self._evaluer_position_joueur(map_)

    def aller_ouest(self, map_, lg):
        """
            Effectue un déplacement vers l'Ouest en fonction de la position
            courante du joueur et de la map.

            Vers l'Est, on joue sur les ordonnées (2nde dimension)
            en reculant (-).
        """

        # On efface le robot sur la map
        map_[self._position_courante[0]][self._position_courante[1]] = representation['vide']

        # Variables plus intelligibles
        idx_col_courante = self._position_courante[1]
        idx_ligne_courante = self._position_courante[0]

        # Si le premier déplacement est une porte...
        if map_[idx_ligne_courante][idx_col_courante - 1] == representation['porte']:
            # ...on la franchit
            map_[idx_ligne_courante][idx_col_courante - 2] = representation['robot']
            self._evaluer_position_joueur(map_)

            return map_

        # Pour toute la longueur du déplacement...
        for i in range(1, lg + 1):
            # ...si on rencontre un porte ou un mur, on s'arrête
            if map_[idx_ligne_courante][idx_col_courante - i] in [representation['porte'],representation['mur']]:
                map_[idx_ligne_courante][idx_col_courante - i + 1] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...si on rencontre la sortie, on se positionne dessus
            elif map_[idx_ligne_courante][idx_col_courante - i] == representation['sortie']:
                map_[idx_ligne_courante][idx_col_courante - i] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...sinon, on continue le déplacement...

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante][idx_col_courante - lg] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_


    def aller_nord(self, map_, lg):
        """
            Effectue un déplacement vers le Nord en fonction de la position
            courante du joueur et de la map.

            Vers le Nord, on joue sur les ordonnées (1ère dimension)
            en reculant (-).
        """

        # On efface le robot sur la map
        map_[self._position_courante[0]][self._position_courante[1]] = representation['vide']

        # Variables plus intelligibles
        idx_col_courante = self._position_courante[1]
        idx_ligne_courante = self._position_courante[0]

        # Si le premier déplacement est une porte...
        if map_[idx_ligne_courante - 1][idx_col_courante] == representation['porte']:
            # ...on la franchit
            map_[idx_ligne_courante - 2][idx_col_courante] = representation['robot']
            self._evaluer_position_joueur(map_)

            return map_

        # Pour toute la longueur du déplacement...
        for i in range(1, lg + 1):
            # ...si on rencontre un porte ou un mur, on s'arrête
            if map_[idx_ligne_courante - i][idx_col_courante] in [representation['porte'],representation['mur']]:
                map_[idx_ligne_courante - i + 1][idx_col_courante] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...si on rencontre la sortie, on se positionne dessus
            elif map_[idx_ligne_courante - i][idx_col_courante] == representation['sortie']:
                map_[idx_ligne_courante - i][idx_col_courante] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...sinon, on continue le déplacement...

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante - lg][idx_col_courante] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_

    def aller_est(self, map_, lg):
        """
            Effectue un déplacement vers l'Est en fonction de la position
            courante du joueur et de la map.

            Vers l'Est, on joue sur les ordonnées (2nde dimension)
            en avançant (+).
        """

        # On efface le robot sur la map
        map_[self._position_courante[0]][self._position_courante[1]] = representation['vide']

        # Variables plus intelligibles
        idx_col_courante = self._position_courante[1]
        idx_ligne_courante = self._position_courante[0]

        # Si le premier déplacement est une porte...
        if map_[idx_ligne_courante][idx_col_courante + 1] == representation['porte']:
            # ...on la franchit
            map_[idx_ligne_courante][idx_col_courante + 2] = representation['robot']
            self._evaluer_position_joueur(map_)

            return map_

        # Sinon, pour toute la longueur du déplacement...
        for i in range(1, lg + 1):
            # ...si on rencontre un porte ou un mur, on s'arrête
            if map_[idx_ligne_courante][idx_col_courante + i] in [representation['porte'],representation['mur']]:
                map_[idx_ligne_courante][idx_col_courante + i - 1] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...si on rencontre la sortie, on se positionne dessus
            elif map_[idx_ligne_courante][idx_col_courante + i] == representation['sortie']:
                map_[idx_ligne_courante][idx_col_courante + i] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...sinon, on continue le déplacement...

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante][idx_col_courante + lg] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_

    def aller_sud(self, map_, lg):
        """
            Effectue un déplacement vers le Sud en fonction de la position
            courante du joueur et de la map.

            Vers le Sud, on joue sur les ordonnées (1ère dimension)
            en avançant (+).
        """

        # On efface le robot sur la map
        map_[self._position_courante[0]][self._position_courante[1]] = representation['vide']

        # Variables plus intelligibles
        idx_col_courante = self._position_courante[1]
        idx_ligne_courante = self._position_courante[0]

        # Si le premier déplacement est une porte...
        if map_[idx_ligne_courante + 1][idx_col_courante] == representation['porte']:
            # ...on la franchit
            map_[idx_ligne_courante + 2][idx_col_courante] = representation['robot']
            self._evaluer_position_joueur(map_)

            return map_

        # Pour toute la longueur du déplacement...
        for i in range(1, lg + 1):
            # ...si on rencontre un porte ou un mur, on s'arrête
            if map_[idx_ligne_courante + i][idx_col_courante] in [representation['porte'],representation['mur']]:
                map_[idx_ligne_courante + i - 1][idx_col_courante] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...si on rencontre la sortie, on se positionne dessus
            elif map_[idx_ligne_courante + i][idx_col_courante] == representation['sortie']:
                map_[idx_ligne_courante + i][idx_col_courante] = representation['robot']
                self._evaluer_position_joueur(map_)

                return map_
            # ...sinon, on continue le déplacement...

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante + lg][idx_col_courante] = representation['robot']
        self._evaluer_position_joueur(map_)

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
                column = i.index(representation['robot'])
            # ...si le robot n'y est pas, on continue la recherche
            except ValueError:
                continue

            # ...et  on la trouve, on la mémorise
            nouvelles_position = (row, column)
            self._position_courante = nouvelles_position