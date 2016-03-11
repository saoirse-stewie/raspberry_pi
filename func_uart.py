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
		#words = data.split()
		#print data
		if data  == "CR_MP CR_HP":
			words = data.split()
			sqlfind = 'SELECT %s, %s FROM ACTIVE union SELECT %s, %s FROM STARTUP union SELECT %s, %s FROM RECOVERY;' %(words[0] , words[1], words[0], words[1], words[0], words[1])
			print sqlfind
			try: 
				cur.execute(sqlfind)
				#results = cur.fetchall()
				#print len(cur.description)	
				for i in range (cur.rowcount):
					
					row = cur.fetchone()
					#print row[0]
					row1 = str(row[0])
					row2 = str(row[1])
					#row3 = str(row[2]) 
					
					#row2 = str(row[1])
					#print readlineCR.row1
					#print row[0]
					#print row[1]
					#print row[0]
					#print row1
					#print row[1]
					#r = "".join(str(results[0]))
					#name = r.translate(None,"()' '")
					#num = int(name.encode('hex'),16)
					#print str(num)
					#num = struct.unpack(">L", name)[0]
					#s = "".join(name)
					#name = r.replace('(', " ").replace(')', " ")					print word[0]
					#print num
					#print len(results)
					#List.append(str(result[0])
					#print result[0]
					#List = str(results[0]) + str(results[1])
					#print List	
					#r = str(results[0])+ str(results[1])
					#n = zip(*r)
					#print(List)	
					 
					#result+="n"
					#print row1
					#print len(row1)
				#print row[0] + row[1]
					yield row1 + row2
					#return readlineCR.row1 + readlineCR.row2
				#print result
				#return  result
			except MySQLdb.Error as DBIE:
				print DBIE 


	
a = readlineCR(ser)
#b= readlineCR(ser)
row1 = next(a)
row2 =  next(a)
row3= next(a)
result = row1+row2+row3+"n"
print result
ser.write(result)
ser.flushOutput()

ser.close()

db.close()
