# -*- coding: utf8 -*-

from threading import Thread
import time
import select

class Data():
    """
    Classe contenant les données utiles à tous les Threads
    """
    serveur = True
    clients_connectes = []
    infos_clients_connectes = []
    clients_a_lire = []

class NewClient(Thread, Data):
    """Thread chargé de surveiller l'arrivée de nouveaux clients."""
    def __init__(self, connexion):
        Thread.__init__(self)
        self.connexion = connexion
        
    def run(self):
        """Boucle active""" 
        while serveur:
            #on vérifie si de nouveaux clients demandes à se connecter
            connexions_demandees, wlist, xlist = select.select([self.connexion],[], [], 0.05)
            
            for connexion in connexions_demandees:
                connexion_avec_client, infos_connexion = connexion.accept()
                # On ajoute le socket connecté à la liste des clients
                clients_connectes.append(connexion_avec_client)
                #les infos sont sauvegardées au cas où...
                infos_clients_connectés.append(infos_connexion)

class DataExchange(Thread, Data):
    """Thread chargé de surveiller l'envoi de données par les clients."""
    def __init__(self):
        Thread.__init__(self)

    def run(self):
        """Boucle active""" 
        while serveur:
            try:
                clients_a_lire, wlist, xlist = select.select(clients_connectes, [], [], 0.05)
            except select.error:
                pass
            else:
                for client in clients_a_lire:
                    msg_recu = client.recv(1024)
                    # Peut planter si le message contient des caractères spéciaux
                    msg_recu = msg_recu.decode()
                    print("Reçu {}".format(msg_recu))
                    if msg_recu == "fin":
                        serveur = False
