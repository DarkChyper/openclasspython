#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
from threading import Thread, RLock
from tkinter import *
from time import *

# Imports interne
from .client_class import *
from .client_function import *

class Affichage(Frame):
	def __init__(self, fenetre, **kwargs):
		Frame.__init__(self, fenetre, width=768, height=576,bg="ivory", **kwargs)
		self.pack(fill=BOTH, expand=1)

		# creation des cadres
		# cadre hauts
		self.up = Frame(self, width=768, height=400, borderwidth=0,bg="ivory")
		self.up.pack(side="top", fill=BOTH, expand=YES)

		# cadre bas
		self.down = Frame(self, width=768, height=176, borderwidth=0,bg="ivory")
		self.down.pack(side="bottom", fill=BOTH, expand=YES)

		# cadre de la grille dans le cadre haut
		self.grille = LabelFrame(self.up, width=498, height=500, borderwidth=0, bg="black", fg="white", text="Le labyrinthe :")
		self.grille.pack(side="left", expand=1, fill=BOTH, padx=10, pady=10)

		# texte de la grille
		Label(self.grille, text=Data.txtGrille, bg="black", fg="white").pack(side="left", fill=BOTH, expand=1)

		# cadre des infos du jeu das le cadre haut
		self.infos = LabelFrame(self.up, width=270, height=500, borderwidth=0, bg="blue", text="Infos de la partie :")
		self.infos.pack(side="right", padx=10, pady=10, fill=BOTH)

		# texte des infos des messages du serveur :
		self.canvaInfo = Canvas(self.infos, width=270, height=500, bg="black")
		self.canvaInfo.pack(side="left", padx=10, expand=YES, fill=BOTH)

		self.listeInfo = self.canvaInfo.create_text(10,10, fill="white", text=Data.txtListe)

		#Label(msg, text="Data.txtMSG").pack(expand="yes", fill=BOTH)
		self.canvas = Canvas(self.down, width=498, height=76, bg="black")
		self.canvas.pack(side="left", padx=10, expand=YES, fill=BOTH) 

		self.Messages = self.canvas.create_text(60,20,fill="white", text=Data.txtMSG) 

		# cadre des commandes dans le cadre 
		self.cmd = LabelFrame(self.down, width=270, height=76, borderwidth=0, bg="grey", text="Commandes")
		self.cmd.pack(side="left", fill=BOTH, expand=1)


		# cadre du type d'action
		self.tipe = Frame(self.cmd, width=120, height=76, bg="grey")
		self.tipe.pack(side="left",fill=BOTH, expand=1)

		self.value = StringVar() 
		self.bouton1 = Radiobutton(self.tipe, text="mouvement", variable=self.value, value="1", bg="grey")
		self.bouton2 = Radiobutton(self.tipe, text="murer         ", variable=self.value, value="2", bg="grey")
		self.bouton3 = Radiobutton(self.tipe, text="creuser       ", variable=self.value, value="3", bg="grey")
		self.bouton1.pack()
		self.bouton2.pack()
		self.bouton3.pack()

		# cadre des directions
		self.dire = Frame(self.cmd, width=150, height=76, bg="grey")
		self.dire.pack(side="right", fill=BOTH, expand=1)

		# boutons de directions
		Button(self.dire, text='^', borderwidth=1, command=self.haut).grid(row=1, column=2)
		Button(self.dire, text='<', borderwidth=1, command=self.gauche).grid(row=2, column=1)
		Button(self.dire, text='C', borderwidth=1, command=self.begin).grid(row=2, column=2)
		Button(self.dire, text='>', borderwidth=1, command=self.droite).grid(row=2, column=3)
		Button(self.dire, text='v', borderwidth=1, command=self.bas).grid(row=3, column=2)

	def MaJInfos(self):
		"""Boucle qui permet de mettre a jour l'affichage des textes"""
		self.canvaInfo.delete(self.listeInfo)
		self.canvas.delete(self.Messages)

		self.Messages = self.canvas.create_text(60,20,fill="white", text=Data.txtMSG) 
		self.listeInfo = self.canvaInfo.create_text(10,10, fill="white", text=Data.txtListe)

		self.after(10, self.MaJInfos)

	def evaluerType(self):
		letype = value.get()
		if letype == "" or letype == "1" or letype == " ":
			return ""
		elif letype == "2":
			return "M"
		elif letype == "3":
			return "C"
		else : 
			return ""

	def begin(self):
		if Data.init and Data.start == False:
			message = "INI" + Data.pseudo
			with Data.verrou_send :
				Data.message_send = message

	def terminer(self):
		message = "EXI" + Data.pseudo
		with Data.verrou_send :
			Data.message_send = message
		self.quit()

	def haut(self):
		if Data.init and Data.start and Data.utu:
			letype = self.evaluerType()
			message = "MVT" + letype + "N"
			with Data.verrou_send :
				Data.message_send = message
				Data.utu = False

	def bas(self):
		if Data.init and Data.start and Data.utu:
			letype = self.evaluerType()
			message = "MVT" + letype + "S"
			with Data.verrou_send :
				Data.message_send = message
				Data.utu = False


	def gauche(self):
		if Data.init and Data.start and Data.utu:
			letype = self.evaluerType()
			message = "MVT" + letype + "O"
			with Data.verrou_send :
				Data.message_send = message
				Data.utu = False


	def droite(self):
		if Data.init and Data.start and Data.utu:
			letype = self.evaluerType()
			message = "MVT" + letype + "E"
			with Data.verrou_send :
				Data.message_send = message
				Data.utu = False

class Interface(Thread):
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""

	def __init__(self, **kwargs):
		Thread.__init__(self)


	def run(self, **kwargs):
		
		fenetre = Tk()
		self.interface = Affichage(fenetre)
		self.interface.mainloop()
		self.interface.destroy()



