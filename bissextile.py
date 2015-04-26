#!/usr/bin/env python3
# coding: utf-8

def bissextile(year):
    try: year = int(year)
    except: return False
    return ( year % 400 == 0 ) or ( year % 4 == 0 and year % 100 != 0 )

entry = input("Entrez une année : ");
print('Bissextile' if bissextile(entry) else 'Non bissextile')