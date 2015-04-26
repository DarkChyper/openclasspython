#!/usr/bin/env python3
# coding: utf-8


#######################################################################################
# AUTEUR/AUTHOR : Fabien HUITELEC
#######################################################################################
# TP à réaliser dans le cadre d'une certification délivrée par OpenClassroom
# Pour en connaître l'intitulé exact, cliquer sur le lien ci-dessous :
#######################################################################################
# Practical work realized as part of a certificating course delivered by OpenClassroom
# To acknowledge the content of the said PW, please click the link below
# Comments and messages are in French. Dear english speakers, forgive me
#######################################################################################
# http://openclassrooms.com/courses/apprenez-a-programmer-en-python/tp-tous-au-zcasino
#######################################################################################

from random import randrange
from math import ceil

### DEMANDER_MISE ######################
# Si __mise_de_base est à True, cela
# concerne la mise de départ et on skip
# le contrôle car le joueur peut y entrer
# le nombre souhaité
########################################
def demander_mise(mise_de_base = False):
    global compte
    mise = None
    message = "Entrez ce que vous souhaitez ajouter à votre compte : " if mise_de_base else "Entrez votre mise : "

    while type(mise) != int:
        try:
            mise = int(input(message))
            if mise_de_base is False: assert ( mise <=  compte )
        except AssertionError:
            print("Mise supérieur à ce que vous possédez !")
            mise = None
        except: continue
    print(mise)
    return mise

### DEMANDER_NUMERO ####################
# Demande un numéro entre 0 et 49
########################################
def demander_numero():
    numero = None

    while type(numero) != int:
        try:
            numero = int(input("Entrez le numéro sur lequel vous souhaitez miser : "))
            assert ( numero >= 0 and numero < 50 )
        except AssertionError:
            print("Doit être entre 0 et 49 compris")
            numero = None
        except: continue
    print(numero)
    return numero

### FAIRE_TOURNER ######################
# Tire un entier entre 0 et 50 et le
# compare à __numero.
# Retourne la mise impactée
########################################
def faire_tourner(mise, numero):
    global compte
    numero_roulette = randrange(50)
    message = "Numéro " + str(numero_roulette) + "\n"

    if numero_roulette == numero:
        retour = mise * 4
        message += "Vous avez gagné " + str(retour) + "\n"
    elif numero_roulette % 2 == numero % 2:
        retour = ceil(mise * 1.5)
        message += "Vous avez gagné " + str(retour) + "\n"
    else:
        retour = mise * -1
        message += "Vous avez perdu " + str(retour) * -1 + "\n"
    message += "Votre compte : " + str(compte + retour)
    print(message)
    return retour

### PLAY ###############################
# Fait varier le compte en fonction du
# résultat fourni par faire_tourner()
# En demander au joueur une mise et un
# numéro
########################################
def play():
    global compte

    # On soustrait le compte du résultat
    compte += faire_tourner( demander_mise(),  demander_numero() )


### MAIN ###############################
# Tant que le compte le permet, on
# continue de jouer
########################################
compte = demander_mise(True)

while compte > 0:
    play()

print("Terminé !")