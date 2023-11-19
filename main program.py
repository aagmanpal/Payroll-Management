import mysql.connector
import datetime

#Connecting mysql to python
connection = mysql.connector.connect(host='localhost',user='root',password='123')
cursor = connection.cursor()
#Creating a database
cursor.execute("CREATE DATABASE IF NOT EXISTS PAYROLL;")
cursor.execute("USE PAYROLL;")

#Login system
emp_credentials = []
admin_credentials = [['aagman','123'],['shivaansh','123']]
#login for employee
def emplogin():
    print("*"*70,"EMPLOYEE LOGIN","*"*70)
    while True:
        user = input("Username:")
        password = input("Password:")
        if user=='' or password=='':
            print("Fields cannot be empty!")
        elif [user,password] in emp_credentials:
            print(user,"Logged in Successfully!\n")
            main_emp()
            break
        else:
            print("Invalid! Please enter correct credentials!")
#login for admins
def adminlogin():
    print("*"*70,"ADMIN LOGIN","*"*70)
    while True:
        user = input("Username:")
        password = input("Password:")
        if user=='' or password=='':
            print("Fields cannot be empty!")
        elif [user,password] in admin_credentials:
            print(user,"Logged in Successfully!\n")
            main_admin()
            break
        else:
            print("Invalid! Please enter correct credentials!")
            

#Main program for Employee
def main_emp():
    print("*"*70,"Employee Window Panel","*"*70)

# Main Program for Admins
def main_admin():
    print("*"*70,"Admin Window Panel","*"*70)







while True:
    print("*"*70,"Select User Type","*"*70)
    print("1. Employee\n2. Admin")
    usertype=int(input("Enter choice:"))
    if usertype==1:
        emplogin()
        break
    elif usertype==2:
        adminlogin()
        break
    else:
        print("Please enter correct choice from above!!\n")
        pass
