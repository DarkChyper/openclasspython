#!/usr/bin/python3.4
# -*- coding: utf8 -*-

from random import randrange
from math import ceil

print("Bienvenu au Casino du Terminal!")
print("Please insert an ASCII art Striper!")

def testnombre(nbr):
    try:
        nbr = int(nbr)
    except ValueError:
        print('entrez un entier!')
        nbr = False
    finally:
        return nbr

ReserveJoueur = None
Suite = "o"

while ReserveJoueur == None:
        Temp = input("Combien de jetons voulez vous pour jouer? ")
        Temp = testnombre(Temp)
        if Temp != False:
            ReserveJoueur = Temp

while Suite != "n":
    Mise = None
    while Mise == None:
        Temp = input("Combien voulez vous miser? ")
        Temp = testnombre(Temp)
        if Temp != False:
            if Temp <= ReserveJoueur:
                Mise = Temp
                ReserveJoueur = ReserveJoueur - Mise
            else:
                print("Vous ne pouvez pas miser autant!")
    
    Pari = None
    while Pari == None:
        Temp = input("Sur quel chiffre (entre 0 et 49)? ")
        Temp = testnombre(Temp)
        if Temp != False:
            Pari = Temp
            try:           
                assert Pari >= 0
                assert Pari < 50
            except AssertionError:
                print('La roulette ne contient pas ce nombre!')
                Pari = None

    Resultat = randrange(50)
    print("La bille de la roulette s\'arrête sur :", Resultat, "!")

    if Resultat == Pari:
        Gains = Mise * 3
        print("Jackpot! Vous avez misé sur le bon nombre!\nFélicitations vous gagnez :", Gains, "jetons !")
    elif (Resultat % 2 == 0 and Pari % 2 == 0) or (Resultat % 2 != 0 and Pari % 2 != 0):
        Gains = ceil(Mise * 1.5)
        print("Pas si mal! Bonne couleur\nFélicitations vous gagnez :", Gains, "jetons !")
    else:
        Gains = 0
        print("Rien de gagné cette fois...")

    ReserveJoueur = ReserveJoueur + Gains
    
    if ReserveJoueur <= 0:
        print("vous êtes fauché!!")
        Suite = input("Voulez vous reprendre des jetons? (o/n) ")
        if Suite == "o":
            ReserveJoueur = None
            while ReserveJoueur == None:
                Temp = input("Combien de jetons voulez vous pour jouer? ")
                Temp = testnombre(Temp)
                if Temp != False:
                    ReserveJoueur = Temp
        else:
            exit()
    else:
        print("Il vous reste :", ReserveJoueur, "jeton(s)")
        Suite = input("Voulez vous continuer à parier? (o/n) ")
