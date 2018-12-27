# -*-coding:Utf-8 -*

"""
Fichier principal du jeu Roboc.
Créé par Laurent Gaulhiac.
Pour OpenClassroom.

Exectutez-le avec Python pour jouer.
"""

# importation des modules nécéssaires
import os
import pickle

from fonctions import *
from labyrinthe import *
from carte import Carte

# présentation du jeu
intro()

# initialisation et début de la boucle principale
jouer = True
while jouer == True:

	# On charge les cartes existantes
	cartes = []
	for nom_fichier in os.listdir("cartes"):
		if nom_fichier.endswith(".txt"):
			chemin = os.path.join("cartes", nom_fichier)
			nom_carte = nom_fichier[:-4].lower()
			with open(chemin, "r") as fichier:
				contenu = fichier.read()
				fichier.close()
				# Création d'une carte, à compléter
			nom_carte = Carte(nom_carte, contenu)
			cartes.append(nom_carte)

	# pour l'enregistrement, on va créer une copie de cartes[] : cartes_saved[]
	# d'abord on essaie d'importer "cartes_saved" du fichier de sauvergarde
	if os.path.exists("fichier_de_sauvegarde"):
		# Si le fichier existe...
		fichier_sauvegarde = open("fichier_de_sauvegarde", "rb")
		mon_depickler = pickle.Unpickler(fichier_sauvegarde)
		# on récupère la variable cartes_saved
		cartes_saved = mon_depickler.load()
		fichier_sauvegarde.close()
		# Puis, pour toutes les cartes qui ont une partie en cours...
		for carte_s in cartes_saved:
			if carte_s.current == True:
				nom_carte_encours = carte_s.nom
				for i, carte in enumerate(cartes):
					if cartes[i].nom == nom_carte_encours:
						cartes[i] = carte_s
	else:
		# Si le fichier n'existe pas, on crée le fichier...
		cartes_saved = list(cartes)

	# On affiche les cartes existantes
	print("Entrez le numéro du labyrinthe que vous souhaitez faire ('Q' pour quitter):\n")
	for i, carte in enumerate(cartes):
		if carte.current == True:
			print("  {} - {} (partie sauvegardée disponible)".format(i + 1, carte.nom))
		else:
			print("  {} - {}".format(i + 1, carte.nom))

	# Le joueur choisi une carte
	selected_map = choose_map(len(cartes))
	# Si il y a une partie sauvegardée, sur la carte choisie
	if cartes[selected_map].current == True:
		print("Il existe une partie sauvegardée sur cette carte.")
		print("Souhaitez-vous Continuer la partie ou Recommencer ('C'/'R') ?")
		map_option = choose_continue_or_redo()
		if map_option == 'R':
			# on réinitialise le labyrinthe en cours par le labyrinthe initial.
			cartes[selected_map].map.labyrinthe = dict(cartes[selected_map].map.labyrinthe_initial)

	# on passe la carte selectionnée en tant que "carte en cours"
	cartes[selected_map].current = True

	# On affiche notre labyrinthe
	cartes[selected_map].map.display()
	# On réccupère la position actuelle de roboc
	roboc_position = cartes[selected_map].map.get_roboc_position()
	# On réccupère la position de la sortie
	exit_position = cartes[selected_map].map.get_exit_position()

	# boucle de déplacement
	while roboc_position != exit_position:
		# On demande au joueur de choisir un déplacement
		move_orient, move_dist = choose_direction()

		# Tant qu'il reste de la distance à parcourir dans une direction...
		while move_dist > 0:
			# on vérifie si la nouvelle position de Roboc est valable
			roboc_next_position = next_coordonates(move_orient, roboc_position)
			if is_good_move(roboc_next_position, cartes[selected_map].map.labyrinthe) == True:
				# on enregistre la nouvelle position de Roboc dans le labyrinthe
				cartes[selected_map].map.labyrinthe[(roboc_next_position)] = 'X'
				# on réccupère le symbole présent à l'ancienne position
				# de Roboc sur la carte initiale
				symbol_initial = cartes[selected_map].map.labyrinthe_initial[(roboc_position)]
				# si c'était Roboc lui-même...
				if symbol_initial == 'X':
					# On remplace la case par un espace vide 
					# pour ne pas qu'il y ai 2 Roboc.
					cartes[selected_map].map.labyrinthe[(roboc_position)] = ' '
				# sinon, on affiche n'importe quel symbol présent 
				# sur le labyrinthe initial
				else:
					cartes[selected_map].map.labyrinthe[(roboc_position)] = symbol_initial
				print('-' * largeur)
				# On affiche le labyrinthe mis à jour
				cartes[selected_map].map.display()
				# On réduit de 1 le nombre de déplacement demandé
				move_dist -= 1
				# on enregistre la nouvlle position de Roboc
				roboc_position = roboc_next_position
				# on vérifie si Roboc se trouve sur la sortie
				if roboc_position == exit_position:
					print('-' * largeur)
					print("BRAVO, vous en êtes sortis (presque) indemne !")
					print('-' * largeur)
					pass
				else:
					continue
			# si la nouvelle position n'est pas valide, on sort de la boucle
			else:
				if roboc_position == exit_position:
					break
				else:    
					move_dist = 0
					print('-' * largeur)
					print("Impossible d'aller plus loin")
					print('-' * largeur)
					cartes[selected_map].map.display()
					continue
		# ici on enregistre
		cartes_saved = cartes
		fichier_sauvegarde = open("fichier_de_sauvegarde", "wb")
		mon_pickler = pickle.Pickler(fichier_sauvegarde)
		mon_pickler.dump(cartes_saved)
		fichier_sauvegarde.close()
	# la carte est terminée, donc elle n'a plus de partie "en cours"
	cartes[selected_map].current = False

# Ici on re-choisi une carte