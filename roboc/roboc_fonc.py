from os import listdir
from re import findall

def intro():
    print("Bienvenu sur Roboc!")

def choixcarte(svgpartie):
    """
    affiche la lsite de toutes les cartes diponibles dans le dossier
    modules nécessaires os; re
    """
    lstcartes = listdir("cartes") #permet de récupérer tous les noms de fichier/dossier dans un dossier, retour est une liste
    i = 1
    for crt in lstcartes:
        crtname = findall('^[a-zA-Z0-9]+', crt) #on extrait le nom de la carte sans l'extension
        print("{} - {}".format(i, crtname[0]))
        i += 1
        
    choix = input("Quelle carte voulez vous jouer? ")
    
    svgpartie.carte = lstcartes[(int(choix) - 1)] #on charge le nom de la carte jouée dans la sauvegarde
    
    return svgpartie

def affichcarte(svgpartie):
    path = "cartes/" + svgpartie.carte
    Lline = 0
    Nbrline = 0
    hX = 0
    lX = 0
    
    with open(path, "r") as carte:
        for line in carte:
            if Nbrline == 0:
                Lline = len(line)
                
            if "X" in line:
                
            print(line, end = "")
            Nbrline += 1
        print("")
    
    svgpartie.Nbrline = Nbrline
    svgpartie.Lline = Lline
    
    return svgpartie
