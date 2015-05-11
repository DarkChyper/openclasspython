#!/usr/python3.4
# -*-coding:utf_8 -*

import * from donnees
import pickle
"""
	Définition des fonctions utilisées dans le jeu de pendu pendu.py
"""

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
"""
def initScores(pseudo):
	scores = dict()
	#tentative d'ouverture du fichier des scores
	try:
		with open(donnees.defNameScores(), 'rb') as fichier :
			lesScoresBrut = pickle.Unpickler(fichier)
			scores = pickle.load(lesScoresBrut)
	
	except IOError:
		print("New Challenger !!")

	scores[pseudo] = scores.get(pseudo,0) 

	return scores
