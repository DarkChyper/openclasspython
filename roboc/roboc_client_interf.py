# -*- coding: utf8 -*-

from threading import Thread
from tkinter import *
from roboc_client_class import *

class Envoi():
    """
    Gère les différents aspect de la communication vers le server.
    Le chat pourrait être placé dans cette class.
    """
    def __init__(self):
        pass
    
    def verifmvt(message):
        """
        on contrôle la validité (d'un point de vue règles) du mouvement avant son envoi
        l'idée est de limiter les échanges avec le serveur
        """
        status = False
        message = message.upper()
        #message de mouvement strictement uniquement
        if message[0] == "N" or message[0] == "S" or message[0] == "E" or message[0] == "O":
            if len(message) == 1:
                status = True
            else:
                try:
                    temp = int(message[1:])
                    status = True
                except:
                    pass
        #messages de ouverture porte ou murer uniquement
        elif message[0] == "P" or message[0] == "M":
            if message[1:] == "N" or message[1:] == "S" or message[1:] == "E" or message[1:] == "O":
                status = True
        
        #les autres messages aboutissent directement ici
        return status
    
    def envoi(message):
        """
        la fonction envoi les messages qui lui sont passés en ajoutant un préfixe de mouvement.
        Le passage en uppercase simplifie le travail coté serveur
        l'ajout du suffixe 1 est fait pour la même raison
        """
        if len(message) == 1:
            message += "1"
        message = message.upper()
        message = "mvt" + message
        message = message.encode()
        Data.connexion.send(message)
        Data.turn = False
        
def uppercarte():
    """
    Mise en majuscule du X correspondant au joueur
    """
    line = 1
    carac = 1
    templine = ""
    for char in Data.lstmsg[0]:
        carac += 1
        if char == "\n":
            line +=1
            carac = 0
            templine += char
            continue
                
        if line == Data.pos[1] and carac == Data.pos[0]:
            templine += char.upper()
        else:
            templine += char
        
    Data.lstmsg[0] = templine

class Interface(Frame, Envoi):
    """
    Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre.
    """
    
    def __init__(self, fenetre, **kwargs):
        """
        Création de la fenêtre
        """
        #initialisation globale de la fenêtre
        Frame.__init__(self, fenetre)
        self.pack(fill = BOTH)
        
        #création des frames
        
        self.ctrl = Frame(self, borderwidth=2, relief=GROOVE, bg="white")
        self.ctrl.pack(fill = Y, side = RIGHT)
        
        self.carte = Canvas(self, width=200, height=400)
        self.carte.pack(fill = Y, side = LEFT)
        
        self.comm = LabelFrame(self.ctrl, text="Entrez un message pour le serveur :")
        self.comm.pack(fill = X, side = BOTTOM)
        
        # Création de nos widgets
        
            #champ d'entrée
        self.var_texte = StringVar()
        self.ligne_texte = Entry(self.comm, textvariable = self.var_texte, width = 5)
        self.ligne_texte.pack(side = LEFT)
        self.ligne_texte.focus_set()

            #bouton envoi
        self.bouton_cliquer = Button(self.comm, text = "Envoyer", fg = "red",command = self.cliquer)
        self.bouton_cliquer.pack(side = RIGHT)

            #bouton quitter
        self.bouton_quitter = Button(self.ctrl, text = "Quitter", command = self.quit)
        self.bouton_quitter.pack(side = TOP, padx=10, pady=10)
        
            #message information
        self.infos = Label(self.ctrl,text="test")
        self.infos.pack(padx=10,pady=100)
        
            #affichage carte
        self.principal = self.carte.create_text(100, 200, text = "Veuillez patienter", font = "UbuntuMono 16")
        
        #on démarre une première fois majprincipal et majinfos pour lancer le cycle des mise à jour
        self.majprincipal()
        self.majinfos()
    
    def cliquer(self):
        """
        Il y a eu un clic sur le bouton.
        On envoi le contenu du champ vers le server.
        """
        if Data.turn == True:
            valide = Envoi.verifmvt(self.var_texte.get())
            if valide:
                Envoi.envoi(self.var_texte.get())
        self.var_texte.set("")
        Data.lstinfos[0] = ""
        
    def majprincipal(self):
        """
        after permet à la fonction de se relancer en automatique toute les secondes
        actualise le contenu de la fenêtre du client
        """
        if Data.lstmsg[0] != None:
            uppercarte()
            self.carte.delete(self.principal)
            self.principal = self.carte.create_text(100, 200, text=Data.lstmsg[0], font="UbuntuMono 16")
        else:
            self.carte.delete(self.principal)
            self.principal = self.carte.create_text(100, 200, text="Veuillez patienter", font="UbuntuMono 16")
            
        self.after(10, self.majprincipal)
        
    def majinfos(self):
        """
        after permet à la fonction de se relancer en automatique toute les secondes
        actualise le contenu de la fenêtre du client
        """
        if Data.lstinfos[0] != None:
            self.infos["text"] = Data.lstinfos[0]
        else:
            self.infos["text"] = ""
            
        self.after(10, self.majinfos)
        

class Affichage(Thread):
    """
    Thread chargé de l'envoi des messages entrés par l'utilisateur
    """
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
        """Boucle active"""
        self.fenetre = Tk()
        self.interface = Interface(self.fenetre)
        self.interface.mainloop()
        self.interface.destroy()

                
