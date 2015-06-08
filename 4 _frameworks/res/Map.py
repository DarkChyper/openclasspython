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
        self.representation_map = self._convert(map_str)
        """Représentation interne de la map : liste 2D"""
        self._liste_joueurs = []
        """Liste des joueurs"""
        self._liste_portes = obtenir_positions_portes(self.representation_map)
        """Liste des portes de la map"""

    def __repr__(self):
        """
            Concatène tous les éléments de la liste 2D
            pour afficher le labyrinthe
        """

        str_ = ""
        for line in self.representation_map:
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

    def deplacement(self, type_, longueur, joueur):
        """
            En fonction du type de déplacement, on réévalue la map.
            Si un déplacement renvoie un IndexError, on l'ignore.
        """

        print( self.__str__() ) # DEBUG
        try:
            self.representation_map = self._liste_joueurs[joueur].se_deplacer(self.representation_map, type_)
        except IndexError:
            raise

        self._retablir_portes()

    def maj_carte_joueurs(self, joueur_courant):
        """
            Envoie la carte à tous les joueurs
        """

        for joueur in self._liste_joueurs:
            joueur.envoi_map_client(self, joueur_courant)

    def _retablir_portes(self):
        """
            Pour toutes les portes de la map,
            les rétablis si elles ne sont pas occupées
        """

        for lig_porte, col_porte in self._liste_portes:
            print("Porte : ({}, {})".format(lig_porte, col_porte)) # DEBUG
            if self.representation_map[lig_porte][col_porte] == representation['vide']:
                self.representation_map[lig_porte][col_porte] = representation['porte']

    def etat_jeu(self):
        """
            Retourne False si le jeu n'est pas gagné et True s'il est gagné.

            Le robot doit remplacer la sortie lors de son dernier mouvement
            pour que cette méthode fonctionne correctement.
        """

        # Pour chacune des lignes...
        for row, i in enumerate(self.representation_map):
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

    def obtenir_joueur(self, indice):
        return self._liste_joueurs[indice]

    def ajouter_joueur(self, socket):
        """
            Permet d'ajouter un joueur à la map et renvoie la map au client
        """

        # Données
        ligne = len(self.representation_map)
        colonne = len(self.representation_map[0])
        id_ = len(self._liste_joueurs)

        # Tant que la position générée n'est pas du vide...
        lig_joueur = randrange(0,ligne)
        col_joueur = randrange(0, colonne)
        while not self.representation_map[lig_joueur][col_joueur] == representation['vide']:
            # ...on regénère
            lig_joueur = randrange(0,ligne)
            col_joueur = randrange(0, colonne)

        # On l'ajoute à la map
        self.representation_map[lig_joueur][col_joueur] = representation['autre_robot']

        # On crée un nouveau joueur qu'on préviens
        nouveau_joueur = Joueur(socket, lig_joueur, col_joueur, id_)
        nouveau_joueur.envoi_map_client(self, nouveau_joueur.id_)

        # On ajoute le nouveau joueur à la liste
        self._liste_joueurs.append(nouveau_joueur)

    def prevenir_joueurs(self, balise, msg):
        for joueur in self._liste_joueurs:
            joueur.envoi_message_client(balise, msg)

    def fermer_connexions(self):
        """
            On ferme la connexion de tous les joueurs
        """
        for joueur in self._liste_joueurs:
            joueur.fermer_connexion()


########## PROPRIÉTÉS ##########


    def _get_nb_joueurs(self):
        return len(self._liste_joueurs)

    def _get_sockets(self):
        sockets = []
        for joueur in self._liste_joueurs:
            sockets.append(joueur.socket)

        return sockets

    nb_joueurs = property(_get_nb_joueurs, None)

    sockets = property(_get_sockets, None)


######### FONCTIONS MAP ##########


def obtenir_positions_portes(map_):
    """
        Mémorise la position des portes d'une map
    """

    position_portes = []
    # Pour chacune des lignes...
    for i, lig in enumerate(map_):
        # ...on cherche l'indice de la colonne...
        for j, cell in enumerate(lig):
            if cell == representation['porte']:
                position_portes.append( (i, j) )

    return position_portes