import serial
import time
import MySQLdb
 
ser = serial.Serial(port= "/dev/ttyAMA0",
			baudrate = 9600,
			parity = serial.PARITY_NONE,
			stopbits = serial.STOPBITS_ONE,
			bytesize = serial.EIGHTBITS,
			timeout =1)

#ser.baudrate=9600
out = ""
count=0

db = MySQLdb.connect("localhost","root","root","framedata")

cur = db.cursor()

while 1:
	data = ser.read(5)
	words = data.split(" ")
	
	sql_find = 'SELECT %s FROM STARTUP;' %(words[0])
	print sql_find
	try:
		cur.execute(sql_find)
		results = cur.fetchall()
	
		for value in results:
	
			r = str(value[0])
		
			r+="n" 

			print(str(r))
	
	#print data
			ser.write(r)
	except MySQLdb.Error as DBIE:
		print DBIE
	
ser.close()
db.close()
