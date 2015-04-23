# ################################################################ #
# DEFINITION OF MY FUNCTION TO KNOW IF A YEAR IS BISSEXTILE OR NOT #
#                                                                  #  
def is_bis(annee)
	try:
		year = int(annee)
	except:
		# RETURN FALSE IF ARGUMENT IS NOT A INT()
		return False

	if year % 400 == 0 or ( year % 4 == 0 and year % 100 != 0):
		return True
	else: 
		return false 
