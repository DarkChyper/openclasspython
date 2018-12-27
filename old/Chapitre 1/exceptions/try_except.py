#!/usr/bin/python3.4
# -*-coding:utf_8 -*

""" Test des try et except complets """
print "Veuillez entrer un numérateur puis un denompinateur"
resultat = None
numerateur = raw_input("Numérateur ? ")
denominateur = raw_input("Dénominateur ? ")
try:
	resultat = float(numerateur) / float(denominateur)
	print "Résultat :",resultat
except ZeroDivisionError:
	print "Division par zéro impossible"
except NameError:
	print "vous n'avez pas définit l'un des opérandes"
except TypeError:
	print "Une division ne se fait qu'avec des nombres"
	print "numérateur : ",numerateur
	print "dénominateur : ",denominateur 

