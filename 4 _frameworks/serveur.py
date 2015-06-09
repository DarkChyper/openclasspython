#!/usr/bin/env python
# coding: utf-8

# Interne
from res.Serveur    import *

def main():
    """
        Main du serveur :

        Tant qu'aucun des joueurs n'est sorti du labyrinthe,
        on continue de jouer
    """

    serveur = Serveur()
    sorti_du_labyrinthe = False

    while not sorti_du_labyrinthe:
        sorti_du_labyrinthe = serveur.jouer()

    serveur.prevenir_joueur_partie_gagne()
    serveur.terminer()
    exit(0)


if __name__ == "__main__":
    main()