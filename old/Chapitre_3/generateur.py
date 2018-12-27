#!/usr/python3.4
# -*- coding:utf-8 

def intervalle(borne_inf, borne_sup, pas):
	"""

	"""
	if isinstance(pas, float):
		borne_inf = float(borne_inf)
		borne_sup = float(borne_sup)
	
	if borne_inf < borne_sup:
		
		while borne_inf <= borne_sup:
			yield borne_inf
			borne_inf += pas
	elif borne_inf > borne_sup :
		
		while borne_inf >= borne_sup:
			yield borne_inf
			borne_inf -= pas
	else:
		pass
		


for nombre in intervalle(5,10,1):
	print(nombre)
for nombre in intervalle(28,24,0.1):
	print(nombre)