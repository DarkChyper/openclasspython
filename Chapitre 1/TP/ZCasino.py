#!/usr/bin/Python3.4
# -*-coding:utf_8 -*

""" Premier TP OpenClassRoom
ZCasino
"""
import os
from ZCasino.settings import *

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
print infoBank

