#!/usr/python3.4
# -*-coding:utf_8 -*

from random import randrange

"""
	Definition des données utiles pour le jeu de pendu.py
"""
def affRegles():
	print("\n==============")
	print("Règles du jeu:")
	print("     _ à chaque mot, le joueur à 8 tentatives pour trouver")
	print("       les lettres qui le compose")
	print("     _ le nombre de point est le nombre de tentative(s) restante(s)")
	print("     _ à chaque mot vous cululez des points")
	print("     _ ATTENTION si le nombre de tentative passe à 0")
	print("       votre score revient à 0!!!")
	print("==============\n")
	
def defNameScores():
	fichier_des_scores = "scores"
	return fichier_des_scores


"""
	Contient les mots de 8 car max à trouver
	retourne 1 mot à trouver 
"""
def selectMot():
	motWoasar = {
		0:"etat",
		1:"violent",
		2:"doute",
		3:"quantite",
		4:"individu",
		5:"arme",
		6:"fusils",
		7:"coup",
		8:"obtenir",
		9:"femme",
		10:"maniere",
		11:"famine",
		12:"sommeil",
		13:"long",
		14:"songe",
		15:"dos",
		16:"docteur"
	} 
	return motWoasar[randrange(16)]

