#!/usr/bin/python3.4
# coding: utf-8


from tkinter import *
import tkinter.scrolledtext as tkst

class Interface(Frame):
	"""Notre fenêtre principale.
	Tous les widgets sont stockés comme attributs de cette fenêtre."""

	def __init__(self, fenetre, monText, txtConsole, **kwargs):
		Frame.__init__(self, fenetre, width=768, height=576,bg="ivory", **kwargs)
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
		Label(grille, text=monText, bg="black", fg="white").pack(side="left", fill=BOTH, expand=1)

		# cadre des infos du jeu das le cadre haut
		infos = LabelFrame(up, width=270, height=500, borderwidth=0, bg="blue", text="Infos de la partie :")
		infos.pack(side="right", padx=10, pady=10, fill=BOTH)

		# cadre des messages dans le cadre bas
		"""msg = LabelFrame(down, width=498, height=76, borderwidth=0, bg="grey", text="Infos du serveur :")
		msg.pack(side="left")"""

		# texte des infos des messages du serveur :
		"""editArea = tkst.ScrolledText(master=msg, wrap=WORD, height=50)
		editArea.pack(fill='both', expand='yes')
		editArea.insert(INSERT,txtConsole)"""
		#Label(msg, text="txtConsole").pack(expand="yes", fill=BOTH)
		canvas = Canvas(down, width=498, height=76, bg="black")
		canvas.pack(side="left", padx=10, expand=YES, fill=BOTH) 

		canvas.create_text(60,20,fill="white", text=txtConsole) 

		# cadre des commandes dans le cadre bas
		cmd = LabelFrame(down, width=270, height=76, borderwidth=0, bg="grey", text="Commandes")
		cmd.pack(side="left", fill=BOTH, expand=1)

		# cadre du type d'action
		tipe = Frame(cmd, width=120, height=76, bg="grey")
		tipe.pack(side="left",fill=BOTH, expand=1)

		value = StringVar() 
		bouton1 = Radiobutton(tipe, text="mouvement", variable=value, value=1, bg="grey")
		bouton2 = Radiobutton(tipe, text="murer         ", variable=value, value=2, bg="grey")
		bouton3 = Radiobutton(tipe, text="creuser       ", variable=value, value=3, bg="grey")
		bouton1.pack()
		bouton2.pack()
		bouton3.pack()

		# cadre des directions
		dire = Frame(cmd, width=150, height=76, bg="grey")
		dire.pack(side="right", fill=BOTH, expand=1)

		# boutons de directions
		Button(dire, text='^', borderwidth=1, command=fenetre.quit).grid(row=1, column=2)
		Button(dire, text='<', borderwidth=1, command=fenetre.quit).grid(row=2, column=1)
		Button(dire, text='>', borderwidth=1, command=fenetre.quit).grid(row=2, column=3)
		Button(dire, text='v', borderwidth=1, command=fenetre.quit).grid(row=3, column=2)


fenetre = Tk()
monText = "Ceci sera \nremplacé par \nle labyrinthe"
txtConsole = "Messages\nen provenance\ndu serveur de jeu\nDarkMaze\n\nOn teste\nalors on fait\nbeaucoup\nde\nsauts\nde\nligne."
interface = Interface(fenetre, monText, txtConsole)

interface.mainloop()
interface.destroy()