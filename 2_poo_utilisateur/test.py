#!/usr/bin/env python
# Coding: utf-8

#########################################################################################
# AUTEUR/AUTHOR : Fabien HUITELEC
#########################################################################################
# Module de tests unitaires
# Pour plus d'informations, lire la description de pendu.py
#########################################################################################
# Unit test module
# For more informations, please read pendu.py's description
#########################################################################################

from fonctions  import *
from donnees    import *
from sys        import exit

mot = [[],[]]
mot[0] = ["m","o","t"]
mot[1] = [True,False,True]
print(mot)
afficher_mot(mot,1)

exit(0)