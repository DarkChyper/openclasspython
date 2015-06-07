# -*- coding: utf8 -*-

from threading import Thread
import socket
import select

class Data():
    """
    Classe contenant les données utiles à tous les Threads
    """
    serveur = True
    init = True
    nbr_joueurs_max = 0
    nbr_joueurs_actu = 0
    clients_connectes = []
    infos_clients_connectes = []
    clients_a_lire = []
    hote = ''
    port = 12800
    connexion = None
    mouv = []

class NewClient(Thread, Data):
    """Thread chargé de surveiller l'arrivée de nouveaux clients."""
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        """Boucle active""" 
        while Data.init:
            #on vérifie si de nouveaux clients demandes à se connecter
            connexions_demandees, wlist, xlist = select.select([Data.connexion],[], [], 0.05)
            
            for connexion in connexions_demandees:
                if Data.nbr_joueurs_actu < Data.nbr_joueurs_max:
                    connexion_avec_client, infos_connexion = connexion.accept()
                    # On ajoute le socket connecté à la liste des clients
                    Data.clients_connectes.append(connexion_avec_client)
                    #les infos sont sauvegardées au cas où...
                    Data.infos_clients_connectes.append(infos_connexion)
                    print("Nouveau client")
                    Data.nbr_joueurs_actu += 1
                else:
                    Data.init = False

class DataExchange(Thread, Data):
    """Thread chargé de surveiller l'envoi de données par les clients."""
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Boucle active""" 
        while Data.serveur:
            msg_recu = ""
            clients_a_lire = []
            try:
                clients_a_lire, wlist, xlist = select.select(Data.clients_connectes, [], [], 0.05)
            except select.error:
                pass
            else:
                if len(clients_a_lire) > 0:
                    for client in clients_a_lire:
                        msg_recu = client.recv(1024)
                        # Peut planter si le message contient des caractères spéciaux
                        msg_recu = msg_recu.decode()
                        
                        if msg_recu[:3] == "mvt":
                            msg_recu = msg_recu[3:]
                            Data.mouv.append(client)
                            Data.mouv.append(msg_recu)

class Network(Data):
    """
    ensemble des méthodes régissant la connection TCP
    """
    def __init__(self):
        """
        Ouverture de la connection
        """
        Data.connexion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        Data.connexion.bind((Data.hote, Data.port))
        Data.connexion.listen(5)
        print("Le serveur écoute à présent sur le port {}".format(Data.port))
        
    def decotot(self):
        """
        Fermeture de tous les sockets clients et fermeture de la connection principale
        """
        print("Fermeture des connexions")
        for client in Data.clients_connectes:
            client.close()

        Data.connexion.close()
