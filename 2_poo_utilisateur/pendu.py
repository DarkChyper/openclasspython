#!/usr/bin/env python
# Coding: utf-8

#########################################################################################
# AUTEUR/AUTHOR : Fabien HUITELEC
#########################################################################################
# TP à réaliser dans le cadre d'une certification délivrée par OpenClassroom
# Pour en connaître l'intitulé exact, cliquer sur le lien ci-dessous :
#########################################################################################
# Practical work realized as part of a certificating course delivered by OpenClassroom
# To acknowledge the content of the said PW, please click the link below
# Comments, messages and var names are in French. Dear english speakers, forgive me
#########################################################################################
# http://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-un-bon-vieux-pendu
#########################################################################################

from fonctions  import *
from donnees    import *
from sys        import exit

def main():
    #Init
    score = avoir_score(adresse_fichier,connaitre_joueur())
    mots_joues = list()

    #Tant que le joueur souhaite jouer
    while True:
        #Si on n'est pas au premier tour
        if len(mots_joues) > 0 and not continuer_jeu():
            break #ToDo

        #Initialiser mot à jouer
        mots_joues = initialiser_mot(mots_joues)
        mot_courant = mots_joues[len(mots_joues) - 1]
        coups_restants = nb_coups_max
        continuer = True

        while continuer:
            #Afficher
            afficher_mot(mot_courant,coups_restants)

            #Jouer
            mot_courant = demander_lettre(mot_courant)
            coups_restants -= 1

            #Evaluer
            continuer = evaluer_jeu(mot_courant,coups_restants)

    #Bye
    exit(0)

if __name__ == "__main__":
    main()