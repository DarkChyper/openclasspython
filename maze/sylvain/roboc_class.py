# -*- coding: utf8 -*
class svg:
    """
    contient les données de la partie en cours
    """
    
    def __init__(self):
        """
        création de la base de la sauvegarde
        """
        self.carte = None
        self.Longueurligne = 0
        self.Nbrligne = 0
        self.posX = []
        self.plan = []
        self.victoire = False

    def checkpos(self, tempposX):
        """
        Vérifie la validité de la nouvelle position par rapport aux données de taille de carte
        Retourne un Booléen
        """
        if tempposX[0] > 0 and tempposX[1] > 0 and tempposX[0] <= self.Nbrligne and tempposX[1] <= self.Longueurligne:
            return True
        else:
            print("Ce déplacement est impossible!")
            return False

    def save(self):
        """
        via pickle sauvegarde la partie
        pas de retour
        """
        import pickle
        with open("scores", "wb") as Scores:
            mon_pickler = pickle.Pickler(Scores)
            mon_pickler.dump(self)

    def clear(self):
        """
        réinitialise la sauvegarde
        pas de retour
        """
        self.carte = None
        self.Longueurligne = 0
        self.Nbrligne = 0
        self.posX = []
        self.plan = []
        self.victoire = False
