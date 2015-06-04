# -*- coding: utf8 -*-

from roboc_server_class import *
from threading import Thread
from os import listdir
from re import findall
from time import sleep

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
        numtour = 0
        while Data.nbr_joueurs_actu != Data.nbr_joueurs_max:
            sleep(0.1)
        while True:
            #défini l'indice du joueur dont on attend le message
            if numtour > 3:
                numtour = 0
                
            #envoi de la carte à tous les joueurs
            for socketclient in Data.clients_connectes:
                cartetemp = "crt" + DataCarte.plan
                socketclient.send(cartetemp.encode())
            
            #on signale au joueur actif que c'est son tour
            message = "trn"
            Data.clients_connectes[numtour].send(message.encode())
            
            tempo = True
            while tempo == True:
                if len(Data.mouv) == 1:
                    tempo = False

class Carte(DataCarte, Data):
    """Gestion de la carte"""
    def __init__(self):
        """
        affichage de la liste des cartes disponibles
        """
        #permet de récupérer tous les noms de fichier/dossier dans un dossier, retour est une liste
        lstcartes = listdir("cartes") 
        i = 1
        for crt in lstcartes:
            crtname = findall('^[a-zA-Z0-9 _-]+', crt) #on extrait le nom de la carte sans l'extension
            print("{} - {}".format(i, crtname[0]))
            DataCarte.carte[i] = crtname[0]
            i += 1
    
    def Definition(self):
        """
        Définition des paramètres de la partie coté serveur
        """
        temp = input("Choisissez la carte à charger : ")
        try:
            DataCarte.numcarte = int(temp)
        except:
            DataCarte.numcarte = 2
            
        temp = input("Choisissez le nombre de joueurs maximum : ")
        try:
            Data.nbr_joueurs_max = int(temp)
        except:
            Data.nbr_joueurs_max = 1
        
    def ChargeCarte(self):
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
