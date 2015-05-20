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
    joueur_courant = connaitre_joueur()
    score = avoir_score(adresse_fichier,joueur_courant)
    mots_joues = list()

    #Tant que le joueur souhaite jouer
    while True:
        #Si on n'est pas au premier tour
        if len(mots_joues) > 0 and not continuer_jeu():
            break

        #Initialiser mot à jouer

        # On cherche un mot qui n'a pas déjà été joué
        mots_joues = initialiser_mot(mots_joues)
        # On récupère le dernier mot trouvé
        nouveau_mot = mots_joues[len(mots_joues) - 1]
        print(nouveau_mot)
        # On met ce mot dans le bon format
        mot_courant = trans_mot_liste(nouveau_mot)
        # Autre
        coups_restants = nb_coups_max
        continuer = True

        while continuer:
            #Afficher
            afficher_mot(mot_courant,coups_restants)

            #Jouet et évaluer
            continuer,mot_courant,coups_restants = evaluer_jeu(mot_courant,coups_restants)

    #Bye
    score = enregistrer_score(adresse_fichier, joueur_courant, coups_restants)
    print("Votre score est de",score, "\nÀ bientôt !")
    exit(0)

if __name__ == "__main__":
    main()