#!/usr/bin/python3.4

from tkinter import *

fenetre = Tk()

cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
cadre.pack(padx=10, pady=10, fill=BOTH, expand="yes")
#Label(cadre, text="content", width=768, height=576).pack(padx=10, pady=10, fill=BOTH, expand="yes")
#Label(cadre, text="Hello World", width=768, height=576).pack()

canvas = Canvas(cadre,width=750, height=550, bg='blue')
canvas.pack(expand=YES, fill=BOTH) 

canvas.create_text(50,20,text="Test\navec des sauts\nde ligne.") 
#message.pack(side="top", fill=BOTH)

fenetre.mainloop()