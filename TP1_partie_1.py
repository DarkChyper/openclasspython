#!/usr/bin/python3.4
# -*- coding: utf8 -*-

temp = input('entrez une année : ')

while temp != 'quit':
    try:
        ann = int(temp)
    except:
        print('ce n\'est pas un chiffre mais un(e)', type(temp))
    else:
        if (ann%400 == 0) or (ann%4 == 0 and ann%100 != 0):
            print('c\'est une année bisextile!')
        else:
            print('ce n\'est pas une année bisextile!')
    finally:
        temp = input('entrez une année : ')

