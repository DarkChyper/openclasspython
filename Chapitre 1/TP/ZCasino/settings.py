#!/usr/bin/Python3.4
# -*-coding:utf_8 -*

# choix de la difficulte
def difficulte(diff=2):
	bankInfo = dict()
	if diff==1:
		bankInfo['Bank']=100
		bankInfo['User']=200
	if diff==2:
		bankInfo['Bank']=200
		bankInfo['User']=200
	if diff==3:
		bankInfo['Bank']=500
		bankInfo['User']=100
	if diff==4:
		bankInfo['Bank']=1000
		bankInfo['User']=50
	return bankInfo

