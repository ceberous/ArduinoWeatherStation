#!/usr/bin/python

from pyquery import *
from time import strftime
from datetime import datetime
from array import array
import time

FMT = '%H:%M'

tomorrowHigh = ""
tomorrowLow = ""

def getCurrentTime():
	return strftime( "%H:%M" )


d = PyQuery( url='http://tides.willyweather.com/wa/mason-county/lilliwaup.html' )

x = d('.info')#.children()

def getTomorrow():

	global tomorrowHigh
	global tomorrowLow

	y = x[1].getchildren()

	first			= y[0].text
	firstContents 	= y[1].getchildren()
	second 			= y[2].text
	secondContents	= y[3].getchildren()
	third 			= y[4].text
	thirdContents  	= y[5].getchildren()
	forth 			= y[6].text
	forthContents	= y[7].getchildren()

	firstTime 	= firstContents[0].text
	secondTime 	= secondContents[0].text
	thirdTime 	= thirdContents[0].text
	forthTime 	= forthContents[0].text

	if first == "High":
		h1Time = firstTime
		h2Time = thirdTime
		l1Time = secondTime
		l2Time = forthTime
	else:
		h1Time = secondTime 
		h2Time = forthTime
		l1Time = firstTime
		l2Time = thirdTime


	h1 			= h1Time.split(":")
	h1Hours 	= 0 if h1[0] == "-" else int(h1[0])
	h1Minutes 	= "00am" if h1Hours == 0 else h1[1]
	h1AMPM		= h1Minutes[-2] + h1Minutes[-1]
	h1Minutes 	= int( h1Minutes[:-2] )

	h2 			= h2Time.split(":")
	h2Hours		= 0 if h2[0] == "-" else int(h2[0])
	h2Minutes	= "00am" if h2Hours == 0 else h2[1]
	h2AMPM		= h2Minutes[-2] + h2Minutes[-1]
	h2Minutes	= int( h2Minutes[:-2] )

	l1 			= l1Time.split(":")
	l1Hours		= 0 if l1[0] == "-" else int(l1[0])
	l1Minutes	= "00am" if l1Hours == 0 else l1[1]
	l1AMPM		= l1Minutes[-2] + l1Minutes[-1]
	l1Minutes 	= int( l1Minutes[:-2] )

	l2			= l2Time.split(":")
	l2Hours		= 0 if l2[0] == "-" else int(l2[0])
	l2Minutes	= "00am" if l2Hours == 0 else l2[1]
	l2AMPM		= l2Minutes[-2] + l2Minutes[-1]
	l2Minutes	= int( l2Minutes[:-2] )


	# 24 Hour Conversion
	h1Hours = ( ( h1Hours + 12 ) , (h1Hours) )[h1AMPM == "am"]
	h2Hours = ( ( h2Hours + 12 ) , (h2Hours) )[h2AMPM == "am"]
	l1Hours = ( ( l1Hours + 12 ) , (l1Hours) )[l1AMPM == "am"]
	l2Hours = ( ( l2Hours + 12 ) , (l2Hours) )[l2AMPM == "am"]

	'''
	print( "Tomorrow = " )
	print("-------------------------")
	print( "H1 = " + str(h1Hours) + ":" + str(h1Minutes) )
	print( "H2 = " + str(h2Hours) + ":" + str(h2Minutes) )
	print("-------------------------")
	print( "L2 = " + str(l1Hours) + ":" + str(l1Minutes) )
	print( "L2 = " + str(l2Hours) + ":" + str(l2Minutes) )
	'''

	# Classic Minute adjustment
	if h1Minutes < 10:
		h1Minutes = "0" + str( h1Minutes )
	if l1Minutes < 10:
		l1Minutes = "0" + str( l1Minutes )

	tomorrowHigh = str(h1Hours) + ":" + str(h1Minutes) 
	tomorrowLow = str(l1Hours) + ":" + str(l1Minutes)
	#print( "Tomorrow High = " + tomorrowHigh)
	#print( "Tomorrow Low = " + tomorrowLow)

