#!/usr/bin/env python
# coding: utf-8

# Interne
from res.Client    import *

def main():
    """
        Main du client :
        tourne sans arrêt jusqu'à la fermeture du serveur et/ou du client par le joueur
    """
    try:
        client = Client()
    except:
        raise

    # On quitte
    try:
        client.fermer()
    except:
        raise
    finally:
        exit(0)

if __name__ == "__main__":
    main()