# -*- coding: utf8 -*-

import socket

class Data():
    """
    Classe contenant les données utiles à tous les Threads
    """
    serveur = True
    hote = "localhost"
    port = 12800
    connexion = None
    
class Network(Data):
    """
    ensemble des méthodes régissant la connection TCP
    """
    def __init__(self):
        """
        Ouverture de la connexion
        """
        connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        connexion_avec_serveur.connect((hote, port))
        print("Le client est maintenant connecté")
        
    def deco(self):
        """
        Fermeture de  la connexion principale
        """
        print("Fermeture de la connexion")
        connexion.close()
