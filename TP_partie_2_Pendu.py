#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# permet entre autre l'enregistrement d'objet directement récupérables dans un fichier
import pickle
# récupération des données nécessaires au jeu
from TP_partie_2_Donnees import *
#récupération des fonctions du jeu
from TP_partie_2_Fonctions import *
#choisi aléatoirement l'un des éléments d'une liste ou d'un tuple
from random import choice

#introduction
print("Bienvenu, préparez vous à être pendu!")
print("De façon à préparer votre tombe...")
name = input("Quel est votre nom? ")

if len(name) == 0:
    name = "John Doe"
else:
    name = name.capitalize()

#lecture du fichier de scores et établissement du lien avec le nom de joueur
try:
    with open("scores", "rb") as Scores:
        try:
            mon_depickler = pickle.Unpickler(Scores)
            tabscores = mon_depickler.load()
        except:
            tabscores = {}
        finally:
            tabscores[name] = tabscores.get(name, 0)
except:
    tabscores = {}
    tabscores[name] = tabscores.get(name, 0)

#intermède :p
print ("ok", name, ", on y va!")
print ("Pour le moment vous avez cumulé :", tabscores[name], "point(s)!")

######################début du jeu#################################

#appel de l'initialisation.
coups_restants, mot, a_decouvrir, cache, affiche, lettres_util = initialisation()

#main
while reponse != "N":
    
    points = main(coups_restants, mot, a_decouvrir, cache, affiche, lettres_util)
    tabscores[name] += points
    
    while len(reponse) != 1:
        reponse = input("Voulez-vous refaire une partie? O/N ")
        reponse = reponse.upper()

#fin
try:
    with open("scores", "wb") as Scores:
        mon_pickler = pickle.Pickler(Scores)
        mon_pickler.dump(tabscores)
except:
    print("Erreur lors de la sauvegarde des scores!")
