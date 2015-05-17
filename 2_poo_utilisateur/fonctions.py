#!/usr/bin/env python
# Coding: utf-8

#########################################################################################
# AUTEUR/AUTHOR : Fabien HUITELEC
#########################################################################################
# Bibliothèque de fonctions utilisées par pendu.py
# Pour plus d'informations, lire la description de pendu.py
#########################################################################################
# Function library used by pendu.py
# For more informations, please read pendu.py's description
#########################################################################################

from pickle import Pickler, Unpickler

score = dict()

def avoir_score(adresse_fichier_score, joueur):
    """Ouvre le fichier des scores, s'il existe, selon le joueur, le score est chargé et envoyé,
    sinon on renvoie 0. Se charge également de charger entièrement le fichier des scores"""
    global score

    try:
        with open(adresse_fichier_score, 'rb') as fichier_score:
            #Lecture du fichier
            unpick = Unpickler(fichier_score)
            score = unpick.load()

            return score.get(joueur, 0)
    except IOError:
        print("erreur")
        return 0
    except EOFError:
        return 0

def connaitre_joueur():
    """Demande le nom du joueur"""

def enregistrer_score(adresse_fichier_score, joueur, nouveau_score):
    """Ouvre le fichier des scores, s'il existe, selon le joueur, le score est chargé et envoyé,
    sinon on renvoie 0. Se charge également de charger entièrement le fichier des scores"""
    global score

    try:
        with open(adresse_fichier_score, 'wb') as fichier_score:
            #Définition du score
            score[joueur] = score.get(joueur, 0) + nouveau_score

            #Enregistrement du socre
            pick = Pickler(fichier_score)
            score = pick.dump(score)
    except IOError:
        print("Erreur lors de l'enregistrement du fichier")

def afficher_mot(mot,coups_restants):
    """En fonction du dictionnaire du mot, affiche un tiret ou la lettre
    trouvée par l'utilisateur"""
    mot_affiche = ""

    for i,lettre in enumerate(mot[0]):
        if mot[1][i] == True:
            mot_affiche += lettre
        else:
            mot_affiche += "_"

    print("Mot:", mot_affiche)
    print("Coups restants:", coups_restants)

#ToDo
def initialiser_mot(mots_joues):
    """Va chercher le mot à trouver dans la liste et le retourne initialisé"""
    return [ [["m","o","t"],[True,False,True]] ] #Exemple de mot

#ToDo
def demander_lettre(mot_courant):
    """Demande une lettre au joueur et renvoie le mot correctement valorisé"""
    return mot_courant

#ToDo
def evaluer_jeu(mot_courant,coups_restants):
    """Évalue l'état du jeu et renvoie un booléen (continuer ou non)"""
    if coups_restants < 1:
        return False

    return True

#ToDo
def continuer_jeu():
    """Demande au joueur s'il souhaite continuer ou non"""
    return False