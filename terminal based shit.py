import mysql.connector
from tkinter import *
from tkinter import messagebox
import datetime

#Connecting mysql to python
connection = mysql.connector.connect(host='localhost',user='root',password='123')
cursor = connection.cursor()
#Creating a database
cursor.execute("CREATE DATABASE IF NOT EXISTS PAYROLL;")
cursor.execute("USE PAYROLL;")

#Login system
emp_credentials = [['aagman','pass'],['shivaansh','pass']]
admin_credentials = [['aagman','123'],['shivaansh','123']]
#login for employee
def emplogin():
    if usernameentry.get()=='' or passwordentry.get()=='':
         messagebox.showerror('Error','Fields cannot be empty!')
    elif [usernameentry.get(),passwordentry.get()] in emp_credentials:
        messagebox.showinfo('Success',"You've been logged in sucessfully!")
        root.destroy()
        print("Employee Logged In Successfully!\n")
        main_emp()
    else:
        messagebox.showerror('Incorrect details','Please enter correct credentials!')
#login for admins
def adminlogin():
    if usernameentry.get()=='' or passwordentry.get()=='':
         messagebox.showerror('Error','Fields cannot be empty!')
    elif [usernameentry.get(),passwordentry.get()] in admin_credentials:
        messagebox.showinfo('Success',"You've been logged in sucessfully!")
        root.destroy()
        print("Admin Logged In Successfully!\n")
        main_admin()
    else:
        messagebox.showerror('Incorrect details','Please enter correct credentials!')

#login for employee by pressing enter
def emplogin_enter(event):
    if event.state == 0 and event.keysym == "Return":
            emplogin()

#login for admin by pressing enter
def adminlogin_enter(event):
    if event.state == 0 and event.keysym == "Return":
            adminlogin()

#Main program for Employee
def main_emp():
    print("*"*70,"Employee Window Panel","*"*70)
    while True:
        print("1. See your Personal Information")
        print("2. ")

# Main Program for Admins
def main_admin():
    print("*"*70,"Admin Window Panel","*"*70)






#Program
while True:
    print("*"*70,"Select User Type","*"*70)
    print("1. Employee\n2. Admin")
    usertype=int(input("Enter choice:"))
    if usertype==1:
        root = Tk()
        root.geometry("626x417+400+150")
        root.resizable(False,False)
        root.title("Employee Login Page")
        root.attributes('-topmost',True)
        root.iconbitmap("assets/user.ico")
        loginframe = Frame(root)
        loginframe.place(x=70,y=40)

        logo = PhotoImage(file="assets/login logo.png")
        logolabel = Label(loginframe,image=logo)
        logolabel.grid(row=0,column=1)

        userimage = PhotoImage(file="assets/user.png")
        usernamelabel = Label(loginframe,image=userimage,text=" Username:",compound=LEFT,font=('times new roman',18,'bold'))
        usernamelabel.grid(row=1,column=0)
        usernameentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
        usernameentry.bind("<KeyPress>", emplogin_enter)
        usernameentry.grid(row=1,column=2)

        padlock = PhotoImage(file="assets/padlock.png")
        passwordlabel = Label(loginframe,image=padlock,text=" Password:",compound=LEFT,font=('times new roman',18,'bold'))
        passwordlabel.grid(row=2,column=0)
        passwordentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
        passwordentry.bind("<KeyPress>", emplogin_enter)
        passwordentry.grid(row=2,column=2)

        loginbutton = Button(loginframe,text='Login',font=('times new roman',14),width=12,bg='black',fg='white', border = 0, activebackground='black',activeforeground='white',cursor='hand2',command=emplogin)
        loginbutton.grid(row=3,column=1,pady=20)
        
        root.mainloop() 

        break
    elif usertype==2:
        root = Tk()
        root.geometry("626x417+400+150")
        root.resizable(False,False)
        root.title("Admin Login Page")
        root.iconbitmap("assets/user.ico")
        root.attributes('-topmost',True)
        loginframe = Frame(root)
        loginframe.place(x=70,y=40)

        logo = PhotoImage(file="assets/login logo.png")
        logolabel = Label(loginframe,image=logo)
        logolabel.grid(row=0,column=1)

        userimage = PhotoImage(file="assets/user.png")
        usernamelabel = Label(loginframe,image=userimage,text=" Username:",compound=LEFT,font=('times new roman',18,'bold'))
        usernamelabel.grid(row=1,column=0)
        usernameentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
        usernameentry.bind("<KeyPress>", adminlogin_enter)
        usernameentry.grid(row=1,column=2)

        padlock = PhotoImage(file="assets/padlock.png")
        passwordlabel = Label(loginframe,image=padlock,text=" Password:",compound=LEFT,font=('times new roman',18,'bold'))
        passwordlabel.grid(row=2,column=0)
        passwordentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
        passwordentry.bind("<KeyPress>", adminlogin_enter)
        passwordentry.grid(row=2,column=2)

        loginbutton = Button(loginframe,text='Login',font=('times new roman',14),width=12,bg='black',fg='white', border = 0, activebackground='black',activeforeground='white',cursor='hand2',command=adminlogin)
        loginbutton.grid(row=3,column=1,pady=20)
        
        root.mainloop() 

        break
    else:
        print("Please enter correct choice from above!!\n")
        pass
