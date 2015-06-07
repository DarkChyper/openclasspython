#!/usr/bin/env python
# coding: utf-8

# Interne
from res.Serveur    import *

def main():
    """
        Coeur du jeu.

        Tant que le joueur n'est pas sorti, on continue de jouer.
    """

    serveur = Serveur()
    sorti_du_labyrinthe = False

    while not sorti_du_labyrinthe:
        sorti_du_labyrinthe = serveur.jouer()

    serveur.terminer()
    exit(0)


if __name__ == "__main__":
    main()