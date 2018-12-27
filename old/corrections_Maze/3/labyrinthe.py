# -*-coding:Utf-8 -*

"""
Ce module contient la classe Labyrinthe.
"""

class Labyrinthe():
	"""
	Classe représentant un labyrinthe.
	"""
	def __init__(self, chaine):
		self.labyrinthe_initial = self.txt_to_dic(chaine)
		self.labyrinthe = self.txt_to_dic(chaine)
		self.roboc_position = ()
		self.exit_position = ()
		# largeur et hauteur max de la carte.
		self.x_max = self.get_max_x(chaine)
		self.y_max = self.get_max_y(chaine)


	def display(self):
		"""
		Permet d'afficher le labyrinthe.
		"""
		y_current = 0
		while y_current <= self.y_max :
			txt_to_display = ""
			x_current = 0
			while x_current < self.x_max:
				try:
					symbol_to_add = self.labyrinthe[(x_current, y_current)]
				except KeyError:	# quand il s'agit de la dernière clé
					symbol_to_add = ''
				x_current += 1
				txt_to_display += symbol_to_add
			y_current += 1
			print(txt_to_display)


	def get_roboc_position(self):
		"""
		Permet de connaitre les coordonnees de Roboc.
		Mets à jour et renvoie self.roboc_position() => (x, y)
		"""
		for coordonnees, symbol in self.labyrinthe.items():
			if symbol == 'X':
				self.roboc_position = coordonnees
		return self.roboc_position


	def get_exit_position(self):
		"""
		Permet de connaitre les coordonnees de la sortie.
		Renvoie self.exit_position() => (x, y)
		"""
		for coordonnees, symbol in self.labyrinthe.items():
			if symbol == 'U':
				self.exit_position = coordonnees
		return self.exit_position


	def txt_to_dic(self, chaine):
		"""
		pour convertir une chaine de caractères en un dictionnaire de la forme :
		labyrinthe = {(0,0):'O', (1,0):'X', ..... (8,7):"U"}
		"""
		txt = chaine
		labyrinthe = {}
		coor_x = 0							# correspond au numéro du caratère
		coor_y = 0							# correspond au numéro de la ligne
		for symbole in txt:
			# print("labyrinthe[{}, {}] = {}".format(coor_x, coor_y, symbole))
			labyrinthe[coor_x, coor_y] = symbole
			if symbole == "\n":				# si le caractère est un retour à la ligne...
				coor_y += 1 				# on incrémente le numéro de ligne
				coor_x = 0					# on repart au premier caractère de la ligne.
			else:
				coor_x += 1
		return labyrinthe


	def get_max_x(self, chaine):
		"""
		permet de connaître la largeur max d'une carte.
		renvoie x_max
		"""
		x_max_temp = 0
		counter = 0
		for symbole in chaine:
			counter += 1	
			if symbole == "\n" and x_max_temp <= counter:
				# si le caractère est un retour à la ligne...
				x_max_temp = counter - 1 	# - 1 pour l'index.
				counter = 0
		return x_max_temp


	def get_max_y(self, chaine):
		"""
		permet de connaître la hauteur max d'une carte.
		renvoie y_max
		"""
		y_max_temp = 0
		nb_ligne = 1
		for symbole in chaine:
			if symbole == "\n":
			# si le caractère est un retour à la ligne...
				nb_ligne += 1
		y_max_temp = nb_ligne
		return y_max_temp