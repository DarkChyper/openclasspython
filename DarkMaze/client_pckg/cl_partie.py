#!/usr/bin/python3.4
# -*- coding: utf8 -*-

""" Interface client"""

# Imports externes
import socket
from threading import Thread, RLock
from time import *
from tkinter import *

# Imports internes
from .cl_function import *
from .cl_data import *


class Affichage(Thread):
	""" Thread d'Affichage """
	def __init__(self, **kwargs):
		Thread.__init__(self)


	def run(self, **kwargs):
		
		fenetre = Tk()

		self.interface = Interface(fenetre)
		self.interface.mainloop()
		self.interface.destroy()

class Interface(Frame):
	""" Classe instanciée qui crée notre fenêtre d'affichage et les fonctions des boutons """
	def __init__(self, fenetre, **kwargs):
		fenetre.protocol("WM_DELETE_WINDOW", self.quitter)
		# des variables pour les méthodes #########################################################
		###########################################################################################
		with Data.verrou_msg:
			self.msg = Data.txtMSG

		with Data.verrou_liste:
			self.liste = Data.txtListe

		# La fenêtre principale ###################################################################
		###########################################################################################
		Frame.__init__(self, fenetre, width=800, height=600,bg="black", **kwargs)
		self.pack(fill=BOTH, expand=1)

		# Les frames ##############################################################################
		###########################################################################################
		self.up = Frame(self, width=780, height=380, bg="ivory")
		self.up.pack(side="top", padx=10, pady=10, fill=BOTH, expand=1)

		self.down = Frame(self, width=780, height=180, bg="ivory")
		self.down.pack(side="bottom", padx=10, pady=10, fill=BOTH, expand=1)

		self.grille = Frame(self.up, width=560, height=360, bg="black")
		self.grille.pack(side="left", padx=10, pady=10, fill=Y, expand=0)

		self.menu = Frame(self.up, width=180, height=360, bg="ivory")
		self.menu.pack(side="right", padx=10, pady=10, fill=Y, expand=0)

		self.menu_boutons = Frame(self.menu, width=180, height=30, bg="ivory")
		self.menu_boutons.pack(side="top", padx=0, pady=0, fill=X, expand=0)

		self.menu_liste = LabelFrame(self.menu, width=180, height=330, bg="black", fg="white", text="Liste des joueurs")
		self.menu_liste.pack(side="bottom", padx=0, pady=0, fill=X, expand=0)

		self.msg = Frame(self.down, width=560, height=160, bg="black")
		self.msg.pack(side="left", padx=10, pady=10, fill=Y, expand=0)

		self.cmd = LabelFrame(self.down, width=180, height=160, bg="ivory", text="Commandes")
		self.cmd.pack(side="right", padx=10, pady=10, fill=BOTH, expand=0)

		self.cmd_type = Frame(self.cmd, width=180, height=30, bg="ivory")
		self.cmd_type.pack(side="top", padx=0, pady=0, fill=X, expand=0)

		self.cmd_dir = Frame(self.cmd, width=180, height=30, bg="ivory")
		self.cmd_dir.pack(side="bottom", padx=10, pady=10, fill=BOTH, expand=1)


		# les modules ############################################################################
		##########################################################################################
		##les canvas
		self.canvas_grille = Canvas(self.grille, width=560, height=360, bg="black")
		self.canvas_grille.pack(side="left", padx=0, pady=0, fill=BOTH, expand=1)


		################ les textes
		###########################################################################################
		self.texte_grille = self.canvas_grille.create_text(280, 180, fill="green",font="LiberationMono", text=Data.txtGrille)

		#texte en provenance du serveur
		self.texte_console = Text(self.msg, wrap=WORD, relief=FLAT, height=10, bg="black", fg="green")
		self.texte_console.insert(END, self.msg)
		self.texte_console.config(state=DISABLED)
		self.texte_console.pack(side="left", padx=0, pady=0, expand=0)

		#liste des joueurs 
		self.texte_liste = Text(self.menu_liste, wrap=WORD, relief=FLAT, bg="black", fg="green", width=25)
		self.texte_liste.insert(END, self.liste)
		self.texte_liste.config(state=DISABLED)
		self.texte_liste.pack(side="left", padx=0, pady=0, expand=0)


		################ les variables
		########################################################################################
		self.distance = ""

		################ les boutons
		########################################################################################
		Button(self.menu_boutons, text="Commencer", command=self.begin, relief=FLAT, bg="black", fg="ivory", cursor="target").pack(side="left", expand=1)
		Button(self.menu_boutons, text="Quitter", command=self.quitter, relief=FLAT, bg="black", fg="ivory", cursor="target").pack(side="right", expand=1)

		self.value = StringVar() 
		self.bouton1 = Radiobutton(self.cmd_type, text="MVT", variable=self.value, value="1")
		self.bouton2 = Radiobutton(self.cmd_type, text="MUR", variable=self.value, value="2")
		self.bouton3 = Radiobutton(self.cmd_type, text="CRE", variable=self.value, value="3")
		self.bouton1.pack(side="left")
		self.bouton2.pack(side="left")
		self.bouton3.pack(side="right")

		Button(self.cmd_dir, text='^', borderwidth=1, command=self.haut).grid(row=1, column=2)
		Button(self.cmd_dir, text='<', borderwidth=1, command=self.gauche).grid(row=2, column=1)
		Button(self.cmd_dir, text='>', borderwidth=1, command=self.droite).grid(row=2, column=3)
		Button(self.cmd_dir, text='v', borderwidth=1, command=self.bas).grid(row=3, column=2)
	
		# Appel des méthodes ###################################################################
		########################################################################################
		self.majInfos()

	def majInfos(self):
		""" Méthode qui mets à jour, en boucle, le texte des canvas """
		self.canvas_grille.delete(self.texte_grille)

		# texte de la grille
		with Data.verrou_grille :
			if Data.txtGrille != "":
				self.texte_grille = self.canvas_grille.create_text(280,180,fill="green",font="LiberationMono", text=Data.txtGrille) 
			else :
				self.texte_grille = self.canvas_grille.create_text(280,180,fill="green", text="En attente de joueur") 

		# texte de la console
		with Data.verrou_msg :
			if Data.txtMSG != self.msg:
				self.texte_console.config(state=NORMAL)
				self.texte_console.delete("1.0","20.0")
				self.texte_console.insert(END, Data.txtMSG)
				self.texte_console.config(state=DISABLED)
				self.texte_console.pack(side="left", padx=0, pady=0, expand=0)
				self.msg = Data.txtMSG

		#texte de la liste
		with Data.verrou_liste:
			if Data.txtListe != self.liste:
				self.texte_liste.config(state=NORMAL)
				self.texte_liste.delete("1.0","20.0")
				self.texte_liste.insert(END, Data.txtListe)
				self.texte_liste.config(state=DISABLED)
				self.texte_liste.pack(side="left", padx=0, pady=0, expand=0)
				self.liste = Data.txtListe

		# on boucle si le jeu n'est pas terminé
		if Data.nonEnd == False:
			printd(Data.nonEnd)
			try:
				self.quit()
			except RuntimeError: # rustine pour éviter une erreur de sortie liée à une non utilisation d'une file d'attente
				pass
		else:
			self.after(10, self.majInfos)

	def begin(self):
		""" Méthode qui lance la partie lorsque le joueur appuie sur le bouton"""
		if Data.init == True and Data.start == False :
			Data.init = False
			with Data.verrou_msg:
				Data.gestionMSG("Initialisation envoyée au serveur, merci de patienter.")
			with Data.verrou_send:
				Data.message_send = "INI" + Data.pseudo

	def quitter(self):
		""" Fermeture propre des connexions, du jeu et des fenetres """
		if Data.init == False and Data.start and Data.isutu:
			Deconnexion(True) 
		else :
			Deconnexion(False) 
		

	def evaluerType(self):
		"""évalue quelle action est demandée par le joueur
		   retourne MUR pour murer, CRE pour creuser ou MVT dans tous les autres cas (un déplacement par exemple)"""
		letype = self.value.get()
		if letype == "" or letype == "1" or letype == " ":
			return "MVT"
		elif letype == "2":
			return "MUR"
		elif letype == "3":
			return "CRE"
		else : 
			print("Type d'action inconnue, Déplacement par défaut.")
			return "MVT"

	def haut(self):
		if Data.init == False and Data.start and Data.isutu:
			letype = self.evaluerType()
			message =  letype + "N" + self.distance
			with Data.verrou_send :
				Data.message_send = message
				Data.isutu = False

	def bas(self):
		if Data.init == False and Data.start and Data.isutu:
			letype = self.evaluerType()
			message = letype + "S" + self.distance
			with Data.verrou_send :
				Data.message_send = message
				Data.isutu = False


	def gauche(self):
		if Data.init == False and Data.start and Data.isutu:
			letype = self.evaluerType()
			message = letype + "O" + self.distance
			with Data.verrou_send :
				Data.message_send = message
				Data.isutu = False


	def droite(self):
		if Data.init == False and Data.start and Data.isutu:
			letype = self.evaluerType()
			message = letype + "E" + self.distance
			with Data.verrou_send :
				Data.message_send = message
				Data.isutu = False