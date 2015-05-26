README.md

Exécution :
Le fichier à exécuter est roboc.py
Le shebang en tête de fichier permet de lancer directement l'exécutable peu importe d'OS, cependant si vous avez une installation concurrente de python 2 et 3 :
py -3 roboc.py

Brèves explication sur les méthodes de développements :
- J'ai utilisé beaucoup de commentaires par endroit, notamment pour faciliter la compréhension de la modélisation
- Certains commentaires pourrons paraître superflus mais sont cependant nécessaires (premier affichage, etc.)
- La modélisation du labyrinthe sous forme de liste à 2 dimensions peut paraître assez "bourrine", cependant je souhaite nuancer :
    - Elle permet une grande modularité (ajouter une 3e dimension n'en est que plus facile, ajouter des obstacles, etc.)
    - La gestion des indices est très facilité (jouer sur les indices des ordonnées et des abcisses)
- En termes de nommage, pour m'éviter un effort de test, je n'ai pas renommé les classes et les variables pour coller au contexte,
    comprenez :
    Map     = labyrinthe
    Joueur  = robot

Bonne lecture !