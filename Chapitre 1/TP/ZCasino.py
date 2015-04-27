#!/usr/bin/Python3.4
# -*-coding:utf_8 -*

""" Premier TP OpenClassRoom
ZCasino
"""
import os
from ZCasino import *

"""Main"""
print "==========================="
print "Bienvenue au Dark ZCasino !"
print "==========================="
print "Le but est de faire sauter la banque au jeu de la roulette"

#choix des settings de l'utilisateur
#on demande le nom du joueur
userName = raw_input("Comment vous appellez-vous ? ")

# on demande au joueur le niveau de difficulte
print "Merci de choisir votre niveau de difficulté, ",userName
print "1 Facile : Bank 100$ ",userName," 200$"
print "2 Normal : Bank 200$ ",userName," 200$"
print "3 Difficil : Bank 500$ ",userName," 100$"
print "4 Ninja : Bank 1000$ ",userName," 50$"
choixFait = None
while choixFait == None:
	choix = raw_input("1,2,3 ou 4 ? ")
	try:
		choixDifficulte = int(choix)
		assert choixDifficulte >= 1 and choixDifficulte <= 4
	except ValueError:
		print "Merci de ne pas choisir autre chose qu'un nombre"
	except TypeError:
		print "Merci de choisir 1, 2 4 ou 4 !"
	except AssertionError:
		print "Le choix ne peut pas être en dessous de 1 ou au dessus de 4"
	else:
		choixFait = True
infoBank = dict()
infoBank = difficulte(choixDifficulte)

"""
Boucle qui fait continuer la partie après x mise(s) tant que : 
	_ le joueur ou la banque n'est pas à < 0
	_ le joueur ne décide pas de terminer la partie
"""
nouveauParis = True
while nouveauParis:
	#on initialise le lancé
	table = dict() #contiendra les mises sur les différentes cases
	infoBank['lancer'] = infoBank[User] # le joueur ne peut miser que ce qu'il possède
	while 1:
		tableauMises()#affichage des mises et de l'argent que l'user peut encore miser
		print "Laisser vide si vous voulez lancer la bille !"
		case = raw_input("Sur quelle case misez-vous ?")
		if case == "":
			break
		try:
			case = int(case)
			assert case >= 0 or case <= 49
		except ValueError:
			print "Merci de choisir une case entre 0 et 49."
		except AssertionError:
			print "Merci de choisir une case entre 0 et 49."
		else:
			while 1:
				mise = raw_input("Combien misez-vous ?")
				try:
					mise = int(mise)
					assert mise <= bankInfo[lancer] or mise >= 0
				except AssertionError:
					print "Vous ne pouvez pas miser plus de "bankInfo[lancer]"$ ou une mise négative !"
				except ValueError:
					print "Mise incorrecte."
				else:
					
		
	
	choix = False
	while choix == False:
		try:		
			again = raw_input("Une nouvelle mise ? O/n ")
			assert again == "o" or again =="n"
		except AssertionError:
			print "Merci de choisir o pour oui ou n pour non."
		else:
			if again == "n":
				choix = True
				nouveauParis = False

		



