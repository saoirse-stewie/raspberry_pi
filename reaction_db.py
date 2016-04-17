import MySQLdb

db = MySQLdb.connect("localhost", "stewie3540" , "root", "reaction")

cursor = db.cursor()

cursor.execute("DROP TABLE IF EXISTS CR_MP_CR_MP_CR_HK")


sql = """CREATE TABLE  CR_MP_CR_MP_CR_HK(
	CR_MP FLOAT,
	CR_HK FLOAT,
	CR_MP_FRAMES INT,
	CR_HK_FRAMES INT,
	TIMING TIME,
	DATES DATE
	)"""

sql2 = """CREATE TABLE CR_LP_CR_HP_HU_HK(
	CR_LP FLOAT,
	CR_HP FLOAT,
	CR_LP_FRAMES INT,
	CR_HP_FRAMES INT,
	TIMING TIME,
	DATES DATE )"""
	
#try:	
cursor.execute(sql)
cursor.execute(sql2)
print "table successfully created"
#except:
#print "unable"

#sql_insert = """INSERT INTO  REACTIONTIME(CR_MP_CR_MP_CR_HK )VALUES(3.2)"""


#try:
#	cursor.execute(sql_insert)
#	db.commit()
#	print "successful commit"
#except:
#	db.rollback()
#	print "error inserting into database"	
	
db.close()



