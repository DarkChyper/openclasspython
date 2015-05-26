README.md

Exécution :
    Le fichier à exécuter est roboc.py
    Le shebang en tête de fichier permet de lancer directement l'exécutable peu importe d'OS, cependant si vous avez une installation concurrente de python 2 et 3 :
    py -3 roboc.py

Écarts :
    En relisant l'énoncé, il apparaît que je l'ai lu trop rapidement, et il est trop tard pour de quelconques modifications :
    - Le franchissement des portes se fait comme suit :
        - Peu importe la longueur du mouvement, on s'arrête devant la porte.
        - Peu importe la longueur du mouvement suivant, on saute la porte et on ne va pas plus loin.
    - Le rafraichissement de la carte se fait comme suite :
        Je ne rafraîchis et n'affiche la carte qu'une fois par entrée utilisateur (ex : s5, je fais le mouvement entier et j'affiche la carte)
        D'après l'exemple, il apparaît que pour chaque déplacement unitaire au sein d'un même déplacement, on doit rafraîchir la carte et l'afficher
        (ex : s5, je fais un pas, je rafraîchis et j'affiche, puis un 2nd, je rafraîchis et j'affiche, etc., jusqu'au 5e)

Brèves explication sur les méthodes de développement :
    - J'ai utilisé beaucoup de commentaires par endroit, notamment pour faciliter la compréhension de la modélisation
    - Certains commentaires pourrons paraître superflus mais sont cependant nécessaires (premier affichage, etc.)
    - La modélisation du labyrinthe sous forme de liste à 2 dimensions peut paraître assez "bourrine", cependant je souhaite nuancer :
        - Elle permet une grande modularité (ajouter une 3e dimension n'en est que plus facile, ajouter des obstacles, etc.)
        - La gestion des indices est très facilité (jouer sur les indices des ordonnées et des abcisses)
    - En termes de nommage, pour m'éviter un effort de test, je n'ai pas renommé les classes et les variables pour coller au contexte,
        comprenez :
        Map     = labyrinthe,
        Joueur  = robot

Bonne lecture !