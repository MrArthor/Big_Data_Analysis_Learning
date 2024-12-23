import mysql.connector

# create a data base

db = mysql.connector.connect( host="localhost",  user="root",  passwd="admin1234")
# cursor object cur
cur = db.cursor()

# create database statement

cur.execute("CREATE DATABASE employee_db2")
# fetching all the databases
cur.execute("SHOW DATABASES")
for i in cur:
    print(i)
cur = db.cursor()

# create of table
db = mysql.connector.connect( host="localhost", user="root",  passwd="password", database="employee_db2")
cur = db.cursor()

# create statement for tblemployee
employeetbl_create = """CREATE TABLE `employee_db2`.`tblemployee` (`empid` INT NOT NULL AUTO_INCREMENT,  `empname` VARCHAR(45) NULL,`department` VARCHAR(45) NULL,  `salary` INT NULL, PRIMARY KEY (`empid`))"""
cur.execute(employeetbl_create)
cur= db.cursor()

# fetch tblemployee details in the database
cur.execute("desc tblemployee")
# print the table details
for i in cur:
    print(i)

############### insert multirow for tblemployee
employeetbl_insert = """INSERT INTO tblemployee (empname, department,salary)    VALUES  (%s, %s, %s)"""
# we save all the row data to be inserted in a data variable
data = [("Vani", "HR", "100000"), ("Krish", "Accounts", "60000"), ("Aishwarya", "Sales", "25000"),  ("Govind", "Marketing", "40000")]
# execute the insert commands for all rows and commit to the database
cur.executemany(employeetbl_insert, data)
db.commit()

#################### fetch data from the table
employeetbl_select = """SELECT * FROM tblemployee"""
# execute the select query to fetch all rows
cur.execute(employeetbl_select)
# fetch all the data returned by the database
employee_data = cur.fetchall()
# print all the data returned by the database
for e in employee_data:
    print(e)

##########update data from table

employeetbl_update = "UPDATE tblemployee SET salary = 115000 WHERE empid = 1"
# the salary of employee with
# employee id = 1 and commit to the database
cur.execute(employeetbl_update)
db.commit()

##################### delete statement for tblemployee

employeetbl_delete = "DELETE FROM tblemployee WHERE empid=3"
cur.execute(employeetbl_delete)
db.commit()
 
# closing the database connection
db.close()
