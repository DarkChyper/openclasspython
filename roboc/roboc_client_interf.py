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
    
    def envoi(message):
        """
        suivant le point du programme le "mode" varie et permet de préfixer différement le message pour que le serveur les reconnaissent.
        là encore un préfixe sera ajouté pour le chat
        """
        message = "mvt" + message
        message = message.encode()
        Data.connexion.send(message)

class Interface(Frame, Envoi):
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
        
        #on démarre une première fois majprincipal pour lancer le cycle des mise à jour
        self.majprincipal()
    
    def cliquer(self):
        """
        Il y a eu un clic sur le bouton.
        On envoi le contenu du champ vers le server.
        """
        Envoi.envoi(self.var_texte.get())
        self.var_texte.set("")
        
    def majprincipal(self):
        """
        after permet à la fonction de se relancer en automatique toute les secondes
        actuelise le contenu de la fenêtre du client
        """
        try:
            self.principal["text"] = Data.lstmsg[0]
        except:
            self.principal["text"] = "Veuillez patienter"
            
        self.after(1000, self.majprincipal)
        

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
    
    def stop(self):
        self.interface.destroy()
                
