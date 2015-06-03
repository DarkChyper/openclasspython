#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from tkinter import *
from roboc_client_class import *

class Envoi():
    def __init__(self):
        pass
    
    def envoi(message):
        if Data.mode == "choix":
            message = "chx" + message
        message = message.encode()
        Data.connexion.send(message) 

class Interface(Frame, Envoi):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        
        # Création de nos widgets
        #self.message = Label(self, text="Entrez un message pour le serveur :")
        #self.message.pack()
        
        comm = LabelFrame(fenetre, text="Entrez un message pour le serveur :", padx=40, pady=40)
        comm.pack(fill="both", expand="yes")
 
        #Label(l, text="A l'intérieure de la frame").pack()
        
        self.var_texte = StringVar()
        ligne_texte = Entry(comm, textvariable=self.var_texte, width=5)
        ligne_texte.pack()
        ligne_texte.focus_set()
        
        self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        self.bouton_quitter.pack(side="left")
        
        self.bouton_cliquer = Button(self, text="Envoyer message", fg="red",
                command=self.cliquer)
        self.bouton_cliquer.pack(side="right")
        
        if len(Data.lstmsg) == 0:
            Data.lstmsg.append("")
        self.principal = Label(self, text = Data.lstmsg[0])
        self.principal.pack()
    
    def cliquer(self):
        """Il y a eu un clic sur le bouton.
        On change la valeur du label message."""
        
        Envoi.envoi(self.var_texte.get())
        self.var_texte.set("")



