# -*- coding: utf8 -*-

import socket

class Data():
    """
    Classe contenant les données utiles à tous les Threads
    """
    client = True
    hote = "localhost"
    port = 12800
    connexion = None
    lstmsg = []
    
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

class DataReceive(Thread, Data):
    """
    Thread chargé de la réception des messages en provenance du server.
    Les données sont stockées dans une liste commune avant affichage.
    """
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Boucle active""" 
        while client:
            msg_recu = connexion.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            lstmsg.append(msg_recu)
            if msg_recu == "fin":
                client = False
