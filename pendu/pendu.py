#!/usr/python3.4
# -*-coding:utf_8 -*

from donnee import *
from fonctions import *

""" pendu.py est un simple jeu de pendu en ligne de commande
	Le joueur renseigne son pseudo et essaye de trouver les mots
	proposés par l'ordinateur, lettre par lettre, en moins de 
	8 tentatives sinon il est "pendu" 
"""

""" Déclaration des variables
"""
# Initialisation du dictionnaire des scores
scores = dict()

""" Main
"""
print("Bienvenue dans le jeu de pendu.\n")

# On demande au joueur de renseigner son nom/pseudo
pseudo = askName()affEtatPendu(**dico)

# Vérification de la présence du fichier des scores 
# et de la présence du joueur ou non
scores = initScores(pseudo)

#boucle de sortie du jeu
while 1:
	affPlayerScores(scores, pseudo)
	dico = initWord()
	while 2: # tant que l'on ne sort pas de cette boucle
			 # on cherche le mot
		affEtatPendu(**dico) #affiche l'etat du pendu
		lettre = askLettre()
		dico = verifLettre(lettre,**dico)
		# on vérifie les conditions de sortie
		if dico[essai] == 0: # le joueur a utilisé ses 8 tentatives
			affEtatPendu(**dico)
			print("Vous avez perdu ! ")
			print("Le mot était \"{}\"."format(dico[hidden]))
			break # on sort du mot mais le joueur peut recommencer
		elif dico[hidden] == dico[founded]: # le joueur a trouvé le mot en moins de 8 tentatives
			print("Bravo {}, vous avez trouvé le mot \"{}\"".format(pseudo,dico[founded]))
			print("Vous gagnez {} points.".format(dico[essai]))
			print("Vous avez {} au total".format(dico[essai] + scores[pseudo]))
			dico[essai] = dico[essai] + scores[pseudo] # on prépare la sauvegarde du nouveau score
			break
	# on sort du mot
	# on enregistre le score même si c'est 0 point
	# on écrase l'ancien score
	scores[pseudo] = dico[essai]
	break