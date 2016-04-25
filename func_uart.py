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
l=[]
result = ""
a={}
def readlineCR(ser):
	while 1:

		data = ser.read(17)
		ser.flushInput()
		
		print data
		if data  == "CR_MP CR_MP CR_HP" or data == "CR_LP ST_LP CL_LP":
			words = data.split()
			sqlfind = 'SELECT %s, %s, %s FROM STARTUP union SELECT %s, %s, %s FROM ACTIVE union SELECT %s, %s, %s  FROM RECOVERY;'  %(words[0] , words[1], words[2] , words[0], words[1],words[2], words[0], words[1], words[2])
		
			try: 
				cur.execute(sqlfind)

							
				for i in range (cur.rowcount):
					
					row = cur.fetchone()
					row1 = str(row[0])
					row2 = str(row[1])
					row3= str(row[2])
 
					n = reduce(lambda rst, d: rst + d, (row1,row2,row3))

									
					yield n
					

		
			except NameError as e:
				print e  
				





def reaction_record(state):
	count =0
	while count<=5:
		dataInput = ser.read(50)
		ser.flushInput()
		print dataInput
			

		state = 0
		if dataInput.isupper():
			
			if dataInput == "FAIL":
				out = "fail"
                       		out = out  + "," + "Too fast" + "," +  "poop" + "," + "blah" + "," +"fix"
                       		#print out
                        	out = " " 
				count+=1
		
		elif dataInput<0:
		
			print "too slow"
		else:


			line = dataInput.strip().split(',')
			try:
				first = line[0]
				second = line[1]
				third = line[2]
				fourth = line[3]
				fifth = line[4]

				#print first, second, third, fourth, fifth
	
		
			except IndexError:
				continue

			if fifth == "cr_mp_cr_mp_cr_hk":	
			
				sqlInsert = 'INSERT INTO CR_MP_CR_MP_CR_HK(CR_MP,CR_HK,CR_MP_FRAMES,CR_HK_FRAMES,TIMING,DATES) VALUES(%s,%s,%s,%s,CURTIME(),CURDATE())' %(first, second,third,fourth)
				try:
					out = " "
					stats = " "
					two_frame = 2
					one_frame = 1

					


					third = round(float(third))
					fourth = round(float(fourth))

					print third,fourth
								
 				
					if int(first)<= 41 and int(first) > 0 and int(second) <= 19 and int(second) > 0:
                                       		out = "succ,"

						two_frame = two_frame - int(third)
						one_frame = one_frame - int(fourth)
					

						if two_frame<0:
                                                        two_frame *= -1
                                                elif one_frame<0:
                                                        one_frame *=-1

						out +=  first + "," + second + "," + str(two_frame) + "," + str(one_frame) 
						stats += out

                                        	out = out.replace('\n',',').replace('\r',' ')
						print out.rstrip(',')
						out = " "

					elif int(first) < 0 or int(second) < 0:
					        out = "fail,"
                                        
				
					
						two_frame =  two_frame- int(third)
                                        	one_frame = one_frame - int(fourth)

						if two_frame<0:
                                                        two_frame *= -1
                                                elif one_frame<0:
                                                        one_frame *=-1


                                       		#out +=  first + "," + second + "," + str(two_frame) + "," + str(one_frame)
						if int(first) <= 41  and int(first) > 0  and int(second) < 0:	
							out += first + "," + "Sucess," + second + "," + "too fast," + str(two_frame) + "," +str(one_frame)
							stats += out

						elif int(second) <=19 and int(second) > 0 and int(first) < 0:
							out += first + "," + "too fast," + second+ "," + "Success," + str(two_frame) +"," + str(one_frame)

							stats += out

						else:
							out += first + "," + "too fast," + second + "," + "too fast," + str(two_frame) +","+ str(one_frame)
							stats += out

						
						out = out.replace('\n',',').replace('\r',' ')
						print out.rstrip(',')
				           	out = " "


					elif int(first) > 41 or int(second) > 19:
                                        	out = "block,"
                                        
						two_frame = two_frame - int(third)
						one_frame = one_frame - int(fourth)

						if two_frame<0:
							two_frame *= -1
						elif one_frame<0:
							one_frame *=-1

                                        	#out +=  first + ","  + second + "," + str(two_frame) + "," + str(one_frame)

						if int(first) <= 41  and int(first) > 0  and int(second) > 19:
                                                        out += first + "," + "Success," + second + "," + "too slow," + str(two_frame) + "," +str(one_frame)
							stats += out

                                                elif int(second) <= 19 and int(second) > 0 and int(first) > 41 :
                                                        out += first + "," + "too slow," + second+ "," + "Success," + str(two_frame) +"," + str(one_frame)
							stats += out

                                                else:
                                                        out += first + "," + "too slow," + second + "," + "too slow," + str(two_frame) +","+ str(one_frame)
							stats += out


						out = out.replace('\n',',').replace('\r',' ')

                                        	print out.rstrip(',')
						
                                        	out = " "
						#print stats


					cur2.execute(sqlInsert)
                                	db2.commit()


					count+=1
					#return stats
				
									
				except MySQLdb.Error as dbie:
					print dbie
					db2.rollback

			elif fifth == "cr_lp_s_lp_cr_oks":

                        	sqlInsert = 'INSERT INTO CR_LP_S_LP(CR_LP,S_LP,CR_LP_FRAMES,S_LP_FRAMES,TIMING,DATES) VALUES(%s,%s,%s,%s,CURTIME(),CURDATE())' %(first,second,third,fourth)
                        	try:
			
					out = " "

                                        two_frame = 2
                                        one_frame = 1

					
					if int(first)<= 61 and int(first) > 0:
                                                out = "succ,"

                                                two_frame = two_frame - float(third)
                                                one_frame = one_frame - float(fourth)

                                                out +=  first + "," + "N/A" + "," + str(two_frame) + "," + "N/A"

                                                out = out.replace('\n',',').replace('\r',' ')
                                                print out.rstrip(',')
                                                out = " "



					elif int(first) < 0:
                                                out = "fail,"

                                                #if int(first) > 0 :


                                                two_frame =  two_frame- float(third)
                                                one_frame = one_frame - float(fourth)

                                                out +=  first + "," + "N/A" + "," + str(two_frame) + "," + "N/A"
                                                

                                                out = out.replace('\n',',').replace('\r',' ')
                                                print out.rstrip(',')
                                                out = " "

					elif int(first) > 61:
                                                out = "block,"

                                                two_frame = two_frame - float(third)
                                                one_frame = one_frame - float(fourth)

                                                out +=  first + ","  + "N/A" + "," + str(two_frame) + "," + "N/A"

                                                

                                                out = out.replace('\n',',').replace('\r',' ')

                                                print out.rstrip(',')

                                                out = " "

	
					cur2.execute(sqlInsert)
                               		db2.commit()

                                	count+=1

                        

                        	except MySQLdb.Error as dbie:
                                	print dbie
 	                             	db2.rollback

#while True:
	#try_again = ser.read(3)
	#if try_again == "yes":
      		#count = 0
		#break
	

a = readlineCR(ser)
#while True:
        #try_again = ser.read(3)
        #if try_again == "yes":
                #count = 0
                #break

row1 = next(a)

row2 =  next(a)

row3 = next(a)

result = row1+row2+row3+"n"
print result

ser.write(result)
ser.flushOutput()
ser.flushInput()

reaction_record(0)
print "start"
count =0

#print stat
while True:

        try_again = ser.read(2)
	
	
	print try_again
	if try_again == 'hi':
		print "button"
	
        if try_again == "ye":
               	count = 0
		reaction_record(1)
	elif try_again == "no":
		print "no"
		#count =0 
		#sys.exit()
                #break





ser.close()

db.close()
db2.close()
