#!/usr/bin/env python
# coding: utf-8

# Externe
from socket         import *
from threading      import Thread
from tkinter        import *
# Interne
from res.func       import *
from res.Listener   import Listener
from res.Sender     import Sender
from res.settings   import *


########## CLASSE CLIENT ##########


class Client(Frame):

    def __init__(self, **kwargs):
        # Intialisation fenêtre
        fenetre = Tk()
        fenetre.resizable(FALSE,FALSE)
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)

        # Création des widgets
        self._map_label = Label(fenetre, justify=LEFT, font="Courier", bg="white", relief=GROOVE)
        message_aide = Label(fenetre, text=afficher_aide(), justify=LEFT)
        self._message_label = Label(fenetre, justify="left")
        self._bouton_envoyer = Button(fenetre, text="Envoyer")
        self._input_client = StringVar()
        ligne_texte = Entry(fenetre, textvariable=self._input_client, width=17)

        # Pack
        self._message_label.grid(row=0, column=0, padx=10, pady=5, sticky=W+N)
        self._map_label.grid(row=1, column=0, pady=10, padx=10, sticky=W+N)
        message_aide.grid(row=1, column=1, pady=10, padx=10, sticky=W+N)
        ligne_texte.grid(row=3, column=0,  sticky=W+N, pady=10, padx=10)
        self._bouton_envoyer.grid(row=3, column=1, sticky=W+E+N+S, pady=10, padx=10)
        ligne_texte.focus()

        self.connexion = init_connexion_serveur()
        """Connexion avec le serveur"""
        self.id_ = self._obtenir_id()
        """Identifiant du joueur du client"""
        self._listener = Listener(self)
        self._sender = Sender(self)

        # On démarre l'écoute du serveur
        self._listener.start()

        # Dernières assignations
        self._bouton_envoyer.config(command=self._send)
        fenetre.protocol("WM_DELETE_WINDOW", self.terminer)

        # Lancement de la fenêtre
        self.mainloop()

        # On attend la fin du Thread et on quitte lorsque la fenêtre est fermée
        self._listener.join()
        exit(0)

    def terminer(self):
        try:
            print("Client.terminer()")
            self.connexion.close()
        except:
            pass
        finally:
            self.quit()
            exit(0)

    def _obtenir_id(self):
        """
            Permet d'obtenir l'ID sous forme d'entier
        """

        print("obtenir_id") # DEBUG

        try:
            msg = self.connexion.recv(1024).decode()
            id_ = int(msg)
        except:
            print("Récupération de l'ID impossible")
            self.terminer()

        self.message_label = "Bienvenue, joueur {}.\nAppuyez sur c pour commencer !".format(id_ + 1)

        print(self.message_label) # DEBUG

        return id_

    def _send(self):
        self._sender.send(self._input_client)
        self._input_client.set("")

########## PROPRIETES ##########
    def _set_message_label(self, msg):
        self._message_label['text'] = msg

    def _get_message_label(self):
        return self._message_label['text']

    def _set_map_label(self, msg):
        self._map_label['text'] = msg

    def _get_map_label(self):
        return self._map_label['text']

    message_label = property(_get_message_label, _set_message_label)
    map_label = property(_get_map_label, _set_map_label)

########## FONCTIONS CLIENT ##########


def init_connexion_serveur():
    """
        Initialise la connexion du client au serveur
    """

    print("On tente de se connecter au serveur...")
    try:
        connexion = socket(AF_INET, SOCK_STREAM)
        connexion.connect((hote, port))
    except ConnectionError:
        print("Connexion au serveur impossible")
    else:
        print("Connexion établie avec le serveur.")

    return connexion

########## FENETRE ##########


def afficher_aide():
    """
        Affiche toutes les touches possibles
    """
    msg = "Aide :\n\n"
    for c, v in touches.items():
        if c == 'commencer':
            continue

        msg +="{} : {}\n".format(c.title(), v)

    return msg

client = Client()