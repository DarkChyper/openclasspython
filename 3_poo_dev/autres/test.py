#!/usr/bin/env python
# Coding: utf-8

from ClassTest  import *

francis = Personne("Dupond", "Francis", 18, "Londres")
print(francis.lieu_residence)

fabien = Personne("Huitelec", "Fabien", 21)
print(fabien.lieu_residence)
help(Personne)
fabien.bla()
fabien.interne()
