largeur = 79


def intro():
	# on présente juste le jeu, les règles...   
	print('-' * largeur)
	print('-' * largeur)
	print('\n')
	print("ROBOC\n".center(largeur))
	print('-' * largeur)
	print('-' * largeur)
	print("BUT DU JEU : sortir vivant de ces foutus labyrinthes !")
	print('-' * largeur)
	print("""
COMMENT ON JOUE ?
- vous controllez un robot symbolisé par le signe'X'.
- les symboles 'O' représentent les murs (vous ne pouvez passer au travers)
- les symboles '.' représentent des portes (vous pouvez les traverser)
- rejoignez le symbole 'U' qui représente la sortie pour gagner.

CONTROLES :
- entrez 'N' pour demander au robot de se déplacer d'une case vers le Nord.
- entrez 'E' pour demander au robot de se déplacer d'une case vers l' Est.
- entrez 'S' pour demander au robot de se déplacer d'une case vers le Sud.
- entrez 'O' pour demander au robot de se déplacer d'une case vers l' Ouest.
(ajoutez un nombre à la suite de votre direction pour aller plus vite.)

POUR SAUVEGARDER ET QUITTER : entrez 'Q'.
	""")
	print('-' * largeur)
	print('-' * largeur)


def next_coordonates(move_orient):
	"""
	fonction permettant de calculer les prochaines coordonnées de Roboc.
	renvoie roboc_position => (x, y)
	"""
	roboc_next_position = roboc_position
	next_x, next_y = roboc_next_position

	if move_orient == 'N':
		next_y -= 1
	elif move_orient == 'S':
		next_y += 1
	elif move_orient == 'E':
		next_x += 1
	elif move_orient == "O":
		next_x -= 1
	
	roboc_next_position = (next_x, next_y)
	return roboc_next_position


def is_good_move(roboc_next_position):
	"""
	Fonction permettant de savoir si les prochaines coordonnées de Roboc
	sont valables, CAD, si il n'y a pas de mur.

	renvoie True (si la position est valide), sinon False
	"""
	good_next_position = False
	# on cherche dans le labyrinthe ce qui se trouve à l'endroit où
	# est sensé se retrouver Roboc.
	symbol_in_place = labyrinthe[roboc_next_position]
	if symbol_in_place in (' ', '.', 'U'):
		good_next_position = True
	return good_next_position


def choose_direction():
	"""
	fonction qui permet de :
	- demander à l'utilisateur d'entrer un déplacement
	- de valider l'entrée de l'utilisateur (sinon, entre un nouveau déplacement)
	- de renvoyer le sens et la distance d'un déplacement
	"""
	good_entry = False
	error_msg = "Utilisiez la forme 'S3' pour vous déplacer de 3 cases vers le Sud par exemple..."
	while good_entry == False:
		move_orient = ''                # le sens du déplacement
		move_dist = 0                   # la distance du déplacement
		move_request = input('> ').upper()
		if len(move_request) == 0:
			print("Vous n'êtes pas près de sortir...")
			print(error_msg)
			continue
		else:
			pass

		if move_request[0] in ('N', 'S', 'E','O'):
			move_orient = move_request[0]
			if len(move_request) == 1:
				move_dist = 1
				good_entry = True
			elif len(move_request) == 2:
				try:                    # si ça renvoie une erreur... 
					move_dist = int(move_request[1])  
				except:                 # ce n'est pas un nombre.
					print(error_msg)
					continue
				if int(move_request[1]) in range(1,10):
					move_dist = int(move_request[1])
					good_entry = True
				else:
					print(error_msg)
					continue
			else:
				print(error_msg)
				continue
		elif move_request[0] == 'Q':
			print("Ce labyrinthe à eu raison de vous ?")
			print("Je suis sûr que vous trouverez la sortie la prochaine fois.")
			print("A bientôt")
			exit()                      # on quitte le jeu
		else:
			print(error_msg)
			continue    
	return move_orient, move_dist


def next_coordonates(move_orient, roboc_position):
	"""
	fonction permettant de calculer les prochaines coordonnées de Roboc
	renvoie roboc_position => (x, y)
	"""
	roboc_next_position = roboc_position
	next_x, next_y = roboc_next_position

	if move_orient == 'N':
		next_y -= 1
	elif move_orient == 'S':
		next_y += 1
	elif move_orient == 'E':
		next_x += 1
	elif move_orient == "O":
		next_x -= 1
	roboc_next_position = (next_x, next_y)
	return roboc_next_position


def is_good_move(roboc_next_position, labyrinthe):
	"""
	Fonction permettant de savoir si les prochaines coordonnées de Roboc
	sont valables, CAD, si il n'y a pas de mur.
	renvoie True (si la position est valide), sinon False
	"""
	good_next_position = False
	# on cherche dans le labyrinthe ce qui se trouve à l'endroit où
	# est sensé se retrouver Roboc.
	try:
		symbol_in_place = labyrinthe[roboc_next_position]
		if symbol_in_place in (' ', '.', 'U'):
			good_next_position = True
	except:
		pass
	return good_next_position


def txt_to_dic():
	"""
	pour convertir une chaine de caractères en un dictionnaire de la forme :
	labyrinthe = {(0,0):'O', (1,0):'X', ..... (8,7):"U"}
	"""
	txt = "OOOOOOOOOO\nO O    O O\nO . OO   O"
	labyrinthe = {}
	coor_x = 0                          # correspond au numéro du caratère
	coor_y = 0                          # correspond au numéro de la ligne
	for symbole in txt:
		if symbole == "\n":             # si le caractère est un retour à la ligne...
			coor_y += 1                 # on incrémente le numéro de ligne
			coor_x = 0                  # on repart au premier caractère de la ligne.
		print("labyrinthe[{}, {}] = {}".format(coor_x, coor_y, symbole))
		labyrinthe[coor_x, coor_y] = symbole
		coor_x += 1


def choose_map(nombre_de_cartes_totales):
	"""
	fonction permettant de choisir une carte.
	on vérifie que le numéro est valbale.
	renvoie le numéro de l'index dans l'index "cartes[]"
	"""
	good_entry = False
	nombre_de_cartes_totales = int(nombre_de_cartes_totales)
	error_msg = "Merci de choisir une carte de 1 à {}".format(
		nombre_de_cartes_totales)
	while good_entry == False:
		map_request = input('> ')
		try:                            # si ça renvoie une erreur... 
			map_request = int(map_request)  
		except:                         # ce n'est pas un nombre.
			if map_request == 'Q' or map_request == 'q':
				print("A bientôt.")
				exit()                  # on quitte le jeu
			print(error_msg)
			continue
		if map_request in range(1, nombre_de_cartes_totales + 1):
			good_entry = True
		else:
			print(error_msg)
			continue
	map_request -= 1                    # On enlève 1 pour l'index
	return map_request


def choose_continue_or_redo():
	"""
	Fonction permettant de demander au joueur si il souhaite
	Continuer la partie enregistrée sur une carte ou Recommencer
	renvoie 'C' ou 'R'
	"""
	good_entry = False
	error_msg = """
		Merci d'entrer 'C' si vous souhaitez Continuer la partie en cours
		ou 'R' pour recommencer la carte.
		"""
	while good_entry == False:
		map_option = input('> ')
		try:							# si ça renvoie une erreur... 
			map_option = str(map_option).upper()  
		except:							# ce n'est pas un nombre.
			print(error_msg)
			continue
		if map_option in ['C', 'R']:
			pass
		else:
			print(error_msg)
			continue	
		good_entry = True
		
	return map_option
