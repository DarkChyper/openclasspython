#!/usr/bin/python3.4

from tkinter import *

fenetre = Tk()

cadre = Labelframe(fenetre, width=768, height=576, borderwidth=1, text="Notre fenêtre")
cadre.pack(fill=BOTH)


#message.pack(side="top", fill=BOTH)

fenetre.mainloop()