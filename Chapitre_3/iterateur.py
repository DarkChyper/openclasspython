#!/usr/python3.4
# -*- coding:utf-8 

class RevStr(str):
    """Classe reprenant les méthodes et attributs des chaînes construites
    depuis 'str'. On se contente de définir une méthode de parcours
    différente : au lieu de parcourir la chaîne de la première à la dernière
    lettre, on la parcourt de la dernière à la première.
    
    Les autres méthodes, y compris le constructeur, n'ont pas besoin
    d'être redéfinies"""
    def __init__(self, chaine_a_parcourir):
		"""On se positionne à la fin de la chaîne"""
		self.chaine_a_parcourir = chaine_a_parcourir
		self.position = len(chaine_a_parcourir)
    
    def __iter__(self):
		"""Cette méthode renvoie un itérateur parcourant la chaîne
		dans le sens inverse de celui de 'str'"""
		
		return self # On renvoie l'itérateur créé pour l'occasion
	def __next__(self):
		"""Cette méthode doit renvoyer l'élément suivant dans le parcours,
		ou lever l'exception 'StopIteration' si le parcours est fini"""

		if self.position == 0: # Fin du parcours
			raise StopIteration
		self.position -= 1 # On décrémente la position
		return self.chaine_a_parcourir[self.position]

chaine = RevStr("allo")
print chaine
for i in chaine:
	print(i)
