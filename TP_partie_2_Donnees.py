"""ce fichier contient les données nécessaires au fonctionnement du 
pendu"""

# la liste des mots disponibles
mots = ("ARMOIRE"
, "BANC"
, "BUREAU"
, "ANGLE"
, "CABINET"
, "CARREAU"
, "CHAISE"
, "CLASSE"
, "CLEF"
, "COIN"
)

coups_max = 10
delimiter = ""
reponse = ""

def pendaison(coups_restants):
    if coups_restants == 10:
        print("\n\n\n\n\n\n\n")
    elif coups_restants == 9:
        print("\n\n\n\n\n\n_____________\n")
    elif coups_restants == 8:
        print("\n |\n |\n |\n |\n |\n_|___________\n")
    elif coups_restants == 7:
        print("_____________\n |\n |\n |\n |\n |\n_|___________\n")
    elif coups_restants == 6:
        print("_____________\n | /\n |/\n |\n |\n |\n_|___________\n")
    elif coups_restants == 5:
        print("_____________\n | /       |\n |/\n |\n |\n |\n_|___________\n")
    elif coups_restants == 4:
        print("_____________\n | /       |\n |/        O\n |\n |\n |\n_|___________\n")
    elif coups_restants == 3:
        print("_____________\n | /       |\n |/        O\n |         |\n |\n |\n_|___________\n")
    elif coups_restants == 2:
        print("_____________\n | /       |\n |/        O\n |        -|-\n |\n |\n_|___________\n")
    elif coups_restants == 1:
        print("_____________\n | /       |\n |/        O\n |        -|-\n |         /\\\n |\n_|___________\nOn suffoque, non?")
    elif coups_restants == 0:
        print("_____________\n | /       |\n |/        O\n |        -|-\n |         /\\\n |\n_|____________\nTrop tard vous etes mort !\n")
