import serial 
import time
import MySQLdb
from decimal import *
import sys

ser = serial.Serial(port = "/dev/ttyAMA0",

				baudrate = 9600,
				parity = serial.PARITY_NONE,
				stopbits = serial.STOPBITS_ONE,
				bytesize = serial.EIGHTBITS,
				timeout = 1)

db = MySQLdb.connect("localhost","root","root","framedata")


db2 = MySQLdb.connect("localhost","stewie3540","root","reaction")

cur = db.cursor()
cur2 = db2.cursor()

List = []
result = ""
a={}
def readlineCR(ser):
	while 1:

		data = ser.read(11)
		ser.flushInput()

		#print data		

		#words = data.split()
		#print data

		if data  == "CR_MP CR_HP":
			words = data.split()
			sqlfind = 'SELECT %s, %s FROM STARTUP union SELECT %s, %s FROM ACTIVE union SELECT %s, %s FROM RECOVERY;'  %(words[0] , words[1], words[0], words[1], words[0], words[1])
			#print sqlfind
			try: 
				cur.execute(sqlfind)

							
				for i in range (cur.rowcount):
					
					row = cur.fetchone()
					row1 = str(row[0])
					row2 = str(row[1]) 
					n = reduce(lambda rst, d: rst + d, (row1,row2))

					#print row1
					#ser.close()				
					yield n
					

			#except MySQLdb.Error, e:
				
				 #print "MySQL Error [%d]: %s" % (e.args[0], e.args[1]) 
			except NameError as e:
				print e  
				



a = readlineCR(ser)

row1 = next(a)

row2 =  next(a)

row3 = next(a)


result = row1+row2+row3+"n"


ser.write(result)
ser.flushOutput()
ser.flushInput()

count =0

while count<5:
	dataInput = ser.read(20)
	ser.flushInput()

	if dataInput.isupper():
		#print "fail"
		sys.stdout.write("fail")
		sys.stdout.flush()
		
		
	elif dataInput<0:
		
		print "too slow"
	else:
		
		line = dataInput.strip().split(',')
		#print line
		try:
			first = line[0]
			second = line[1]
			third = line[2]
			fourth = line[3]
		except IndexError:
			continue
			
		#print first , second, third, fourth
	
		sqlInsert = 'INSERT INTO CR_MP_CR_MP_CR_HK(CR_MP,CR_HK,CR_MP_FRAMES,CR_HK_FRAMES,TIMING,DATES) VALUES(%s,%s,%s,%s,CURTIME(),CURDATE())' %(first, second,third,fourth)
		#sys.stdout.write(sqlInsert)
		#sys.stdout.flush()

		#d=int(Decimal(dataInput))
		try:
			#sys.stdout.write("Inserting data")
			#sys.stdout.flush()

			cur2.execute(sqlInsert)
			db2.commit()
			#print "Data committed"
			count+=1

		except MySQLdb.Error as dbie:
			print dbie
			db2.rollback
		#print dataInput + "is string"

ser.close()

db.close()
db2.close()
