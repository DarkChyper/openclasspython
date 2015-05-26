#!/usr/bin/env python
# coding: utf-8

"""
    Données paramétrables permettant :
    - de binder,
    - changer la représentation des maps,
    - changer le nom du fichier de sauvegarde,
    - etc.
"""

adresse_fichier_sauvegarde = "partie_sauvegardee"

dossier_maps = "maps"

# S'il y a modifications, répercuter sur TOUTES les maps
representation =    {
                    'robot':    'X',
                    'mur':      'O',
                    'porte':    '.',
                    'sortie':   'U',
                    'vide':     ' ',
                    }

touches =   {
            'ouest':    'o',
            'nord':     'n',
            'est':      'e',
            'sud':      's',
            'aide':     'a',
            }