# ############################# #
# LHSI 2015-04-17 bissextile.py #
# ############################# #

# My first python script
# which get a year and
# return if the year is bissextile or not

print("Tell me which year do you want to test ?")

#ask a number to the user
year = input("YYYY ? : ")

#transtypage str to int
year = int(year)

#First version which is heavy
""" 
if year % 4 != 0: #case when the year is not bissextile
    print (year, "is not bissextile.")
elif year % 100 == 0:
    if year % 400 == 0:
        #case where year%4 and %100 and %400 = year is bissextile
        print(year, "is bissextile.")
    else:
        print(year, "is not bissextile.")
else:
    print(year, "is not bissextile.")
"""

#Second version
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
	print(year, "is bissextile.")
else:
	print(year, "is NOT bissextile.")
