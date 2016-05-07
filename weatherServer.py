import serial
import sys
import subprocess
import time

import grabToday

def updateTide():
	a1 , b1 = grabToday.getToday()
	print(a1)
	print(b1)



'''
try:
	ser = serial.Serial( '/dev/ttyACM0' , 9600 )
except:
	try:
		ser = serial.Serial( '/dev/ttyACM1' , 9600 )
	except:
		pass


recievedData = ""
testValue = "c"


# constant read serial 
while 1:

	recievedData = ser.readline()
	recievedData = str( recievedData )
	recievedData = recievedData.replace( " " , "" )
	recievedData = recievedData.rstring()

	print( recievedData )

	# test value

	# if test passes , send a response
	ser.write('1')
	
'''