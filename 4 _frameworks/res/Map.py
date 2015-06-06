#!/usr/bin/env python
# Coding: utf-8

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

        self._joueur = Joueur(self._representation_map)
        """Joueur qui va manipuler la Map en se déplaçant"""

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

    def deplacement(self, type_, longueur):
        """
            En fonction du type de déplacement, on réévalue la map.
            Si un déplacement renvoie un IndexError, on l'ignore.
        """

        for i in range(0, longueur):
            try:
                self._representation_map = self._joueur.se_deplacer(self._representation_map, type_)
            except IndexError:
                break
            finally:
                print(self)
        return self._etat_jeu(self._representation_map)

    def _etat_jeu(self, map_):
        """
            Retourne False si le jeu n'est pas gagné et True s'il est gagné.

            Le robot doit remplacer la sortie lors de son dernier mouvement
            pour que cette méthode fonctionne correctement.
        """

        # Pour chacune des lignes...
        for row, i in enumerate(map_):
            # ...on cherche l'indice de la colonne...
            try:

                column = i.index(representation['sortie'])

                # ...si on trouve la sortie, le joueur n'a pas encore gagné
                return False
            # ...si la sortie n'est pas encore trouvé, on continue la recherche...
            except ValueError:
                continue

        # ...si on arrive ici, c'est que la sortie n'a pas été trouvée et que le joueur a gagné
        return True

    def len_lig(self):
        return len(self._representation_map)

    def len_col(self):
        return len(self._representation_map[0])

    def est_vide(self, ligne, colonne):
        return self._representation_map[ligne][colonne] == representation['vide']