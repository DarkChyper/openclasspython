#!/usr/bin/Python3.4
# -*-coding:utf_8 -*
from random import randrange
from math import ceil

# choix de la difficulte
def difficulte(diff=2):
	infoBank = dict()
	if diff==1:
		infoBank['Bank']=100
		infoBank['User']=200
	if diff==2:
		infoBank['Bank']=200
		infoBank['User']=200
	if diff==3:
		infoBank['Bank']=500
		infoBank['User']=100
	if diff==4:
		infoBank['Bank']=1000
		infoBank['User']=50
	return infoBank

# initialisation de la table de jeu
def initTable():
	table = dict()
	for i in range(50):
		table['i'] = 0
	return table

# lancement de la roulette
def lancerDeRoulette():
	return randrange(50)

# affiche l'état des fonds de la banque, du joueur et de ses mises si il y en a
def afficheBank(infoBank,userName, tableDeJeu):
	#affichage de l'état des comptes
	print userName," :", infoBank[User],"    Bank : ",infoBank[Bank],"$"
	
	#affichage des mises si il y en a
	for i in range(50):
		if tableDeJeu[i] > 0:
			print "case ",i," : ",tableDeJeu[i],"$"
	
	if infoBank[user] > infoBank[lancer]:
		print "Reste ",	infoBank[lancer],"$"

# resolution d'un lancé de bille
def resolution(infoBank, bille, tableDeJeu, userName):
	gain = 0
	perte = 0
	# on resoud la case gagnante
	# si le joueur n'a pas parié sur cette case, elle est à 0
	# donc 0 * 3 = 0
	infoBank[lancer] = infoBank[lancer] + ( tableDeJeu[bille] * 3 )
	gain = gain + tableDeJeu[bille] * 2
	# la banque perd 2 fois la somme misée
	infoBank[Bank] = infoBank[Bank] - ( tableDeJeu[bille] * 2 )
	# et on met cette case à zéro pour éviter de compter la parité
	if tableDeJeu[bille] > 0:
		print "Bravo ",userName," vous avez le bon numéro !"
		print "vous gagnez ",tableDeJeu[bille] * 2,"$ !"
	tableDeJeu[bille] = 0

	# on résoud la parité
	for i in range(50):
		if infoBank[i] > 0:
			# si le joueur a la bonne parité
			if ( i % 2 == 0 and bille % 2 == 0) or (i % 2 == 1 and bille % 2 == 1):
				# les gains sont de 150% de la mise
				infoBank[lancer] = infoBank[lancer] + ceil(tableDeJeu[i] * 1.5)
				# la banque perd la moitié de la mise
				infoBank[Bank] = infoBank[Bank] - ceeil(tableDeJeu[i] * 0.5)

			# sinon il perd sa mise qui va à la banque
			else:
				infoBank[Bank] = infoBank[Bank] + tableDeJeu[i]
				perte = perte + tableDeJeu[i]
	# on met à jour les infos du joueur
	infoBank[User] = infobank[lancer]

	# affichage des résultats
	print "Total des gains : ",gain,"$"
	print "Total des pertes : ",perte,"$"
	
	afficheBank(infoBank, userName)
	
	# on retourne le dictionnaire recalculé
	return(infoBank)




