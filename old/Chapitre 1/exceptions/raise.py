#!/usr/bin/python3.4
# -*-coding:utf_8 -*
print("Tell me which year do you want to test ?")
year = input("YYYY ? : ")
try:
	year = int(year)
	assert year < 0
except AssertionError:
	print("Invalid Value")
else:
	if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
		print(year, "is bissextile.")
	else:
		print(year, "is NOT bissextile.")
