#use admin username as "admin" and admin password as "password"
#frist you have to start mariab by running command "systemctl start mariadb"
 
import HostelManagementDatabase
import os


adminusername = "admin"
adminpassword = "password"
rent = 0
mainchoice = 'y'
while(mainchoice == 'y'):
	print "HOSTEL MANAGEMENT".center(50,'*')
	print ""
	print ""
	print "Identify Yourself".center(50)
	print "(1). Admin"
	print "(2). Exit"
	print ""
	print ""
	choice = input("Please Enter your choice : ")
	if(choice == 1):
		os.system('cls' if os.name == 'nt' else 'clear')
		print "Admin Login".center(50,'*')
		subchoice = 'y'
		username = raw_input("Enter your username : ")
		password = raw_input("Enter your password : ")
		if(username == adminusername and password == adminpassword):
			while(subchoice == 'y'):	
				print "Welcome Admin".center(50,'*')
				print "(1). Add Rent"
				print "(2). Add Student"
				print "(3). Find status of due amount"
				print "(4). Find status of due amount of particular student"
				print "(5). Check incoming and outgoing of students from hostel"
				print "(6). Update the details of student"
				print "(7). View Details of Student"
				print "(8). Delete student details"
				print "(9). Logout"
				print ""
				print ""
				adminchoice = input("Enter your choice : ")
				if(adminchoice == 1):
					rent = input("Enter the rent amount of your hostel(per month) : Rs.")
				elif(adminchoice == 2):
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Add Student".center(50,'*')
					print ""
					print ""
					sid = input("Enter Student id : ")
					first_name = raw_input("Enter first name of the student : ")
					last_name = raw_input("Enter last name of the student : ")
					address = raw_input("Enter address of the student : ")
					institute = raw_input("Enter institute of the student : ")
					age = input("Enter age of the student : ")
					sex = raw_input("Enter sex of the student : ")
					student_mobile = input("Enter student's mobile number : ")
					parent_mobile = input("Enter parent's mobile number : ")
					rate = input("Enter rate of the room : ")
					ammount_paid = input("Enter amount paid by the student : ")
					ammount_due = rate-ammount_paid;
					room_no = raw_input("Enter room number alloted to the student :")
					other_charges = input("Enter other charges if applicable : ")

					HostelManagementDatabase.insertTable(sid,first_name,last_name,address,institute,age,sex,student_mobile,parent_mobile,rate,ammount_paid,ammount_due,room_no,other_charges)
				elif(adminchoice == 3):
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Status of due amount".center(50,'*')
					print ""
					print ""
					HostelManagementDatabase.showDue(0);
				elif(adminchoice == 4):
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Status of due amount of particular student".center(50,'*')
					print ""
					print ""
					sid = input("Enter id of student : ")
					HostelManagementDatabase.showDue(sid)
				elif(adminchoice == 5):
					os.system('cls' if os.name == 'nt' else 'clear')					
					print "Incoming and outgoing of student".center(50,'*')
					print ""
					print ""
					sid = input("Enter id of student : ")
					HostelManagementDatabase.showInOut(sid)
				elif(adminchoice == 6):
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Update details of student".center(50,'*')
					print ""
					print ""
					sid = input("Enter id of the student : ")
					HostelManagementDatabase.updateData(sid)
				elif(adminchoice == 7):
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Student Details".center(50,'*')
					print ""
					print ""
					HostelManagementDatabase.showData()
				elif(adminchoice == 8):
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Delete Records".center(50,'*')
					print ""
					print ""
					sid = input("Enter id of the student to delete : ")
					HostelManagementDatabase.deleteData(sid)
				else:
					os.system('cls' if os.name == 'nt' else 'clear')
					print "Thank you!"
					subchoice = 'n'
		else:
			print "Wrong Credentials"
	elif(choice == 2):
		mainchoice = 'n'
		print "Thank you!"
