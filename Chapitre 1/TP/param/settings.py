#!/usr/bin/Python3.4
# -*-coding:utf_8 -*

def welcome ()
	# on demande le nom du joueur
	userName = raw_input("Comment vous appellez-vous ? ")

	# on demande au joueur le niveau de difficulte
	print("Merci de choisir votre niveau de difficulté, ",userName)
	print("1 Facile : Bank 100$ ",userName," 200$")
	print("2 Normal : Bank 200$ ",userName," 200$")
	print("3 Difficil : Bank 500$ ",userName," 100$")
	print("4 Ninja : Bank 1000$ ",userName," 50$")
	choixFait = None
	while choixFait == None:
		choix = raw_input("1,2,3 ou 4 ? ")
		try:
			choixDifficulte = int(choix)
			assert choixDifficulte < 1 or choixDifficulte > 4
		except TypeError:
			print("Merci de choisir 1, 2 4 ou 4 !")
		except AssertionError:
			print("Le choix ne peut pas être en dessous de 1 ou au dessus de 4")
		else:
			choixFait = True

	# on attribue l'argent en fonction de la difficulte
	difficulte(choixdifficulte)

# choix de la difficulte
def difficulte(diff=2)
	if diff==1:
		coffreBank=100
		coffreUser=200
	if diff==2:
		coffreBank=200
		coffreUser=200
	if diff==3:
		coffreBank=500
		coffreUser=100
	if diff==4:
		coffreBank=1000
		coffreUser=50

# affichage de l'etat des "coffres fort"
def bankInfo()
	print(userName,": ",coffreUser,"$ || Bank : ",coffreBank"$")
