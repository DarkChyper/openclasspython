# -*-coding:Utf-8 -*

"""Ce module contient la classe Carte."""
from labyrinthe import *

class Carte:
	"""
	Objet de transition entre un fichier et un labyrinthe.
	"""
	def __init__(self, name, chaine):
		self.nom = name
		self.labyrinthe_txt = chaine
		self.map = Labyrinthe(chaine)
		# self.labyrinthe = creer_labyrinthe_depuis_chaine(chaine)
		self.current = False			# Si la carte est en cours
	def __repr__(self):
		return "<Carte {}>".format(self.nom)