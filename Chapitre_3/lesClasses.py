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
        self._lieu_residence = "Lille"

    def _get_lieu_residence(self):

        """Méthode qui sera appelée quand on souhaitera accéder en lecture 
        à l'attribut 'lieu_residence'"""

        print("On accède à l'attribut lieu_residence !")
        print self._lieu_residence
    def _set_lieu_residence(self, nouvelle_residence):
        """Méthode appelée quand on souhaite modifier le lieu de résidence"""
        print("Attention, il semble que {} déménage à {}.".format(self.prenom, nouvelle_residence))
        self._lieu_residence = nouvelle_residence
    # On va dire à Python que notre attribut lieu_residence pointe vers une
    # propriété
    lieu_residence = property(_get_lieu_residence, _set_lieu_residence)

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

print("On crée la personne 'Simon'")
simon = Personne("Lhoir","Simon")
print simon.nom
print simon.prenom
print simon.age
simon.lieu_residence
simon.lieu_residence = "Wasquehal"
print simon.lieu_residence

