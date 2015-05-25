#!/usr/bin/env python
# Coding: utf-8

# Interne
from donnees import *

class Joueur:
    """position_courante (ligne, colonne)"""

    def __init__(self, map_):
        # Déterminer la position du joueur
        self._position_courante = (0,0)
        self._evaluer_position_joueur(map_)

    def aller_ouest(self, map_, lg):
        """Effectue un déplacement vers l'Ouest en fonction de la position
        courante du joueur et de la map"""

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
            # ...sinon, on continue

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante][idx_col_courante - lg] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_


    def aller_nord(self, map_, lg):
        """Effectue un déplacement vers le Nord en fonction de la position
        courante du joueur et de la map"""

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
            # ...sinon, on continue...

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante - lg][idx_col_courante] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_

    def aller_est(self, map_, lg):
        """Effectue un déplacement vers l'Est en fonction de la position
        courante du joueur et de la map"""

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
            # ...sinon, on continue

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante][idx_col_courante + lg] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_

    def aller_sud(self, map_, lg):
        """Effectue un déplacement vers le Sud en fonction de la position
        courante du joueur et de la map"""

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
            # ...sinon, on continue...

        #...pour finalement, faire le déplacement complet
        map_[idx_ligne_courante + lg][idx_col_courante] = representation['robot']
        self._evaluer_position_joueur(map_)

        return map_

    def _evaluer_position_joueur(self, map_):
        """Met à jour la position du joueur en fonction de la map"""

        for row, i in enumerate(map_):
            try:
                column = i.index(representation['robot'])
            except ValueError:
                continue

            nouvelles_position = (row, column)
            self._position_courante = nouvelles_position