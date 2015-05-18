#!/usr/python3.4
# -*-coding:utf_8 -*

def chiffreMot(mot):
	hidden = ""
	print hidden
	print range(len(mot))
	for i in range(len(mot)):
		print mot[i]
		hidden += "_"
		print hidden
	return hidden

print chiffreMot("test")

"""
dico = {'hidden':"mot",'founded':"secret",'tantativ':"",'essai':"8"}

def fonction(**dico):
	print("{}\n{}\n{}\n{} ".format(dico['hidden'],dico['founded'],dico['tantativ'],dico['essai']))

fonction(**dico)
"""