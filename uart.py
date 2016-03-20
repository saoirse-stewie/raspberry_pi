import time
import serial
import MySQLdb

#db = MySQLdb.connect("localhost", "root" , "root", "framedata")

#cur = db.cursor()
ser = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout=1 # add this
    )
#ser=serial.Serial("/dev/ttyAMA0")
#ser.baudrate = 9600

db = MySQLdb.connect("localhost","root","root","framedata")

cur = db.cursor()

row="";
state=""
r=""
timeout=1

#ser.xonxoff = True
ser.setXON = True
#time.sleep(10)

byteData = ser.read(1)
	#print(byteData)
byteData += ser.read(ser.inWaiting())
words= byteData.split(" ")
print words[0]

sql_find_all = ' SELECT %s, %s FROM STARTUP union SELECT %s,%s FROM ACTIVE union SELECT %s,%s from RECOVERY;' %(words[0], words[1], words[0], words[1], words[0], words[1]) 
print sql_find_all
try:
	
	cur.execute(sql_find_all) 

	results = cur.fetchall()
	for result in results: 
		r = str(result[0]) + str(result[1])
		#n=zip(*r)
		#a = ord(n)
		n=list(str(result[0]))
		a=list(str(result[1]))
	
		#n=(list(zip(r))
	#print(n)
		#print(b + c)
		#ser.write(str(n))
		#time.sleep(2)
		#ser.write(str(a))
		#n = list(result[0])
		ser.write(str(a))
		ser.flushOutput()
		ser.write(str(n))
		ser.flushOutput()
		#print(str(result[0][0]))
		#print(result[0])
		#word = r.split()
		#ser.write(str(n))
		#print(str(word[0])+ " ")  
		#ser.write(str(result[0])+ " ")
		#ser.write(str(r)+ " ")
		#ser.write(str(result[0]) + str(result[1]))
except MySQLdb.Error as DBIE:	
	print DBIE


db.close()
ser.close()
