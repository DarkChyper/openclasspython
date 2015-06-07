#!/usr/bin/env python
# Coding: utf-8

# Externe
from random     import randrange
# Interne
from res.Joueur     import *
from res.settings    import *

class Map:
    """
        Représentation de la carte.

        Utilisation d'une liste à 2 dimensions pour représenter la map.
    """

    def __init__(self, map_str):
        self._representation_map = self._convert(map_str)
        """Représentation interne de la map : liste 2D"""

    def __repr__(self):
        """
            Concatène tous les éléments de la liste 2D
            pour afficher le labyrinthe
        """

        str_ = ""
        for line in self._representation_map:
            for colonne in line:
                str_ += colonne
            str_ += "\n"

        return str_.rstrip()


    def _convert(self, map_str):
        """
            Convertit la string provenant du fichier texte
            en une liste à 2 dimensions.

            La map est considérée intègre.
        """

        map_ = list()

        # On sépare les lignes
        map_str = map_str.rstrip().split("\n")

        # Pour chacune des lignes...
        for i, ligne in enumerate(map_str):
            # ...on crée une liste de caractères
            ligne = list(ligne)
            # ...et on crée une un liste dans la 1ère dimension
            map_.append(list())

            # Pour chacun des caractères...
            for car in ligne:
                # ...on l'ajoute dans la 2nde dimension
                map_[i].append(car)

        return map_

    def deplacement(self, type_, longueur, ligne_j_courant, col_j_courant):
        """
            En fonction du type de déplacement, on réévalue la map.
            Si un déplacement renvoie un IndexError, on l'ignore.
        """

        # On signale le joueur actuel en 'X'
        self._representation_map[ligne_j_courant][col_j_courant] = representation['robot_courant']
        joueur = Joueur(self._representation_map)

        print("ligne courante : {}, colonne courante : {}".format(ligne_j_courant, col_j_courant)) # DEBUG
        print(self.__str__()) # DEBUG
        for i in range(0, longueur):
            try:
                nv_ligne, nv_col, self._representation_map = joueur.se_deplacer(self._representation_map, type_)
            except IndexError:
                nv_ligne, nv_col = ligne_j_courant, col_j_courant
                break

        return nv_ligne, nv_col

    def set_joueur(self):
        # Données
        ligne = len(self._representation_map)
        colonne = len(self._representation_map[0])

        pos_ligne = randrange(0,ligne)
        pos_col = randrange(0, colonne)

        while not self._representation_map[pos_ligne][pos_col] == representation['vide']:
            pos_ligne = randrange(0,ligne)
            pos_col = randrange(0, colonne)

        self._representation_map[pos_ligne][pos_col] = representation['autre_robot']
        return pos_ligne, pos_col

        self._map

    def get_map_joueur_courant(self, ligne, colonne):
        """
            Renvoie une map avec un 'X' pour le joueur courant
        """

        self._representation_map[ligne][colonne] = representation['robot_courant']
        map_str = self.__str__()
        self._representation_map[ligne][colonne] = representation['autre_robot']

        return map_str