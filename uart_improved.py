
import serial
import MySQLdb

db = MySQLdb.connect("localhost", "root" , "root", "framedata")

cursor = db.cursor()

#ser = serial.Serial("/dev/ttyAMA0")
#ser.baudrate = 9600
ser = serial.Serial(
    port = '/dev/ttyAMA0',
    baudrate = 9600,
    parity = serial.PARITY_NONE,
    stopbits = serial.STOPBITS_ONE,
    bytesize = serial.EIGHTBITS,
    timeout=1 # add this
    )

row="";
state=""
r=0
timeout=1

#while 1:



byteData = ser.read(1)
byteData += ser.read(ser.inWaiting())
words= byteData.split()
sql_find_all = ' SELECT %s, %s FROM STARTUP union SELECT %s,%s FROM ACTIVE union SELECT %s,%s from RECOVERY;' %(words[0], words[2], words[0], words[2], words[0], words[2]) 
print sql_find_all
try:
	
	cursor.execute(sql_find_all) 

	results = cursor.fetchall()
	for result in results: 
		r = str(result[0]) + str(result[1])  
		ser.write(str(r)+ " ")
except MySQLdb.Error as DBIE:	
	print DBIE


db.close()
ser.close()
