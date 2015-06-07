# -*- coding: utf8 -*-

import socket
from threading import Thread
from re import findall

class Data():
    """
    Classe contenant les données utiles à tous les Threads
    """
    client = True
    hote = "localhost"
    port = 12800
    connexion = None
    lstmsg = [None]
    lstinfos = [None]
    pos = None
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
                Data.lstmsg[0] = msg_recu
            elif msg_recu == "trn":
                Data.turn = True
                Data.lstinfos[0] = "A vous de jouer"
            elif msg_recu[:3] == "pos":
                print(msg_recu)
                temp0 = findall('^\(([0-9])+,', msg_recu[3:])
                temp1 = findall(' ([0-9]+)\)$', msg_recu[3:])
                Data.pos = (int(temp0[0]), int(temp1[0]))
            elif msg_recu[:3] == "fin":
                if len(msg_recu) == 3:
                    Data.lstinfos[0] = "Vous avez perdu!"
                elif len(msg_recu) > 3:
                    Data.lstinfos[0] = "Vous avez gagné!"
                Data.client = False
            elif msg_recu[:3] == "err":
                Data.lstinfos[0] = msg_recu[3:]
                
            print(msg_recu)

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

