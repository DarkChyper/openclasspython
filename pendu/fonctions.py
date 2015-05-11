#!/usr/python3.4
# -*-coding:utf_8 -*
"""
	Définition des fonctions utilisées dans le jeu de pendu pendu.py
"""

from donnee import *
from random import randrange
import pickle


"""
	Demande du pseudonyme au joueur 
	et retourne si celui-ci est non nul ET plus petit que 20 caratères
"""
def askName():
	while 1:
		try:
			pseudo = raw_input("Quel est votre nom/Pseudo ? ")
			assert pseudo <> "" and len(pseudo) < 20 
		except AssertionError:
			print("Votre pseudo ne peut être vide et doit faire moins de 20 caractères")
		else:
			return pseudo

"""
	Vérifie la présence du fichier des scores (scores)
	Vérifie, le cas échéant, la présence du pseudonyme dans le dictionnaire inclus
	Retourne un dictionnaire contenant au moins le couple pseudo:valeur
	Prend en argument le pseudo
"""
def initScores(pseudo):
	scores = dict()
	#tentative d'ouverture du fichier des scores
	try:
		with open(defNameScores(), 'rb') as fichier :
			lesScoresBrut = pickle.Unpickler(fichier)
			scores = pickle.load(lesScoresBrut)
	
	except IOError:
		print("New Challenger !!")

	scores[pseudo] = scores.get(pseudo,0) 

	return scores

"""
	affiche le nombre de point du joueur
"""
def affPlayerScores(scores, pseudo):
	print ("{} vous avez actuellement {} point(s) ! ".format(pseudo, scores[pseudo]))

"""
	Initialise un mot
	Ne prend pas d'argument 
	Retour un dictionnaire contenant :
		- une chaine hidden
		- une chaine founded
		- une chaine tantativ
		- une nombre essai
"""
def initWord():
	mot = selectMot() # on prend un mot au hasard
	secret = chiffreMot(mot) # on cacche le mot pour le joueur
	dico = {
	hidden:mot,
	founded:secret,
	tentativ:""
	essai:8
	}
	return dico

"""
	Cache le mot à trouver sous forme de "_"
	Prend en argument le mot à trouver
	Renvoi la chaine de "_"
"""
def chiffreMot(mot):
	hidden = ""
	for i in range(len(mot)):
		hidden += hiden + "_"
	return hidden

"""
	affichage de l'état du pendu
	Prend en paramètre un dictionnaire contenant :
		_ le mot à découvrir (hidden()))
		_ les lettres découvertes (founded()))
		_ les lettres déjà proposées (tantativ)
		_ le nombre d'essai restants (essai)
"""
def affEtatPendu(**dico):
	if dico[essai] == 0:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||   /|\    Il reste {} essai(s)".format(dico[essai])
		print"  ||   / \ "
		print"_/||__"
	elif dico[essai] == 1:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||   /|\    Il reste {} essai(s)".format(dico[essai])
		print"  ||   /  "
		print"_/||__"
	elif dico[essai] == 2:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||   /|\    Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"
	elif dico[essai] == 3:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||   /|     Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"
	elif dico[essai] == 4:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||    |     Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"
	elif dico[essai] == 5:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||          Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"
	elif dico[essai] == 6:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico[lettres])
		print"  ||          Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"
	elif dico[essai] == 7:
		print"    _______"
		print"   //   |"
		print"  ||          {}".format(dico[lettres])
		print"  ||          Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"
	elif dico[essai] == 8:
		print"    _______"
		print"   //   "
		print"  ||          {}".format(dico[lettres])
		print"  ||          Il reste {} essai(s)".format(dico[essai])
		print"  ||     "
		print"_/||__"

	print affHiddenWord(dico[founded])


"""
	Affichage du mot avec les lettres trouvées.
	Affiche des "_" pour les lettres manquantes
	Prend en argument une chaine de caratères
"""
def affHiddenWord(mot):
	print mot