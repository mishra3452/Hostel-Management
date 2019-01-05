import mysql.connector as mariadb

def createTable():
	"This function will create a table named 'hostel' that will contains the information of students of a hostel"
	#Open database connection
	db = mariadb.connect(host='localhost',database='appin',user='root',password='mariadb')

	#Prepare a cursor object using cursor() method
	cursor = db.cursor()

	cursor.execute("drop table if exists employee")

	crtable = """create table hostel (sid int not null, first_name char(20) not null, last_name char(20), address char(100) not null, institute char(100) not null, age int, sex char(1),student_mobile long, parent_mobile long, rate long, ammount_paid long, ammount_due long, room_no char(10), other_charges long)"""

	#execute sql query crtable
	cursor.execute(crtable)

	#Disconnect from server
	db.close()

def insertTable(sid,first_name,last_name,address,institute,age,sex,student_mobile,parent_mobile,rate,ammount_paid,ammount_due,room_no,other_charges):
	"This method will insert data into the hostel table"
	#Open database connection
	db = mariadb.connect(host='localhost',database='appin',user='root',password='mariadb')

	#Prepare a cursor object using cursor() method
	cursor = db.cursor()
	
	instable = 'insert into hostel(sid,first_name,last_name,address,institute,age,sex,student_mobile,parent_mobile,rate,ammount_paid,ammount_due,room_no,other_charges) values ("%d","%s","%s","%s","%s","%d","%s","%d","%d","%d","%d","%d","%s","%d")'%(sid,first_name,last_name,address,institute,age,sex,student_mobile,parent_mobile,rate,ammount_paid,ammount_due,room_no,other_charges)

	try:
	
		#execute sql query instable
		cursor.execute(instable) 
		#Commit your changes in the database
		db.commit()
		print "Data Inserted"

	except:
		print "ERROR IN INSERTING DATA"
		#rollback in case there ia an error
		db.rollback()

	#Disconnect from server
	db.close()

def deleteData(sid):
	"This method will delete a row of the table whose sid = sid"
	#Open database connection
	db = mariadb.connect(host='localhost',database='appin',user='root',password='mariadb')

	#Prepare a cursor object using cursor() method
	cursor = db.cursor()
		
	delrow = "delete from hostel where sid='%d'"%(sid)

	try:

		#execute sql query instable
		cursor.execute(delrow)
	except:
		print "ERROR IN DELETING ROW" 

	#Disconnect from server
	db.close()

def showData():
	"This method will show data students"
	#Open database connection
	db = mariadb.connect(host='localhost',database='appin',user='root',password='mariadb')

	#Prepare a cursor object using cursor() method
	cursor = db.cursor()

	showdata = "select * from hostel"

	try:
		cursor.execute(showdata)
		results = cursor.fetchall()
		for row in results:
			sid = row[0]
			fname = row[1]
			lname = row[2]
			add = row[3]
			inst = row[4]
			age = row[5]
			sex = row[6]
			smobile = row[7]
			pmobile = row[8]
			rate = row[9]
			apaid = row[10]
			adue = row[11]
			rno = row[12]
			ocharges = row[13]
			print "sid=%d,fname=%s,lname=%s,add=%s,inst=%s,age=%d,sex=%s,smobile=%d,pmobile=%d,rate=%d,apaid=%d,adue=%d,rno=%s,ocharges=%d"%(sid,fname,lname,add,inst,age,sex,smobile,pmobile,rate,apaid,adue,rno,ocharges)
	except:
		print"Error: Unable to fetch data"
	

def updateData(sid):
	"This function will update a particular row where sid = sid"
	#Open database connection
	db = mariadb.connect(host='localhost',database='appin',user='root',password='mariadb')

	#Prepare a cursor object using cursor() method
	cursor = db.cursor()

	fname = raw_input("Enter First Name : ")
	lname  = raw_input("Enter Last Name : ")
	add = raw_input("Enter Address : ")
	inst = raw_input("Enter Institute : ")
	age = input("Enter Age : ")
	sex = raw_input("Enter Sex : ")
	smobile = input("Enter Student's Mobile Number : ")
	pmobile = input("Enter Parent's Mobile Number : ")
	rate = input("Enter Rate : ")
	apaid = input("Enter Paid Amount : ")
	adue = input("Enter Due Amount : ")
	rno = raw_input("Enter Room Number : ")
	ocharges = input("Enter Other Charges : ")

	updatedata = "update hostel set first_name=%s,last_name=%s,address=%s,institute=%s,age=%d,sex=%s,student_mobile=%d,parent_mobile=%d,rate=%d,amount_paid=%d,ammount_due=%d,room_no=%s,other_charges=%d where sid='%d'"%(fname,lname,add,inst,age,sex,smobile,pmobile,rate,apaid,adue,rno,ocharges)

	try:

		#execute sql query updatedata
		cursor.execute(updatedata)
	except:
		print "ERROR IN UPDATING ROW" 

	#Disconnect from server
	db.close()

def showDue(n):
	"This method will show the id, name and due amount of all student if n = 0 and  of particular student if n = some id"
	#Open database connection
	db = mariadb.connect(host='localhost',database='appin',user='root',password='mariadb')

	#Prepare a cursor object using cursor() method
	cursor = db.cursor()

	if(num != 0):
		showdata = "select id,first_name,last_name,due_ammount from hostel where sid='%d'"%(n)

		try:
			cursor.execute(showdata)
			results = cursor.fetchone()
			for row in results:
				sid = row[0]
				fname = row[1]
				lname = row[2]
				adue = row[11]
				print "sid=%d,fname=%s,lname=%s,adue=%d"%(sid,fname,lname,adue)
		except:
			print "Error: Unable to fetch due amount"
	else:
		showdata = "select id,first_name,last_name,due_ammount from hostel"

		try:
			cursor.execute(showdata)
			results = cursor.fetchall()
			for row in results:
				sid = row[0]
				fname = row[1]
				lname = row[2]
				adue = row[11]
				print "sid=%d,fname=%s,lname=%s,adue=%d"%(sid,fname,lname,adue)
		except:
			print "Error: Unable to fetch due amount"
