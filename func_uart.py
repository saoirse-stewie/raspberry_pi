import serial 
import time
import MySQLdb

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
		if data  == "CR_MP CR_HP":
			words = data.split()
			sqlfind = 'SELECT %s, %s FROM ACTIVE union SELECT %s, %s FROM STARTUP union SELECT %s, %s FROM RECOVERY;' %(words[0] , words[1], words[0], words[1], words[0], words[1])
			print sqlfind
			try: 
				cur.execute(sqlfind)
							
				for i in range (cur.rowcount):
					
					row = cur.fetchone()
					row1 = str(row[0])
					row2 = str(row[1])
					#print word[0]
									
					yield row1 + row2
					
				
				
			except MySQLdb.Error as DBIE:
				print DBIE 




print "hello"
a = readlineCR(ser)
row1 = next(a)
row2 =  next(a)
row3 = next(a)
result = row1+row2+row3+"n"
#print result
ser.write(result)
ser.flushOutput()

ser.close()
db.close()
