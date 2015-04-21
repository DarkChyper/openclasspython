#!/usr/bin/python3.4
# -*- coding: utf8 -*-
temp = input('entrez une année : ')

while temp != 'quit':
    try:
        ann = int(temp)
        if ann%4 == 0:
            if ann%100 == 0:
                if ann%400 == 0:
                    bisextile = True
                else:
                    bisextile = False
            else:
                bisextile = True
        else:
            bisextile = False

        if bisextile:
            print('c\'est une année bisextile!')
        else:
            print('ce n\'est pas une année bisextile!')
            
    except:
        print('ce n\'est pas un chiffre mais un(e)', type(temp))
    
    temp = input('entrez une année : ')

