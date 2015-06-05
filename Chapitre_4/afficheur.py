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
		up.pack(side="top", fill=BOTH)

		# cadre bas
		down = Frame(self, width=768, height=176, borderwidth=0,bg="ivory")
		down.pack(side="bottom", fill=BOTH)

		# cadre de la grille dans le cadre haut
		grille = LabelFrame(up, width=568, height=400, borderwidth=0, bg="black", fg="white", text="Le labyrinthe")
		grille.pack(side="left", expand=1, fill=BOTH, padx=20, pady=20)

		# texte de la grille
		Label(grille, text=monText, bg="black", fg="white").pack(side="left", fill=BOTH, expand=1)

		# cadre des infos du jeu das le cadre haut
		infos = LabelFrame(up, width=200, height=400, borderwidth=0, bg="ivory", text="Infos de la partie")
		infos.pack(side="right", fill=BOTH)

		# cadre des messages dans le cadre bas
		msg = LabelFrame(down, width=518, height=176, borderwidth=0, bg="ivory", text="Infos du serveur")
		msg.pack(side="left", fill=BOTH)

		"""# texte des infos des messages du serveur :
		editArea = tkst.ScrolledText(master = msg, wrap = WORD, height=8, width=50)
		editArea.pack(expand=False)
		editArea.insert(INSERT,txtConsole)"""

		# cadre des commandes dans le cadre bas
		cmd = LabelFrame(down, width=250, height=176, borderwidth=0, bg="ivory", text="Commandes")
		cmd.pack(side="left", fill=BOTH, expand=1)

		# cadre du type d'action
		tipe = Frame(cmd, width=100, height=176)
		tipe.pack(side="left")

		"""value = StringVar() 
		bouton1 = Radiobutton(tipe, text="mouvement", variable=value, value=1)
		bouton2 = Radiobutton(tipe, text="murer", variable=value, value=2)
		bouton3 = Radiobutton(tipe, text="creuser", variable=value, value=3)
		bouton1.pack(side="top")
		bouton2.pack(side="top")
		bouton3.pack(side="bottom")"""

		# cadre des directions
		dire = Frame(cmd, width=150)
		dire.pack(side="right", fill=BOTH)

		# sous cadres de directions
		dirup = Frame(dire)
		dirup.pack(side="top", fill=X)

		dirmid = Frame(dire)
		dirmid.pack(fill=X)

		dirdown = Frame(dire)
		dirdown.pack(side="bottom", fill=X)

		# boutons dans les sous cadres
		bup = Button(dirup, text="^", command=fenetre.quit)
		bup.pack()

		ble = Button(dirmid, text="<", command=fenetre.quit)
		ble.pack()

		bri = Button(dirmid, text=">", command=fenetre.quit)
		bri.pack()

		bdo = Button(dirdown, text="v", command=fenetre.quit)
		bdo.pack()

fenetre = Tk()
monText = "Ceci sera \nremplacé par \nle labyrinthe"
txtConsole = "Messages\nen provenance\ndu serveur de jeu\nDarkMaze\n\nOn teste\nalors on fait\nbeaucoup\nde\nsauts\nde\nligne."
interface = Interface(fenetre, monText, txtConsole)

interface.mainloop()
interface.destroy()