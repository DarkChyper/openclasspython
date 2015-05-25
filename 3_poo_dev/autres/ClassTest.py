#!/usr/bin/env python
# Coding: utf-8

class Personne:
    """
    Classe définissant une personne caractérisé par :
    - nom
    - prenom
    - age
    - lieu de résidence
    """

    def __init__(self, nom, prenom, age, lieu_residence = "Lille"):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.lieu_residence = lieu_residence