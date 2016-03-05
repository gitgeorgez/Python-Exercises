	#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import json
from pprint import pprint # preferably put this on top of the script, close to the other imports


# P15040 GEORGE ZERVOLEAS
# 30/1/2016
# ASKISI 5
#Routine gia ektyposi apotelesmaton Json Service OPAP

def PrintResults(data):
	theJSON = json.loads(data)
	
	# the distribution dictionary
	dist = {}
    # initialize dist dictionary with 0s
	for i in range(81):
		dist[i] = 0
		
	draws = theJSON['draws'] 
	for draw_key in draws:   
		for row in draws[draw_key]:
			for result in row['results']:
				#if row['drawNo'] == 539052:
				#	print('results are: %d' % result)
				dist[result] += 1
	
	print "Akolouthei o pinakas me ton arithmo twn emfanisewn tou kathe arithmou "
	pprint(dist)
	
def main():
	# Instructions:  http://www.opap.gr/el/web/guest/bowling-ws
	#url gia to JSON Service tou OPAP
	
	print "***********************************"
	\
	date=raw_input("Dwse tin imeronia sti morfi dd-mm-yyyy:")
	print date
	Tempurl = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/"
	urlData = Tempurl + date + ".json"
	print "to url einai: " +urlData
	#urlData = "http://applications.opap.gr/DrawsRestServices/kino/drawDate/28-01-2016.json"
	webUrl = urllib2.urlopen(urlData)
	if (webUrl.getcode() == 200):
		data = webUrl.read()
		PrintResults(data)
	else:	
		print "Received Error"
		


if __name__ == "__main__":
	main()
	