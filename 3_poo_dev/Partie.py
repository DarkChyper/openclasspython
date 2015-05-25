#!/usr/bin/env python
# Coding: utf-8

# Externe
from pickle     import Pickler, Unpickler
from os         import listdir, path
# Interne
from Map        import *
from donnees    import *

class Partie:

    def __init__(self):
        self._map = self._demarrer_partie()
        print(self._map)

    def _demarrer_partie(self):
        """Si une partie sauvegardée a été trouvée, on retourne la map,
        sinon, on la demande au joueur"""

        map_ = self._obtenir_partie_sauvegarde(adresse_fichier_sauvegarde)

        # Demande à l'utilisateur s'il souhaite utiliser la sauvegarde trouvée
        entree = ""
        while map_ != None and entree not in ['o','n']:
            entree = input("Souhaitez-vous utiliser la dernière sauvegarde ? (o/n) ").lower()

        # Si aucune sauvegarde n'a été trouvée ou que le joueur ne souhaite pas la continuer...
        if map_ == None or entree == 'n':
            # ...On demande au joueur de choisir le labyrinthe
            nom_maps = self._obtenir_liste_maps(dossier_maps)
            indice = self._demander_map(nom_maps)
            map_str = self._obtenir_map(dossier_maps, indice, nom_maps)
            map_ = Map(map_str)

        return map_

    def _obtenir_partie_sauvegarde(self, adresse_fichier):
        """Récupère la dernière partie sauvegardée, s'il n'y en a pas,
        renvoie None"""

        pas_de_sauv_msg = "Aucune sauvegarde trouvée."

        try:
            with open(adresse_fichier, 'rb') as fichier_sauvegarde:
                #Lecture du fichier
                unpick = Unpickler(fichier_sauvegarde)
                map_ = unpick.load()

                return map_
        except:
            print(pas_de_sauv_msg)
            return None

    def _obtenir_liste_maps(self, dossier):
        """Retourne une liste de nom de maps"""

        nom_maps = []

        # On charge le nom des cartes existantes
        for i, nom_fichier in enumerate(listdir(dossier)):
            if nom_fichier.endswith(".txt"):
                chemin = path.join("cartes", nom_fichier)
                nom_maps.append( nom_fichier[:-4].lower() )

        return nom_maps

    def _demander_map(self, nom_maps):
        """Demande au joueur quel map il souhaite choisir"""

        # On affiche la liste des labyrinthes disponibles
        map_msg = "Indiquer le chiffre du labyrinthe que vous souhaitez choisir parmi la liste suivante : "
        print(map_msg)

        for i, nom in enumerate(nom_maps):
            print("{}. {}".format(i + 1, nom))

        # Tant que l'input est incorrecte...
        indice = None
        while indice not in range(1, len(nom_maps) + 1):
            # ...On demande l'indice du labyrinthe
            try:
                indice = int(input("Labyrinthe : "))
            except:
                pass

        return indice - 1

    def _obtenir_map(self, dossier, indice, maps):
        """Retourne un objet Map en fonction de l'indice"""
        nom_fichier = listdir(dossier)[indice]
        chemin = path.join(dossier, nom_fichier)
        with open(chemin, "r") as fichier:
            contenu = fichier.read()

        return contenu

    def _sauvegarder(self, adresse_fichier):
        """Sauvegarde la map"""

        try:
            with open(adresse_fichier, 'wb') as fichier_sauvegarde:
                pick = Pickler(fichier_sauvegarde)
                pick.dump(self._map)
        except:
            print("Erreur lors de l'enregistrement du fichier")

    def _tuer_sauvegarde(self, adresse_fichier):
        """Sauvegarde la map"""

        try:
            with open(adresse_fichier, 'wb') as fichier_sauvegarde:
                pick = Pickler(fichier_sauvegarde)
                pick.dump(None)
        except:
            print("Erreur lors de l'enregistrement du fichier")

    def jouer(self):
        """Demande au joueur quel deplacement il souhaite effectuer
        et renvoie s'il a gagné ou non"""

        touche_msg = "Quel déplacement souhaitez-vous effectuer ? "

        entree = None
        while entree == None:
            entree = self._entree_correcte( input(touche_msg) )

        gagne = self._map.deplacement(*entree)
        self._sauvegarder(adresse_fichier_sauvegarde)
        print(self._map)

        return gagne

    def terminer(self):
        """Message de sortie pour le joueur, selon qu'il ait gagné ou non"""
        self._tuer_sauvegarde(adresse_fichier_sauvegarde)

        sorti_msg = "Bravo, vous avez réussi à sortir !"
        print(sorti_msg)

    def _afficher_aide(self):
        pass

    def _entree_correcte(self, entree):
        """Renvoie le type de déplacement et la longueur
        ou None si l'entrée est incorrecte.
        Si l'utilisateur demande de l'aide, on renvoie entree"""

        # Si l'utilisateur demande de l'aide, on ne touche à rien
        if entree == touches['aide']:
            self._afficher_aide()
            return None

        # Si le premier caractère est correct
        if len(entree) != 0 and entree[0] in touches.values():
            type_deplacement = entree[0]

            # Si le reste est un nombre
            try:
                lg = int(entree[1:])
            except:
                # Si aucune longueur n'est indiquée
                if entree[1:].strip() == '':
                    lg = 1
                    return type_deplacement, lg
            else:
                return type_deplacement, lg

        return None