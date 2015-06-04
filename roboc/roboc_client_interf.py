#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from tkinter import *
from roboc_client_class import *

class Envoi():
    """
    Gère les différents aspect de la communication vers le server.
    Le chat pourrait être placé dans cette class.
    """
    def __init__(self):
        pass
    
    def envoi(message):
        """
        suivant le point du programme le "mode" varie et permet de préfixer différement le message pour que le serveur les reconnaissent.
        là encore un préfixe sera ajouté pour le chat
        """
        if Data.mode == "choix":
            message = "chx" + message
            Data.lstmsg = []
        message = message.encode()
        Data.connexion.send(message)
        
class MajPrincipal(Data):
    """
    Thread chargé de la réception des messages en provenance du server.
    Les données sont stockées dans une liste commune avant affichage.
    """
    def __init__(self):
        #Thread.__init__(self)
        pass
        
    def rafraich(interf):
        """
        effectue en continu la mise à jour du cadre principal de la fenêtre
        """
        while Data.client:
            try:
                interf.principal["text"] = Data.lstmsg[0]
            except:
                interf.principal["text"] = "Veuillez patienter"

class Interface(Frame, Envoi, MajPrincipal):
    """
    Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre.
    """
    
    def __init__(self, fenetre, **kwargs):
        """
        Création de la fenêtre
        """
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        
        # Création de nos widgets
        
        comm = LabelFrame(fenetre, text="Entrez un message pour le serveur :", padx=25, pady=25)
        comm.pack(fill="both", expand="yes")
        
        self.var_texte = StringVar()
        self.ligne_texte = Entry(comm, textvariable=self.var_texte, width=5)
        self.ligne_texte.pack(side = "left")
        self.ligne_texte.focus_set()

        self.bouton_cliquer = Button(comm, text="Envoyer", fg="red",command=self.cliquer)
        self.bouton_cliquer.pack(side="right")

        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.principal = Label(self, text = "Veuillez patienter")
        self.principal.pack()
        
        MajPrincipal.rafraich(self)
    
    def cliquer(self):
        """
        Il y a eu un clic sur le bouton.
        On envoi le contenu du champ vers le server.
        """
        Envoi.envoi(self.var_texte.get())
        self.var_texte.set("")




