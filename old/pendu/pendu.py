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

# Initialisation du dictionnaire du mot
dico = dict()

""" Main
"""
print("Bienvenue dans le jeu du pendu.\n")
affRegles()

# On demande au joueur de renseigner son nom/pseudo
pseudo = askName()

# Vérification de la présence du fichier des scores 
# et de la présence du joueur ou non
scores = initScores(pseudo)

#boucle de sortie du jeu
nouveauMot = True
while nouveauMot:
	
	affPlayerScores(scores, pseudo)
	
	dico = initWord()
	while 2: # tant que l'on ne sort pas de cette boucle
			 # on cherche le mot
		
		affEtatPendu(**dico) #affiche l'etat du pendu
		
		lettre = askLettre()
		dico = verifLettre(lettre,**dico)

		print("\n\n\n\n")

		# on vérifie les conditions de sortie
		if int(dico['essai']) == 0: # le joueur a utilisé ses 8 tentatives

			affEtatPendu(**dico)

			print("Vous avez perdu ! ")
			print("Le mot était \"{}\".".format(dico['hidden']))

			break # on sort du mot mais le joueur peut recommencer

		elif dico['hidden'] == dico['founded']: # le joueur a trouvé le mot en moins de 8 tentatives

			print("Bravo {}, vous avez trouvé le mot \"{}\"".format(pseudo,dico['founded']))
			print("Vous gagnez {} points.".format(dico['essai']))

			calcul = int(dico['essai']) + int(scores[pseudo])

			print("Vous avez {} au total".format(str(calcul)))
			dico['essai'] = str(calcul) # on prépare la sauvegarde du nouveau score

			break

	# on sort du mot
	# on enregistre le score même si c'est 0 point
	# on écrase l'ancien score
	scores[pseudo] = dico['essai']
	print("Sauvegarde de votre score.")
	svgScores(**scores)

	while 3:
		try:		
			again = input("Un nouveau mot ? O/n ")
			assert again == "o" or again =="n"
		except AssertionError:
			print("Merci de choisir o pour oui ou n pour non.")
		else:
			if again == "n":
				print("Un prochain mot un autre jour !")
				
				nouveauMot = False 
		break

print("A bientôt !")
