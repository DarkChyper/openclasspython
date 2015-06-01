#!/usr/bin/python3.4

import sys
import os
import signal
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("x", type=int, help="le nombre a mettre au carré")
parser.add_argument("-v", "--verbose", action="store_true", help="augmente la verbosité")
args = parser.parse_args()
x = args.x
retour = x ** 2
if ars.verbose:
	print("{} ^ 2 = {}".format(x,retour))
else:
	print(retour)
sys.exit(0)

print("Vous avez précisé X=", args.x)

print("Jouons avec le systeme !")

print(sys.stdin)
print(sys.stdout)
print(sys.stderr)

fichier = open('sortie.txt', 'w')
sys.stdout = fichier
print("Quelque chose...")

sys.stdout = sys.__stdout__
print(os.getcwd())

signal.SIGINT

def fermer_programme(signal, frame):
	"""Fonction appelée quand vient l'heure de fermer notre progrmme"""
	print("C'est l'heure de la fermeture !")
	sys.exit(0)

# Connexion du signa à notre fonction
signal.signal(signal.SIGINT, fermer_programme)

#while 1:
	#continue

print(sys.argv)