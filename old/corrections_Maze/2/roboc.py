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

    # On sort proprement
    partie.terminer()
    exit(0)

if __name__ == "__main__":
    main()