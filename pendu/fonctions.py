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
	'hidden':mot,
	'founded':secret,
	'tantativ':"",
	'essai':"8"
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
		hidden += "_"
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
	if int(dico['essai']) == 0:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||   /|\    Il reste {} essai(s)".format(dico['essai'])
		print"  ||   / \ "
		print"_/||__"
	elif int(dico['essai']) == 1:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||   /|\    Il reste {} essai(s)".format(dico['essai'])
		print"  ||   /  "
		print"_/||__"
	elif int(dico['essai']) == 2:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||   /|\    Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"
	elif int(dico['essai']) == 3:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||   /|     Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"
	elif int(dico['essai']) == 4:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||    |     Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"
	elif int(dico['essai']) == 5:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||          Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"
	elif int(dico['essai']) == 6:
		print"    _______"
		print"   //   |"
		print"  ||    0     {}".format(dico['tantativ'])
		print"  ||          Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"
	elif int(dico['essai']) == 7:
		print"    _______"
		print"   //   |"
		print"  ||          {}".format(dico['tantativ'])
		print"  ||          Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"
	elif int(dico['essai']) == 8:
		print"    _______"
		print"   //   "
		print"  ||          {}".format(dico['tantativ'])
		print"  ||          Il reste {} essai(s)".format(dico['essai'])
		print"  ||     "
		print"_/||__"

	affHiddenWord(dico['founded'])


"""
	Affichage du mot avec les lettres trouvées.
	Affiche des "_" pour les lettres manquantes
	Prend en argument une chaine de caratères
"""
def affHiddenWord(mot):
	print("Mot à trouver :{}".format(mot))

"""
	Demande une lettre au joueur et la retourne
"""
def askLettre():
	while 1:
		lettre = raw_input("Quelle lettre voulez-vous tenter ? ")
		if len(lettre) > 1 or len(lettre) == 0:
			print("Merci de ne saisir qu'une seule lettre")
		elif lettre.lower() not in ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]:
			print("Merci de ne pas saisir autre chose qu'une lettre, sans accent.")
		else:
			return lettre.lower()

"""
	Prend en entrée la lettre choisi et le dictionnaire du jeu.
	Vérifie la présence de la lettre dans le mot à trouver.
	Mets à jour le mot à trouver, les lettres proposées et le nombres de tentatives restantes
	Renvoi un dico
"""
def verifLettre(lettre, **dico):
	# on ajoute la lettre aux lettres proposées
	dico['tantativ'] = dico['tantativ'] + lettre

	# on verifie la presence de la lettre dans le mot
	verif = False
	mot = ""
	for i in range(len(dico['hidden'])):
		if dico['hidden'][i] == lettre:
			mot += lettre
			verif = True
		elif dico['founded'][i] <> "_":
			mot += dico['founded'][i]
		else:
			 mot += "_"

	# on reffecte le mot calculé
	dico['founded'] = mot

	if verif == True:
		print ("La lettre \"{}\" fait bien partie du mot mystère !".format(lettre))
	else: 
		print ("{} ne fait pas partie du mot mystère, vous perdez un point.".format(lettre))
		dico['essai'] = str(int(dico['essai']) - 1)

	return dico

"""
"""
def svgScores(**scores):
	with open(defNameScores(), 'wb') as fichier :
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(scores)