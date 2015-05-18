#!/usr/python3.4
# -*-coding:utf_8 -*

""" les classes
"""

class Personne:
    """Classe définissant une personne caractérisée par :
    - son nom
    - son prénom
    - son age
    - son lieu de résidence"""
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom
        self.age = 29
        self.lieu_residence = "Lille"

class Compteur:
    """Cette classe possède un attribut de classe qui s'incrémente à chaque
    fois que l'on cré un objet de ce typeé"""
    objets_crees = 0 # le compteur vaut 0 au départ

    def __init__(self):
        Compteur.objets_crees += 1
    def combien(cls):
        print("jusqu'à présent, {} objet(s) ont été créé(s)".format(cls.objets_crees))

combien = classmethod(combien)
class TableauNoir:
    """Classe définissant un tableau noir sur lequel on peut écrire, lire et effacer"""

    def __init__(self):
        self.surface = ""

    def ecrire(self, message_a_ecrire):
        """Méthode permettant d'écrire sur la surface du tableau.
        Si la surface n'est pas vide, on ajoute saute une ligne avant de rajouter
        le message à écrire"""
        if self.surface != "":
            self.surface += "\n"
        self.surface += message_a_ecrire

    def lire(self):
        """Cette méthode se charge d'afficher, grâce à print,
        le contenu de la surface tu tableau"""
        print(self.surface)

    def effacer(self):
        """Cette méthode permet d'effacer la surface du tableau"""
        self.surface= ""

print("Voici un tableau vide :")
tab = TableauNoir()
tab.lire()

print("On écrit sur le tableau")
tab.ecrire("F*ck ce ne sont pas les vacances :(")
tab.lire()

print("On ajoute une ligne")
tab.ecrire("Et en plus il fait moche !!!")
tab.lire()

print("A la fin on efface tout")
tab.effacer()
tab.lire()

