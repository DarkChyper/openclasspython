#!/usr/bin/python3.4
# -*-coding:utf_8 -*

""" Test des try et except complets """
print "Veuillez entrer un numérateur puis un denompinateur"
numerateur = raw_input("Numérateur ? ")
denominateur = raw_input("Dénominateur ? ")
try:
	resultat = numerateur / denominateur
except ZeroDivisionError:
	print "Division par zéro impossible"
except NameError:
	print "vous n'avez pas définit l'un des opérandes"
except TypeError:
	print "Une division ne se fait qu'avec des nombre"
	print "numérateur : ",numerateur
	print "dénominateur : ",denominateur 
print numerateur,"/",denominateur,"=",resultat
