#!/usr/bin/env python
# -*- coding: utf-8 -*-

# P15040 GEORGE ZERVOLEAS
# 30/1/2016
# ASKISI 5
print "***********************************"
\
date=raw_input("Dwse tin imeronia sti morfi dd-mm-yyyy:")
originaldate=date
date=date.split("-")
day=int(date[0])
month=int(date[1])
year=int(date[2])
century=year/100
var_for_2sekto=int(date[1])

#kwdikos month

if (month==2 or month==3 or month==11):
	month=4
elif (month==4 or month==7):
	month=0
elif (month==5):
	month=2
elif (month==6):
	month=5
elif (month==8):
	month=3
elif (month==9 or month==12):
	month=6
elif (month==1 or month==10):
	month=1
	
#kwdikos century	

if (century==16 or century==20):
	century=6
elif (century==17 or century==21):
	century=4
elif (century==18 or century==22):
	century=2
elif (century==19 or century==23):
	century=0


# kwdikos year

codeyear=(century+(year%100)+(year%100)/4)%7

#and finally 

day=(codeyear+month+day)%7	

#upologismos 2sektou******

etos=1
if (year%4==0):
	etos=2
	
if (etos==2 and (var_for_2sekto==1 or var_for_2sekto==2)):
	day=day-1
#****************************

print "Stis " +originaldate +" Itan "

if (day==0):
	print "Sabbato"
elif (day==1):
	print "Kyriaki"
elif (day==2):
	print "Deutera"
elif (day==3):	
	print "Triti"
elif (day==4):
	print "Tetarti"
elif (day==5):
	print "Pempti"
elif (day==6):
	print "Paraskevi"
elif (day==-1):
	print "Paraskevi"
	
print "****************************************"
