#!/usr/python3.4
# -*- coding:utf-8 *-

class Exemple:
	"""Un petit exemple de classe"""
	def __init__(self,nom):
		"""Exemple de constructeur"""
		self.nom = nom
		self.autre_attribut = "une valeur"
	def __del__(self):
		"""Méthode appelé quand l'objet est supprimé"""
		print("C'est la fin ! On me supprime !")

class Personne:
	"""Classe représentant une personne"""
	def __init__(self,nom, prenom):
		"""constructeur de notre classe"""
		self.nom = nom
		self.prenom = prenom
		self.age = 29
		self.lieu_residence = "Lille"

	def __repr__(self):
		"""Qand on entre dans notre objet dans l'interpreteur"""
		return "Personne: nom({}), prénom({}), âge({})".format(self.nom, self.prenom, self.age)

	def __str__(self):
		"""Méthode permettant d'afficher plus joliment notre objet"""
		return "{} {}, âgé de {} ans".format(self.prenom,self.nom,self.age)

	"""def __setattr__(self, nom_attr, val_attr):
		Méthode appelée quand on fait objet.nom_attr ) val_attr.
		On se charge d'enregistre l'objet

		object.__setattr__(self, nom_attr, val_attr)
		self.enregistrer()"""

anyone = Personne("Lhoir","Simon")
print(anyone)
chaine = str(anyone)
print(chaine)


print("\n\n__getattr__\n\n")

class Protege:
	"""Classe possédant une méthode particulière d'accès à ses attributs :
	Si l'attribu n'est pas trouvé, on affiche une alerte et renvoie None"""

	def __init__(self):
		"""On créze quelques attributs par défaut"""
		self.a = 1
		self.b = 2
		self.c = 3
	def __getattr__(self, nom):
		"""Si Python ne trouve pas l'attribut nommé "nom", il appelle
		cette méthode. On affiche une alerte """

		print("Alerte ! Il n'y a pas d'attribut {} ici !".format(nom))

pro = Protege()

print(pro.a)
print(pro.b)
pro.e