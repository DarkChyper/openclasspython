# -*- coding: utf8 -*-

import socket
from threading import Thread

class Data():
    """
    Classe contenant les données utiles à tous les Threads
    """
    client = True
    hote = "localhost"
    port = 12800
    connexion = None
    lstmsg = []
    turn = False
    
class Network(Data):
    """
    ensemble des méthodes régissant la connection TCP
    """
    def __init__(self):
        """
        Ouverture de la connexion
        """
        Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Data.connexion.connect((Data.hote, Data.port))
        print("Le client est maintenant connecté")
        
    def deco(self):
        """
        Fermeture de  la connexion principale
        """
        print("Fermeture de la connexion")
        Data.connexion.close()

class DataReceive(Thread, Data):
    """
    Thread chargé de la réception des messages en provenance du server.
    Les données sont stockées dans une liste commune avant affichage.
    """
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """
        Boucle active, réceptionne les messages et sert d'aiguilleur pour diriger le message vers la bonne variable de stockage.
        """ 
        while Data.client:
            msg_recu = ""
            msg_recu = Data.connexion.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            
            if msg_recu[:3] == "crt":
                msg_recu = msg_recu[3:]
            if msg_recu == "trn":
                turn = True
                
            Data.lstmsg.append(msg_recu)
            print(msg_recu)
            
            if msg_recu == "fin":
                Data.client = False

class DataSend(Thread, Data):
    """
    Thread chargé de l'envoi des messages entrés par l'utilisateur
    """
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        """Boucle active"""
        while Data.client:
            msg_a_envoyer = input("> ")
            # Peut planter si vous tapez des caractères spéciaux
            if msg_a_envoyer == "fin":
                Data.client = False
                
            msg_a_envoyer = msg_a_envoyer.encode()
            # On envoie le message
            Data.connexion.send(msg_a_envoyer)

