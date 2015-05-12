#!/usr/bin/python3.4
# -*- coding: utf8 -*-

# permet entre autre l'enregistrement d'objet directement récupérables dans un fichier
import pickle
# récupération des données nécessaires au jeu
from TP_partie_2_Donnees import *
#choisi aléatoirement l'un des éléments d'une liste ou d'un tuple
from random import choice

#introduction
print("Bienvenu, préparez vous à être pendu!")
print("De façon à préparer votre tombe...")
name = input("Quel est votre nom? ")

#lecture du fichier de scores et établissement du lien avec le nom de joueur
try:
    with open("scores", "rb") as Scores:
        try:
            tabscores = pickle.Unpickler(Scores)
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

#début du jeu

#initialisation

mot = choice(mots)
