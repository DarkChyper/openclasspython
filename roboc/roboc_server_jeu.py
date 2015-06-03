# -*- coding: utf8 -*-

from roboc_server_class import *
from threading import Thread
from os import listdir
from re import findall

class DataCarte():
    """Stocke les données de la carte"""
    carte = None
    plan = []

class Partie(Thread, DataCarte, Data):
    """déroulement du jeu"""
    def __init__(self):
        Thread.__init__(self)
        
    def run(self):
        carte = Carte()

class Carte(DataCarte):
    """Gestion de la carte"""
    def __init__(self):
        """demande au premier joueur la carte à jouer"""
        lstcartes = listdir("cartes") #permet de récupérer tous les noms de fichier/dossier dans un dossier, retour est une liste
        i = 1
        message = "choix"
        for crt in lstcartes:
            crtname = findall('^[a-zA-Z0-9 _-]+', crt) #on extrait le nom de la carte sans l'extension
            message += "{} - {}".format(i, crtname[0])
            message += "\n"
            i += 1
        
        message = message.encode()
        Data.clients_connectes[0].send(message)
        
    def ChargeCarte(DataCarte):
        path = "cartes/" + DataCarte.carte
        Lline = 0
        nbrline = 0
        hX = 0
        lX = 0
    
        with open(path, "r") as carte:
            for line in carte:
                DataCarte.plan.append(line)
                if nbrline == 0:
                    Lline = len(line) - 1
                nbrline += 1
    
        DataCarte.Nbrligne = nbrline
        DataCarte.Longueurligne = Lline
