import serial 
import time
import MySQLdb
from decimal import *

ser = serial.Serial(port = "/dev/ttyAMA0",
				baudrate = 9600,
				parity = serial.PARITY_NONE,
				stopbits = serial.STOPBITS_ONE,
				bytesize = serial.EIGHTBITS,
				timeout = 1)

db = MySQLdb.connect("localhost","root","root","framedata")
cur = db.cursor()
List = []
result = ""
a=""
def readlineCR(ser):
	while 1:

		data = ser.read(11)
		ser.flushInput()

		print data		

		#words = data.split()
		#print data

		if data  == "CR_MP CR_HP":
			words = data.split()
			sqlfind = 'SELECT %s, %s FROM STARTUP union SELECT %s, %s FROM ACTIVE union SELECT %s, %s FROM RECOVERY;' %(words[0] , words[1], words[0], words[1], words[0], words[1])
			print sqlfind
			try: 
				cur.execute(sqlfind)

							
				for i in range (cur.rowcount):
					
					row = cur.fetchone()
					row1 = str(row[0])
					row2 = str(row[1]) 
					n = reduce(lambda rst, d: rst + d, (row1,row2))

					#print row1
									
					yield n
					

			except MySQLdb.Error as DBIE:
				print DBIE 





a = readlineCR(ser)

row1 = next(a)

row2 =  next(a)

row3 = next(a)


result = row1+row2+row3+"n"

#print result
#result2 = row3+"n"
#print resultn = reduce(lambda rst, d: rst + d, (row1,row2,row3))
#n = reduce(lambda rst, d: rst + d, (row1,row2,row3))
#result = n + "n"

#print result
#result = row3 + "n"
#r = hex(result)
ser.write(result)
#ser.write(result2)
ser.flushOutput()
ser.flushInput()
while 1:
	dataInput = ser.read(10)
	ser.flushInput()
	if dataInput.encode('hex'): 
		#d=int(Decimal(dataInput))
		print dataInput
		#print dataInput + "is string"

ser.close()

db.close()
