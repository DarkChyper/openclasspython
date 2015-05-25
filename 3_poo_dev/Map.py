#!/usr/bin/env python
# Coding: utf-8

# Interne
from Joueur     import *
from donnees    import *

class Map:

    def __init__(self, map_str):
        # Map
        self._representation_map = self._convert(map_str)

        # Joueur
        self._joueur = Joueur(self._representation_map)

    def __repr__(self):
        str_ = ""
        for line in self._representation_map:
            for colonne in line:
                str_ += colonne
            str_ += "\n"

        return str_


    def _convert(self, map_str):
        """Convertit la string provenant du fichier texte
        en une liste à 2 dimensions"""

        lst = list()

        # On sépare les lignes
        map_str = map_str.rstrip().split("\n")

        # On crée un tableau 2D pour stocker la map
        # Pour chacune des lignes...
        for i, ligne in enumerate(map_str):
            # ...on crée une liste de caractères
            ligne = list(ligne)
            # ...et on crée une un liste dans la 1ère dimension
            lst.append(list())

            # Pour chacun des caractères...
            for car in ligne:
                # ...on l'ajoute dans la 2nde dimension
                lst[i].append(car)

        return lst

    def deplacement(self, type, longueur):
        """En fonction du type de déplacement, on réévalue la map"""
        try:
            if type == 'o':
                self._representation_map = self._joueur.aller_ouest(self._representation_map, longueur)
            if type == 'n':
                self._representation_map = self._joueur.aller_nord(self._representation_map, longueur)
            if type == 'e':
                self._representation_map = self._joueur.aller_est(self._representation_map, longueur)
            if type == 's':
                self._representation_map = self._joueur.aller_sud(self._representation_map, longueur)
        except IndexError:
            pass

        return self._etat_jeu(self._representation_map)

    def _etat_jeu(self, map_):
        """Retourne False si le jeu n'est pas gagné et True s'il est gagné"""

        for row, i in enumerate(map_):
            try:
                column = i.index(representation['sortie'])
                return False
            except ValueError:
                continue

        return True