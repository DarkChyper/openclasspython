# -*-coding:Utf-8 -*

"""Ce module contient la classe Labyrinthe."""

class Labyrinthe:

	"""Classe représentant un labyrinthe.
	   On représente un labyrinthe par ses coordonnees et l'objet qui se situe aux coordonnees
	   exemple de labyrinthe :
	     ooooo   en largeur on a la coordonnee x 
	     o o o   en hauteur on a la coordonnee y
	     o oxu   en hauteur (les etages) on a la coorodnnee z
	     o   o   l'objet est la coordonnee v
	     ooooo
	     Le Robot de valeu x a donc comme coordonnees la liste (4,3,1,x)
	     La sortie a pour coordonnees la liste (5,3,1,u)
	"""

	def __init__(self, robot, obstacles):
		self.robot = robot
		self.grille = {}
		# ... 

