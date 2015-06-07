#!/usr/bin/env python
# coding: utf-8

"""
    Données paramétrables permettant :
    - de binder,
    - changer la représentation des maps,
    - changer les paramètres du serveur,
    - etc.
"""

# Nom du dossier contenant les labyrinthes
dossier_maps = "maps"

# Représentations des items des cartes
representation =    {
                    'robot_courant':    'X',
                    'autre_robot' :     'x',
                    'mur':              'O',
                    'porte':            '.',
                    'sortie':           'U',
                    'vide':             ' ',
                    }

# Binding
touches =   {
            'ouest':        'o',
            'nord':         'n',
            'est':          'e',
            'sud':          's',
            'quit':         'quit',
            'commencer':    'c'
            }

# Serveur
port = 5128
hote = 'localhost'
nb_max_joueurs = 4