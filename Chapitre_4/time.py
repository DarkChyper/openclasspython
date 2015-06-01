#!/usr/bin/python3.4

import time
import datetime

print("Jouons avec le temps")
"""
avant = time.time()
print(avant)
time.sleep(10)
apres = time.time()
print(apres)
print("On vient de perdre {} secondes".format(apres - avant))
"""
print(time.strftime("%A %d %B %Y %H:%M:%S"))

print(datetime.date.today())

print(datetime.datetime.now())