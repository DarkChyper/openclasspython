#!/usr/bin/env python
# coding: utf-8

# Interne
from Partie import *
from Map    import *
from Joueur import *

def main():
    """
        Coeur du jeu.

        Tant que le joueur n'est pas sorti, on continue de jouer.
    """

    partie = Partie()
    sorti_du_labyrinthe = False

    while not sorti_du_labyrinthe:
        sorti_du_labyrinthe = partie.jouer()

        if sorti_du_labyrinthe:
            # On termine la partie actuelle
            partie.terminer()

            sorti_du_labyrinthe = recommencer()

            # Si le joueur continue...
            if not sorti_du_labyrinthe:
                # ...on recrée une nouvelle partie
                partie = Partie()

    exit(0)

def recommencer():
    """
        Retourne False si le joueur souhaite recommencer
    """

    recommencer_msg = "Souhaitez-vous recommencer ?"
    entree = None

    while entree == None:
        entree = input(recommencer_msg)

        if entree.lower() == 'o':
            return False
        elif entree.lower() == 'n':
            return True
        else:
            entree = None

    return False

if __name__ == "__main__":
    main()