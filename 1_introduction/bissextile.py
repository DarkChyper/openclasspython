#!/usr/bin/env python3
# coding: utf-8

from util import pause

def bissextile(year):
    bis = ( year % 400 == 0 ) or ( year % 4 == 0 and year % 100 != 0 )
    print('Bissextile' if bis else 'Non bissextile')


year = None

while type(year) != int:
    try:    year = int(input("Entrez une année : "))
    except: continue
    else:   bissextile(year)

pause()