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

from pickle     import Pickler, Unpickler
from random     import randrange
from donnees    import *

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
    first = True

    while True:
        if first:
            a_afficher = "Quel est votre nom ? "
        else:
            a_afficher = "Entrez un nom de joueur non vide. Quel est votre nom ? "

        joueur = input(a_afficher)
        first = False

        # Checking null entries
        if len(joueur) != 0 and len(joueur.strip()) != 0:
            break

    return joueur

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
            pick.dump(score)
    except IOError:
        print("Erreur lors de l'enregistrement du fichier")

    return score[joueur]

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

def initialiser_mot(mots_joues):
    """Va chercher le mot à trouver dans la liste principale qui n'est pas dans la liste en paramètre.
    Si tous les mots de la liste principale ont déjà été joués, réinitialiser la liste"""
    # Init
    global mots
    cpt_mot = 0

    # On prend un mot une première fois au hasard
    mot_trouve = mots[randrange(len(mots))]

    # S'il n'y a aucun mot déjà joué, renvoyer directement la nouvelle liste
    if len(mots_joues) == 0:
        mots_joues.append(mot_trouve)
        return mots_joues

    # S'il a déjà été joué, en prendre un autre au hasard
    while mot_trouve in mots_joues:
        mot_trouve = mots[randrange(len(mots))]
        cpt_mot += 1

        # Si tous les mots ont été joué
        if cpt_mot >= len(mots):
            mots_joues = list()
            cpt = 0

    mots_joues.append(mot_trouve)
    return mots_joues

def trans_mot_liste(mot):
    lst = [list(),list()]

    for lettre in mot:
        lst[0].append(lettre)
        lst[1].append(False)

    return lst
    #return [ [["m","o","t"],[True,False,True]] ] #Exemple de mot

def demander_lettre():
    """Demande une lettre au joueur et renvoie le mot correctement valorisé"""
    while True:
        lettre = input("Lettre : ")
        if len(lettre) == 1 and not lettre.isdigit():
            break

    return lettre

def mot_trouve(mot):
    """Définit si un mot a été trouvé entièrement"""
    mot_trouve = True

    for lettre in mot[1]:
        if lettre == False:
            mot_trouve = False

    return mot_trouve

def set_mot(mot, lettre_trouve):
    start = 0

    for lettre in mot[0]:
        if lettre == lettre_trouve:
            i = mot[0].index(lettre, start)
            start = i + 1
            mot[1][i] = True

    return mot

def evaluer_jeu(mot_courant,coups_restants):
    """Évalue l'état du jeu et renvoie un booléen (continuer ou non)"""
    global pendu_ascii

    lettre = demander_lettre()

    if lettre not in mot_courant[0]:
        coups_restants -= 1
    else:
        mot_courant = set_mot(mot_courant, lettre)

    continuer = coups_restants >= 1 and not mot_trouve(mot_courant)

    if mot_trouve(mot_courant):
        print("Bravo !")
    else:
        print(pendu_ascii[10 - coups_restants])

    return continuer, mot_courant, coups_restants

def continuer_jeu():
    """Demande au joueur s'il souhaite continuer ou non"""
    while True:
        continuer = input("Souhaitez-vous continuer ? o/n ")
        if continuer.lower() == "n":
            return False
        elif continuer.lower() == "o":
            return True

    return False