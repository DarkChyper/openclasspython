#!/usr/bin/env python
# Coding: utf-8

#########################################################################################
# AUTEUR/AUTHOR : Fabien HUITELEC
#########################################################################################
# Modèle de données utilisé par pendu.py
# Pour plus d'informations, lire la description de pendu.py
#########################################################################################
# Data model used by pendu.py
# For more informations, please read pendu.py's description
#########################################################################################

nb_coups_max = 10

adresse_fichier = "F:/hubiC/Linux/python_mooc/python_mooc_open_classroom/openclasspython/2_poo_utilisateur/scores"

mots = [
        "armoire",
        "boucle",
        "buisson",
        "bureau",
        "chaise",
        "carton",
        "couteau",
        "fichier",
        "garage",
        "glace",
        "journal",
        "kiwi",
        "lampe",
        "liste",
        "montagne",
        "remise",
        "sandale",
        "taxi",
        "vampire",
        "volant",
        ]

# Contient 11 états du pendu,
# l'indice 0 étant le pendu vide et l'indice 10 le pendu entier
pendu_ascii =   (
                "\n\n\n\n\n\n\n",
                "\n\n\n\n\n\n_____________\n",
                "\n |\n |\n |\n |\n |\n_|___________\n",
                "_____________\n |\n |\n |\n |\n |\n_|___________\n",
                "_____________\n | /\n |/\n |\n |\n |\n_|___________\n",
                "_____________\n | /       |\n |/\n |\n |\n |\n_|___________\n",
                "_____________\n | /       |\n |/        O\n |\n |\n |\n_|___________\n",
                "_____________\n | /       |\n |/        O\n |         |\n |\n |\n_|___________\n",
                "_____________\n | /       |\n |/        O\n |        -|-\n |\n |\n_|___________\n",
                "_____________\n | /       |\n |/        O\n |        -|-\n |         /\\\n |\n_|___________\nOn suffoque, non?",
                "_____________\n | /       |\n |/        O\n |        -|-\n |         /\\\n |\n_|____________\nTrop tard vous etes mort !\n",
                )