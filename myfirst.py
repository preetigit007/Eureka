import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="preeti",passwd="1234",database="kapil")

mycursor=mydb.cursor()
mycursor.execute("select * from student")

result=mycursor.fetchone()
for i in mycursor:
	INSERT ("Priya","Po")
	print(i)