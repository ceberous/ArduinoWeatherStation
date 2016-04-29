#!/bin/python

from pyquery import *
from time import strftime

def getCurrentTime():
	return strftime( "%H:%M" )


def getNextHighTide():

	cT = getCurrentTime()
	cT = cT.split(":")
	cTHours 	= int( cT[0] )
	cTMinutes 	= cT[1]

	h1 	= high1Time.split(":")
	h1Hours  	= h1[0]
	h1Minutes 	= h1[1]
	h1AMPM		= h1Minutes[-2] + h1Minutes[-1]
	h1Minutes   = int( h1Minutes[:-2] )

	h2 = high2Time.split(":")
	h2Hours		= h2[0]
	h2Minutes 	= h2[1]
	h2AMPM 		= h2Minutes[-2] + h2Minutes[-1]
	h2Minutes	= int( h2Minutes[:-2] )

	#24 Hour Conversion
	h1Hours = ( ( int(h1Hours) + 12 ) , (h1Hours) )[h1AMPM == "am"]
	h2Hours = ( ( int(h2Hours) + 12 ) , (h2Hours) )[h2AMPM == "am"]

	#print( "Current Time = " + cTHours + ":"  + cTMinutes )
	#print( "H1-Time = " + h1Hours + ":"  + h1Minutes + " " + h1AMPM )
	#print( "H2-Time = " + h2Hours + ":"  + h2Minutes + " " + h2AMPM )


	#if ( cTHours > h1Hours ) :
	hoursLeft = h2Hours - cTHours
	x =  h2Minutes + ( 60 - h2Minutes )
	hoursLeft = str(hoursLeft)
	x = str(x)
	print("next high tide = " + hoursLeft + ":" + x )


d = PyQuery( url='http://tides.willyweather.com/wa/mason-county/lilliwaup.html' )

x = d('.info')#.children()
y = x[0].getchildren()

low1 			= y[0].text # Low
low1TideWrap 	= y[1].getchildren()
low1Time 		= low1TideWrap[0].text
low1Height 		= low1TideWrap[1].text

high1 			= y[2].text
high1TideWrap 	= y[3].getchildren()
high1Time 		= high1TideWrap[0].text
high1Height 	= high1TideWrap[1].text

low2			= y[4].text
low2TideWrap	= y[5].getchildren()
low2Time		= low2TideWrap[0].text
low2Height		= low2TideWrap[1].text

high2			= y[6].text
high2TideWrap	= y[7].getchildren()
high2Time		= high2TideWrap[0].text
high2Height 	= high2TideWrap[1].text


getNextHighTide()

'''
print(low1)
print("------------")
print(low1Time)
print(low1Height)

print("\n")

print(high1)
print("------------")
print(high1Time)
print(high1Height)

print("\n")

print(low2)
print("------------")
print(low2Time)
print(low2Height)

print("\n")

print(high2)
print("------------")
print(high2Time)
print(high2Height)
'''

