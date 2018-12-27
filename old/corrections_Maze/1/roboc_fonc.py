#!/usr/bin/python3.4
# -*- coding: utf8 -*-
from os import listdir
from re import findall

def intro():
    """
    Pour le moment ne sert pas à grand chose mais laisse la possibilité d'ajouter des choses au lancement
    """
    print("Bienvenu sur Roboc!")

def choixcarte(svgpartie):
    """
    affiche la liste de toutes les cartes diponibles dans le dossier
    charge dans l'objet de sauvegarde la carte demandée
    modules nécessaires os; re
    """
    lstcartes = listdir("cartes") #permet de récupérer tous les noms de fichier/dossier dans un dossier, retour est une liste
    i = 1
    for crt in lstcartes:
        crtname = findall('^[a-zA-Z0-9 _-]+', crt) #on extrait le nom de la carte sans l'extension
        print("{} - {}".format(i, crtname[0]))
        i += 1
        
    choix = input("Quelle carte voulez vous jouer? ")
    
    svgpartie.carte = lstcartes[(int(choix) - 1)] #on charge le nom de la carte jouée dans la sauvegarde
    
    return svgpartie

def affichcarte_init(svgpartie):
    """
    Premier affichage de la carte.
    Dans le même temps on récupère les dimensions de la carte et la position initiale de X.
    """
    path = "cartes/" + svgpartie.carte
    Lline = 0
    nbrline = 0
    hX = 0
    lX = 0
    
    with open(path, "r") as carte:
        for line in carte:
            svgpartie.plan.append(line)
            if nbrline == 0:
                Lline = len(line) - 1
                
            if "X" in line:
                svgpartie.posX.append(nbrline)
                svgpartie.posX.append(line.index('X'))
                
            print(line, end="")
            nbrline += 1
        print("")
    
    svgpartie.Nbrligne = nbrline
    svgpartie.Longueurligne = Lline
    
    return svgpartie

def affichecarte(svgpartie):
    """
    Cette fonction gère le réaffichage de la carte après chaque demande de mouvement
    """
    path = "cartes/" + svgpartie.carte
    nbrline = 0
    
    for line in svgpartie.plan:
        if 'X' in line: #on efface X de la carte
            line = line.replace('X', ' ')
            
        if nbrline == svgpartie.posX[0]: #on place le nouveau X
            tempbefore = line[:svgpartie.posX[1]]
            tempafter = line[svgpartie.posX[1]+1:]
            line = tempbefore + "X" + tempafter

        print(line, end="")
        nbrline += 1
    print("")
        
    return

def mouvement(svgpartie, mvt):
    """
    Cette fonction gère la vérification de la nouvelle position de X demandée par l'utilisateur
    Et la transmission de cette nouvelle position dans la svg si besoin
    """
    
    tempposX = list(svgpartie.posX)
    
    if mvt[0].upper() == "N":
        tempposX[0] -= 1
    elif mvt[0].upper() == "S":
        tempposX[0] += 1
    elif mvt[0].upper() == "E":
        tempposX[1] += 1
    elif mvt[0].upper() == "O":
        tempposX[1] -= 1

    valide = svgpartie.checkpos(tempposX)

    if valide == True:
        path = "cartes/" + svgpartie.carte
        nbrline = 0
        
        for line in svgpartie.plan:
            if nbrline == tempposX[0]:
                if line[tempposX[1]] == "O":
                    print("Ce déplacement est impossible !")
                elif line[tempposX[1]] == "U":
                    svgpartie.victoire = True
                else:
                    svgpartie.posX = list(tempposX)
            nbrline += 1
                
    return svgpartie

def mouvementlong(svgpartie, mvt):
    longueur = mvt[1:]
    tempposX = list(svgpartie.posX)
    
    try:
        longueur = int(longueur)
    except:
        print("longueur de déplacement invalide!")
        return svgpartie
        
    while longueur > 0:
        if mvt[0].upper() == "N":
            tempposX[0] -= 1
        elif mvt[0].upper() == "S":
            tempposX[0] += 1
        elif mvt[0].upper() == "E":
            tempposX[1] += 1
        elif mvt[0].upper() == "O":
            tempposX[1] -= 1

        valide = svgpartie.checkpos(tempposX)

        if valide == True:
            path = "cartes/" + svgpartie.carte
            nbrline = 0
        
            for line in svgpartie.plan:
                if nbrline == tempposX[0]:
                    if line[tempposX[1]] == "O":
                        print("Ce déplacement est impossible !")
                        return svgpartie
                    elif line[tempposX[1]] == "U":
                        svgpartie.victoire = True
                        svgpartie.posX = list(tempposX)
                        return svgpartie
                nbrline += 1
        else:
            return svgpartie
        longueur -= 1
        
    svgpartie.posX = list(tempposX)          
    return svgpartie

def aide():
    """
    rappelle les commandes du jeu
    """
    print("le déplacement ce fait via la direction suivie d'un chiffre indiquant le nombre de cases à parcourir.")
    print("N indique le haut de la carte")
    print("S le bas")
    print("O la gauche")
    print("E la droite")
    print("QUIT permet de quitter la partie")
    print("HELP réaffiche ce paragraphe\n")
    
