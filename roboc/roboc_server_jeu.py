# -*- coding: utf8 -*-

from roboc_server_class import *
from threading import Thread
from os import listdir
from re import findall

class DataCarte():
    """Stocke les données de la carte"""
    carte = {}
    numcarte = ""
    plan = ""
    Nbrligne = 0
    Longueurligne = 0

class Partie(Thread):
    """déroulement du jeu"""
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        """
        corps du jeu
        """
        #envoi de la carte à tous les joueurs
        for socketclient in Data.clients_connectes:
            cartetemp = "crt" + DataCarte.plan
            socketclient.send(cartetemp.encode())

class Carte(DataCarte, Data):
    """Gestion de la carte"""
    def __init__(self):
        """
        demande au premier joueur la carte à jouer
        """
        lstcartes = listdir("cartes") #permet de récupérer tous les noms de fichier/dossier dans un dossier, retour est une liste
        i = 1
        message = "chx"
        for crt in lstcartes:
            crtname = findall('^[a-zA-Z0-9 _-]+', crt) #on extrait le nom de la carte sans l'extension
            message += "{} - {}".format(i, crtname[0])
            message += "\n"
            DataCarte.carte[str(i)] = crtname[0]
            i += 1
        
        message = message.encode()
        Data.clients_connectes[0].send(message)
        
    def ChargeCarte():
        """
        Chargement de la carte dans la liste qui servira pour le reste du programme
        """
        path = "cartes/" + DataCarte.carte[DataCarte.numcarte] + ".txt"
        Lline = 0
        nbrline = 0
    
        with open(path, "r") as carte:
            for line in carte:
                DataCarte.plan = DataCarte.plan + line + "\n"
                if nbrline == 0:
                    Lline = len(line) - 1
                nbrline += 1
    
        DataCarte.Nbrligne = nbrline
        DataCarte.Longueurligne = Lline
