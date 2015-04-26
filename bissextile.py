#!/usr/bin/env python3
# coding: utf-8

def bissextile(year):
    try: year = int(year)
    except: return False

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True;
            return False;
        return True;
    return False;

entry = input("Entrez une année : ");
print('Bissextile' if bissextile(entry) else 'Non bissextile')