def getToday():

	getTomorrow()

	global tomorrowHigh
	global tomorrowLow

	y = x[0].getchildren()

	first			= y[0].text
	firstContents 	= y[1].getchildren()
	second 			= y[2].text
	secondContents	= y[3].getchildren()
	third 			= y[4].text
	thirdContents  	= y[5].getchildren()
	forth 			= y[6].text
	forthContents	= y[7].getchildren()

	firstTime 	= firstContents[0].text
	secondTime 	= secondContents[0].text
	thirdTime 	= thirdContents[0].text
	forthTime 	= forthContents[0].text

	if first == "High":
		h1Time = firstTime
		h2Time = thirdTime
		l1Time = secondTime
		l2Time = forthTime
	else:
		h1Time = secondTime 
		h2Time = forthTime
		l1Time = firstTime
		l2Time = thirdTime


	h1 			= h1Time.split(":")
	h1Hours 	= 0 if h1[0] == "-" else int(h1[0])
	h1Minutes 	= "00am" if h1Hours == 0 else h1[1]
	h1AMPM		= h1Minutes[-2] + h1Minutes[-1]
	h1Minutes 	= int( h1Minutes[:-2] )

	h2 			= h2Time.split(":")
	h2Hours		= 0 if h2[0] == "-" else int(h2[0])
	h2Minutes	= "00am" if h2Hours == 0 else h2[1]
	h2AMPM		= h2Minutes[-2] + h2Minutes[-1]
	h2Minutes	= int( h2Minutes[:-2] )

	l1 			= l1Time.split(":")
	l1Hours		= 0 if l1[0] == "-" else int(l1[0])
	l1Minutes	= "00am" if l1Hours == 0 else l1[1]
	l1AMPM		= l1Minutes[-2] + l1Minutes[-1]
	l1Minutes 	= int( l1Minutes[:-2] )

	l2			= l2Time.split(":")
	l2Hours		= 0 if l2[0] == "-" else int(l2[0])
	l2Minutes	= "00am" if l2Hours == 0 else l2[1]
	l2AMPM		= l2Minutes[-2] + l2Minutes[-1]
	l2Minutes	= int( l2Minutes[:-2] )

	# 24 Hour Conversion
	h1Hours = ( ( h1Hours + 12 ) , (h1Hours) )[h1AMPM == "am"]
	h2Hours = ( ( h2Hours + 12 ) , (h2Hours) )[h2AMPM == "am"]
	l1Hours = ( ( l1Hours + 12 ) , (l1Hours) )[l1AMPM == "am"]
	l2Hours = ( ( l2Hours + 12 ) , (l2Hours) )[l2AMPM == "am"]

	# Classic Minute adjustment
	if h1Minutes < 10:
		h1Minutes = "0" + str( h1Minutes )
	if h2Minutes < 10:
		h2Minutes = "0" + str( h2Minutes )
	if l1Minutes < 10:
		l1Minutes = "0" + str( l1Minutes )
	if l2Minutes < 10:
		l2Minutes = "0" + str( l2Minutes )

	cT = getCurrentTime()
	cTCache = cT
	cT = cT.split(":")
	cTHours 	= int( cT[0] )
	cTMinutes 	= cT[1]

	# Next High Time
	nextHighTime = ""
	highTimeDifference = ""
	if cTHours > h1Hours and cTHours > h2Hours:
		nextHighTime = str(tomorrowHigh)
		highTimeDifference = datetime.strptime( nextHighTime , FMT ) - datetime.strptime( cTCache , FMT )
	elif cTHours > h1Hours and cTHours <= h2Hours:
		nextHighTime = ( str(h2Hours) + ":" + str(h2Minutes) )
		highTimeDifference = datetime.strptime( nextHighTime , FMT ) - datetime.strptime( cTCache , FMT )
	elif cTHours <= h1Hours:
		nextHighTime = ( str(h1Hours) + ":" + str(h1Minutes) )
		highTimeDifference = datetime.strptime( cTCache , FMT ) - datetime.strptime( nextHighTime , FMT )
	else:
		nextHighTime = "yesterday?"


	# Next Low Time
	nextLowTime = ""
	lowTimeDifference = ""
	if cTHours > l1Hours and cTHours > l2Hours:
		nextLowTime = str(tomorrowLow)
		lowTimeDifference = datetime.strptime( nextLowTime , FMT ) - datetime.strptime( cTCache , FMT )
	elif cTHours > l1Hours and cTHours <= l2Hours:
		nextLowTime = ( str(l2Hours) + ":" + str(l2Minutes) )	
		lowTimeDifference = datetime.strptime( nextLowTime , FMT ) - datetime.strptime( cTCache , FMT )
	elif cTHours <= l1Hours:
		nextLowTime = ( str(l1Hours) + ":" + str(l1Minutes) )
		lowTimeDifference = datetime.strptime( cTCache , FMT ) - datetime.strptime( nextLowTime , FMT )
	else:
		nextLowTime = "yesterday?"


	print( "Next High Tide in : " + str(highTimeDifference) )
	print( "Next Low Tide in : " + str(lowTimeDifference) )

	return highTimeDifference , lowTimeDifference



