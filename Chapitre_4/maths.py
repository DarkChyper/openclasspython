#!/usr/bin/python3.4

import math
from fractions import Fraction
import random

droit = 90
droitRad = math.radians(droit)

print("Un angle droit ({}°) vaut en radiant : {}".format(droit, droitRad))
print("Et ce radian peut être reconverti en angle droit : {}".format(math.degrees(droitRad)))

x = 3.8

print(x)

print("ceil {} = {}".format(x, math.ceil(x)))

print("floor {} = {}".format(x, math.floor(x)))

print("trunc {} = {}".format(x, math.trunc(x)))

print("Pi = ", math.pi)

print("E = ", math.e)

un_demi = Fraction(1, 2)
un_demi
print(un_demi)

un_quart = Fraction('1/4')
un_quart
print(un_quart)

autre = Fraction(-5, 30)
autre
print(autre)

print(Fraction.from_float(0.5))


print(random.random())
