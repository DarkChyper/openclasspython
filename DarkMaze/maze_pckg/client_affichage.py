#!/usr/bin/python3.4
# -*- coding: utf8 -*-

"""
"""

# Imports externes
from threading import Thread, RLock
from time import *

# Imports interne
from .client_class import *
from .client_function import *

class Interface(Thread, Frame):
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""

	def __init__(self):
		Thread.__init__(self)
		self.fenetre = Tk()


	def run(self, **kwargs):
		Frame.__init__(self, self.fenetre, width=768, height=576,bg="ivory", **kwargs)
		self.pack(fill=BOTH, expand=1)

		# creation des cadres
		# cadre haut
		up = Frame(self, width=768, height=400, borderwidth=0,bg="ivory")
		up.pack(side="top", fill=BOTH, expand=YES)

		# cadre bas
		down = Frame(self, width=768, height=176, borderwidth=0,bg="ivory")
		down.pack(side="bottom", fill=BOTH, expand=YES)

		# cadre de la grille dans le cadre haut
		grille = LabelFrame(up, width=498, height=500, borderwidth=0, bg="black", fg="white", text="Le labyrinthe :")
		grille.pack(side="left", expand=1, fill=BOTH, padx=10, pady=10)

		# texte de la grille
		Label(grille, text=Data.txtGrille, bg="black", fg="white").pack(side="left", fill=BOTH, expand=1)

		# cadre des infos du jeu das le cadre haut
		infos = LabelFrame(up, width=270, height=500, borderwidth=0, bg="blue", text="Infos de la partie :")
		infos.pack(side="right", padx=10, pady=10, fill=BOTH)

		# cadre des messages dans le cadre bas
		"""msg = LabelFrame(down, width=498, height=76, borderwidth=0, bg="grey", text="Infos du serveur :")
		msg.pack(side="left")"""

		# texte des infos des messages du serveur :
		canvaInfo = Canvas(infos, width=270, height=500, bg="black")
		canvaInfo.pack(side="left", padx=10, expand=YES, fill=BOTH)

		canvaInfo.create_text(10,10, fill="white", text=Data.txtListe)

		#Label(msg, text="Data.txtMSG").pack(expand="yes", fill=BOTH)
		canvas = Canvas(down, width=498, height=76, bg="black")
		canvas.pack(side="left", padx=10, expand=YES, fill=BOTH) 

		canvas.create_text(60,20,fill="white", text=Data.txtMSG) 

		# cadre des commandes dans le cadre 
		cmd = LabelFrame(down, width=270, height=76, borderwidth=0, bg="grey", text="Commandes")
		cmd.pack(side="left", fill=BOTH, expand=1)

		if Data.init and Data.start:

			# cadre du type d'action
			tipe = Frame(cmd, width=120, height=76, bg="grey")
			tipe.pack(side="left",fill=BOTH, expand=1)

			value = StringVar() 
			bouton1 = Radiobutton(tipe, text="mouvement", variable=value, value="1", bg="grey")
			bouton2 = Radiobutton(tipe, text="murer         ", variable=value, value="2", bg="grey")
			bouton3 = Radiobutton(tipe, text="creuser       ", variable=value, value="3", bg="grey")
			bouton1.pack()
			bouton2.pack()
			bouton3.pack()

			# cadre des directions
			dire = Frame(cmd, width=150, height=76, bg="grey")
			dire.pack(side="right", fill=BOTH, expand=1)

			# boutons de directions
			Button(dire, text='^', borderwidth=1, command=self.haut).grid(row=1, column=2)
			Button(dire, text='<', borderwidth=1, command=self.gauche).grid(row=2, column=1)
			Button(dire, text='>', borderwidth=1, command=self.droite).grid(row=2, column=3)
			Button(dire, text='v', borderwidth=1, command=self.bas).grid(row=3, column=2)

		elif Data.init and ! Data.start:
			Button(cmd, text="commecer la partie", command=self.begin)

		elif ! Data.init and ! Data.start:
			pass

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
		message = "INI" = Data.pseudo
		with verrou_send :
			Data.message_send = message

	def haut(self):
		letype = evaluerType()
		message = "MVT" + letype + "N"
		with verrou_send :
			Data.message_send = message

	def bas(self):
		letype = evaluerType()
		message = "MVT" + letype + "S"
		with verrou_send :
			Data.message_send = message


	def gauche(self):
		letype = evaluerType()
		message = "MVT" + letype + "O"
		with verrou_send :
			Data.message_send = message


	def droite(self):
		letype = evaluerType()
		message = "MVT" + letype + "E"
		with verrou_send :
			Data.message_send = message

