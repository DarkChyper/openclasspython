# -*- coding: utf8 -*-

from roboc_server_class import *
from threading import Thread
from os import listdir
from re import findall
from time import sleep
from random import randrange

class DataCarte():
    """Stocke les données de la carte"""
    carte = {}
    numcarte = ""
    plan = ""
    Nbrligne = 0
    Longueurligne = 0
    Posjoueurs = []
    victoire = False

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
        while Data.serveur:
            #défini l'indice du joueur dont on attend le message
            if numtour > Data.nbr_joueurs_max - 1:
                numtour = 0

            #envoi de sa position à chaque joueur
            for socketclient in Data.clients_connectes:
                indextemp = Data.clients_connectes.index(socketclient)
                postemp = "pos" + str(DataCarte.Posjoueurs[indextemp])
                socketclient.send(postemp.encode())
            
            #temporisation pour laisser le message précédent être réceptionné
            sleep(0.5)

            #envoi de la carte à tous les joueurs
            for socketclient in Data.clients_connectes:
                cartetemp = "crt" + DataCarte.plan
                socketclient.send(cartetemp.encode())
            
            #temporisation pour laisser le message précédent être réceptionné
            sleep(0.5)
            
            #on signale au joueur actif que c'est son tour
            message = "trn"
            Data.clients_connectes[numtour].send(message.encode())
            
            tempo = True
            while tempo == True:
                if len(Data.mouv) > 0:
                    tempo = False
            
            print("mouvement reçu!")
            
            #2 types de mouvement arrivent ici murer/ouvrir une porte
            if Data.mouv[1][0] == "P" or Data.mouv[1][0] == "M":
                pass
            #ou se déplacer
            else:
                #dans l'ordre, calcule de la nouvelle position, vérification de sa validité
                npos = Carte.nouvpos(Data.mouv)
                verif = Carte.verifpos(npos)
                #si la nouvelle position arrive sur la sortie
                if DataCarte.victoire:
                    for socketclient in Data.clients_connectes:
                        cartetemp = "fin"
                        if Data.mouv[0] == socketclient:
                            cartetemp += "vainqueur"
                        socketclient.send(cartetemp.encode())
                    Data.serveur = False
                #si la nouvelle position est sur un case valide
                elif verif:
                    #dans l'ordre on enlève l'ancien x de la carte
                    Carte.clearpos(Data.mouv[0])
                    #on met à jour la liste des positions
                    Carte.updatepos(Data.mouv[0], npos)
                    #on vérifie si un déplacement multiple a été demandé
                    
                #le reste
                else:
                    message = "err"
                    Data.clients_connectes[numtour].send(message.encode())

            Data.mouv = []
            numtour += 1

class Carte(DataCarte, Data):
    """Gestion de la carte"""
    def __init__(self):
        """
        affichage de la liste des cartes disponibles
        """
        #permet de récupérer tous les noms de fichier/dossier dans un dossier, retour est une liste
        lstcartes = listdir("carte") 
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
        path = "carte/" + DataCarte.carte[DataCarte.numcarte] + ".txt"
        Lline = 0
        nbrline = 0
    
        with open(path, "r") as carte:
            for line in carte:
                DataCarte.plan = DataCarte.plan + line
                if nbrline == 0:
                    Lline = len(line) - 1
                nbrline += 1
    
        DataCarte.Nbrligne = nbrline
        DataCarte.Longueurligne = Lline
        
    def PosInitJoueurs(self):
        """
        Définition aléatoire de la position initiale des joueurs
        """
        listejoueur = list(range(Data.nbr_joueurs_max))
        posvalide = False
        
        for joueur in listejoueur:
            while posvalide != True:
                posinit = (randrange(0, DataCarte.Longueurligne), randrange(0, DataCarte.Nbrligne))
                posvalide = Carte.verifposinit(posinit)
                if posvalide == True:
                    DataCarte.Posjoueurs.append(posinit)
            
            posvalide = False

    def verifposinit(pos):
        """
        Vérifie que la position choisie est bien valide au vue de la carte
        i.e. pas sur un mur, la sortie ou sur un autre joueur
        """
        line = 1
        carac = 1
        templine = ""
        status = False
        for char in DataCarte.plan:
            carac += 1
            if char == "\n":
                line +=1
                carac = 0
                templine += char
                continue
            
            if line == pos[1] and carac == pos[0]:
                if char == "O" or char == "U" or char == "x":
                    status = False
                else:
                    templine += "x"
                    status = True
            else:
                templine += char
        
        if status == True:
            DataCarte.plan = templine
        return status
        
    def nouvpos(mvt):
        """
        calcule la nouvelle position par rapport au mouvement demandé
        """
        tempindex = Data.clients_connectes.index(mvt[0])
        tempinitpos = DataCarte.Posjoueurs[tempindex]
        temppos = [tempinitpos[0], tempinitpos[1]]
        
        if mvt[1][0] == "N":
            temppos[1] -= 1
        elif mvt[1][0] == "S":
            temppos[1] += 1
        elif mvt[1][0] == "O":
            temppos[0] -= 1
        elif mvt[1][0] == "E":
            temppos[0] += 1
        
        npos = (temppos[0], temppos[1])
        return npos

    def clearpos(client):
        """
        supprime l'ancien x du joueur
        """
        tempindex = Data.clients_connectes.index(client)
        temppos = DataCarte.Posjoueurs[tempindex]
        line = 1
        carac = 1
        templine = ""
        for char in DataCarte.plan:
            carac += 1
            if char == "\n":
                line +=1
                carac = 0
                templine += char
                continue
                
            if line == temppos[1] and carac == temppos[0]:
                templine += " "
            else:
                templine += char
        
        DataCarte.plan = templine
    
    def updatepos(client, npos):
        """
        mise à jour de la position actuelle du client dans la liste des position
        """
        tempindex = Data.clients_connectes.index(client)
        DataCarte.Posjoueurs[tempindex] = npos

    def verifpos(pos):
        """
        Vérifie que la position choisie est bien valide au vue de la carte
        i.e. pas sur un mur, la sortie ou sur un autre joueur
        """
        line = 1
        carac = 1
        templine = ""
        status = False
        for char in DataCarte.plan:
            carac += 1
            if char == "\n":
                line +=1
                carac = 0
                templine += char
                continue
            
            if line == pos[1] and carac == pos[0]:
                if char == "O" or char == "x":
                    status = False
                elif char == "U":
                    DataCarte.victoire = True
                else:
                    templine += "x"
                    status = True
            else:
                templine += char
        
        if status == True:
            DataCarte.plan = templine
        return status



