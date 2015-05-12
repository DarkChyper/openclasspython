#choisi aléatoirement l'un des éléments d'une liste ou d'un tuple
from random import choice
# récupération des données nécessaires au jeu
from TP_partie_2_Donnees import *

def initialisation():
    """fonction d'initialisation des variables du programmes.
    Le tuple retourné comprend toutes les information pour la suite.
    le tuple retourné est le suivant : coups_restants(int), mot(str), a_decouvrir(liste), cache(liste), affiche(str), lettres_util(liste)"""
    coups_restants = coups_max
    mot = choice(mots)
    a_decouvrir = []
    cache = []
    lettres_util = []

    for lettre in mot:
        a_decouvrir.append(lettre)
        cache.append("*")
    
    affiche = delimiter.join(cache)
    pendaison(coups_restants)
    print("")
    print("Voici le mot à découvrir :", affiche)
    print("")
        
    return coups_restants, mot, a_decouvrir, cache, affiche, lettres_util

def main(coups_restants, mot, a_decouvrir, cache, affiche, lettres_util):
    while coups_restants > 0:
        print("Il vous reste", coups_restants, "coups")
        
        Lettre = None
        while Lettre == None:
            lettre = input("A quelle lettre pensez vous? ")
            try:
                assert len(lettre) == 1
                Lettre = lettre.upper()
            except:
                pass
    
        if Lettre in lettres_util:
            print("Déjà essayé!\n")
            continue
            
        elif Lettre not in lettres_util and Lettre in a_decouvrir:
            lettres_util.append(Lettre)
            for i in range(len(mot)):
                if a_decouvrir[i] == Lettre:
                    cache[i] = Lettre

            affiche = delimiter.join(cache)
            print("")
            print("Voici le mot à découvrir :", affiche)
            print("")
            if "*" not in affiche:
                points = coups_restants
                print("félicitations!\nVous gagnez", points, "points!")
                return points

        else:
            lettres_util.append(lettre.upper())
            coups_restants = coups_restants - 1
            pendaison(coups_restants)
            print("")
            print("Voici le mot à découvrir :", affiche)
            print("")

    print("c'est fini pour vous!")
    points = coups_restants
    return points
