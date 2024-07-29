from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
import mysql.connector
from datetime import datetime
import math
import random
from modules import payreceipt

#Establishing a connection in Mysql
connection = mysql.connector.connect(host='localhost',user='root',passwd='123')
cursor = connection.cursor()

cursor.execute('CREATE DATABASE IF NOT EXISTS PMS;')
cursor.execute('USE PMS;')

#Creating table for login details
cursor.execute("CREATE TABLE IF NOT EXISTS ADMIN_CREDENTIALS (Username varchar(20) not null,Password varchar(20) not null);")

#Adding default login details to table
cursor.execute("Select * from ADMIN_CREDENTIALS WHERE username='shivaansh';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO ADMIN_CREDENTIALS VALUES ('shivaansh','123');")

cursor.execute("Select * from ADMIN_CREDENTIALS WHERE username='aagman';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO ADMIN_CREDENTIALS VALUES ('aagman','123');")

cursor.execute("Select * from ADMIN_CREDENTIALS WHERE username='pranjal';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO ADMIN_CREDENTIALS VALUES ('pranjal','123');")

cursor.execute("Select * from admin_credentials;")
admins = cursor.fetchall()

#Creating table for emp details
cursor.execute("CREATE TABLE IF NOT EXISTS EMP_DETAILS (EMP_ID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,NAME VARCHAR(50) NOT NULL,DESIGNATION VARCHAR(30) NOT NULL,SALARY INT NOT NULL, AGE INT NOT NULL,GENDER TEXT NOT NULL,EMAIL varchar(40) NOT NULL,DOB DATE NOT NULL,DOJ DATE NOT NULL,ACCOUNT_NO VARCHAR(15) NOT NULL,CONTACT_NO VARCHAR(14) NOT NULL,ADDRESS VARCHAR(50) NOT NULL);")

#Adding default employees to table
cursor.execute("Select * from EMP_DETAILS WHERE NAME='Shivaansh';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO EMP_DETAILS VALUES (1,'Shivaansh','Admin',80000,17,'Male','kanchanshivaansh2006@gmail.com','2006-01-02','2023-12-07','987654321','8471064398','Nawab Yusuf Road, Prayagraj');") 
    connection.commit()

cursor.execute("Select * from EMP_DETAILS WHERE NAME='Aagman';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO EMP_DETAILS VALUES (2,'Aagman','Admin',80000,17,'Male','aagmanpal@gmail.com','2006-06-13','2023-01-12','123456789','7843819008','Sulem Sarai, Prayagraj');") 
    connection.commit()

cursor.execute("Select * from EMP_DETAILS WHERE NAME='Pranjal';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO EMP_DETAILS VALUES (3,'Pranjal','Admin',80000,17,'Male','pranjalsandilya@gmail.com','2006-09-14','2023-01-12','123456789','8459753183','Jhusi, Prayagraj');") 
    connection.commit()   

#Creating table for loans
cursor.execute("CREATE TABLE IF NOT EXISTS EMP_LOANS(EMP_ID INT NOT NULL PRIMARY KEY,LOAN INT(10) NOT NULL,INTEREST INT(3) NOT NULL,LOAN_DATE DATE,REPAYMENT_TIME INT NOT NULL);")

#Adding default loan details to table
cursor.execute("Select * from EMP_LOANS WHERE EMP_ID='1';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO EMP_LOANS VALUES (1,0,0,NULL,0);")

cursor.execute("Select * from EMP_LOANS WHERE EMP_ID='2';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO EMP_LOANS VALUES (2,0,0,NULL,0);")

cursor.execute("Select * from EMP_LOANS WHERE EMP_ID='3';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute("INSERT INTO EMP_LOANS VALUES (3,0,0,NULL,0);")

#Creating table for bonus, fines etc
cursor.execute("CREATE TABLE IF NOT EXISTS EMP_EXTRA(EMP_ID INT NOT NULL PRIMARY KEY,BONUS INT,OTHER_GAIN INT,FINES INT,OTHER_DED INT,MOP VARCHAR(20),NOTE VARCHAR(100),BONUS_MONTH DATE);")

#Adding default bonus,fines etc details to table
cursor.execute("SELECT CURDATE()")
curdate = str(cursor.fetchone()[0])
cursor.execute("Select * from EMP_EXTRA WHERE EMP_ID='1';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute(f"INSERT INTO EMP_EXTRA VALUES (1,0,0,0,0,'Net Banking','N/A','{curdate}');") 

cursor.execute("Select * from EMP_EXTRA WHERE EMP_ID='2';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute(f"INSERT INTO EMP_EXTRA VALUES (2,0,0,0,0,'Net Banking','N/A','{curdate}');")

cursor.execute("Select * from EMP_EXTRA WHERE EMP_ID='3';")
flag = cursor.fetchone()

if flag == None:
    cursor.execute(f"INSERT INTO EMP_EXTRA VALUES (3,0,0,0,0,'Net Banking','N/A','{curdate}');") 


#Defining functions

def adminmain():
    window=Tk()
    window.title('Employee Management')
    window.geometry('1200x640+150+60')
    window.minsize(1200,640)
    window.resizable(False,False)
    window.iconbitmap("Payroll-Management-main/assets/salary.ico")
    window.configure(bg='#41b3a3')

    #Header Frame
    header_frame = Frame(window,bg='#41b3a3', height=60, width = 1280)
    header_frame.place(x=0,y=0)
    header_image=PhotoImage(file='Payroll-Management-main/assets/salary.png')
    header_text=Label(header_frame,image=header_image,text='  EMPLOYEE MANAGEMENT',font=('Adobe Garamond Pro',28,'bold'),compound=LEFT,fg='white',bg='#41b3a3')
    header_text.place(x=355,y=3)
    
    #Right Frame
    rightframe = Frame(window,bg='white')
    rightframe.place(x=350,y=110,width=840,height=508)
    rightframe_header = Frame(window, border = 2,background='burlywood1',relief=SOLID)
    rightframe_header.place(x=350,y=60,width=840,height=50)
    label = Label(rightframe_header,font=('times',20),bg='burlywood1')
    label.pack(expand=True)

    #Menu Panel Frame
    left_frame = Frame(window, bg='#41b3a3')
    left_frame.columnconfigure(0, weight = 1)
    left_frame.rowconfigure(0, weight = 1)
    left_frame.rowconfigure(1, weight = 1)
    left_frame.rowconfigure(2, weight = 1)
    left_frame.rowconfigure(3, weight = 1)
    left_frame.rowconfigure(4, weight = 1)
    left_frame.rowconfigure(5, weight = 1)
    left_frame.rowconfigure(6, weight = 1)
    left_frame.rowconfigure(7, weight = 1)
    left_frame.rowconfigure(8, weight = 1)
    left_frame.rowconfigure(9, weight = 1)
    left_frame.rowconfigure(10, weight = 1)
    left_frame.place(x=0,y=60,width=350,height=558)
    
    #Button Active Function
    def activebtn(n: int):
        btn1.config(bg='#E6DDC4')
        btn2.config(bg='#E6DDC4')
        btn3.config(bg='#E6DDC4')
        btn4.config(bg='#E6DDC4')
        btn5.config(bg='#E6DDC4')
        btn6.config(bg='#E6DDC4')
        btn7.config(bg='#E6DDC4')
        btn8.config(bg='#E6DDC4')

        if n==1:
            btn1.config(bg='gold',fg='black')
        elif n==2:
            btn2.config(bg='gold',fg='black')
        elif n==3:
            btn3.config(bg='gold',fg='black')
        elif n==4:
            btn4.config(bg='gold',fg='black')
        elif n==5:
            btn5.config(bg='gold',fg='black')
        elif n==6:
            btn6.config(bg='gold',fg='black')
        elif n==7:
            btn7.config(bg='gold',fg='black')
        elif n==8:
            btn8.config(bg='gold',fg='black')
    
    #Defining Menu btn functions
    def addemp():
        rightframe.destroy()
        label.config(text='Add Employee Record...')
        activebtn(1)
        addemp_frame = Frame(window,bg='#F9E8D9')
        addemp_frame.columnconfigure(0, weight = 1)
        addemp_frame.columnconfigure(1, weight = 1)
        addemp_frame.columnconfigure(2, weight = 1)
        addemp_frame.columnconfigure(3, weight = 1)
        addemp_frame.rowconfigure(0, weight = 1)
        addemp_frame.rowconfigure(1, weight = 1)
        addemp_frame.rowconfigure(2, weight = 1)
        addemp_frame.rowconfigure(3, weight = 1)
        addemp_frame.rowconfigure(4, weight = 1)
        addemp_frame.rowconfigure(5, weight = 1)
        addemp_frame.rowconfigure(6, weight = 1)
        addemp_frame.rowconfigure(7, weight = 1)
        addemp_frame.place(x=350,y=110,width=840,height=508)
        #Employee Details Variable
        emp_id = StringVar()
        emp_name = StringVar()
        emp_desig = StringVar()
        emp_salary = StringVar()
        emp_age = StringVar()
        emp_gender = StringVar()
        emp_gender.set('Select')
        emp_email = StringVar()
        emp_dob = StringVar()
        emp_doj = StringVar()
        emp_accno = StringVar()
        emp_contact = StringVar()
        emp_add = StringVar()
        #Details of Employess to Add
        text1 = Label(addemp_frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text1.grid(column=0,row=0)
        text2 = Label(addemp_frame,text='Employee Name:',font=('times new roman',16),bg='#F9E8D9')
        text2.grid(column=0,row=1)
        text3 = Label(addemp_frame,text='Designation:',font=('times new roman',16),bg='#F9E8D9')
        text3.grid(column=0,row=2)
        text4 = Label(addemp_frame,text='Salary(in ₹):',font=('times new roman',16),bg='#F9E8D9')
        text4.grid(column=0,row=3)
        text5 = Label(addemp_frame,text='Age:',font=('times new roman',16),bg='#F9E8D9')
        text5.grid(column=0,row=4)
        text6 = Label(addemp_frame,text='Gender:',font=('times new roman',16),bg='#F9E8D9')
        text6.grid(column=0,row=5)
        text7 = Label(addemp_frame,text='Email:',font=('times new roman',16),bg='#F9E8D9')
        text7.grid(column=2,row=0)
        text8 = Label(addemp_frame,text='D.O.B:',font=('times new roman',16),bg='#F9E8D9')
        text8.grid(column=2,row=1)
        text9 = Label(addemp_frame,text='D.O.J:',font=('times new roman',16),bg='#F9E8D9')
        text9.grid(column=2,row=2)
        text10 = Label(addemp_frame,text='Acc No.:',font=('times new roman',16),bg='#F9E8D9')
        text10.grid(column=2,row=3)
        text11 = Label(addemp_frame,text='Contact No.:',font=('times new roman',16),bg='#F9E8D9')
        text11.grid(column=2,row=4)
        text12 = Label(addemp_frame,text='Address:',font=('times new roman',16),bg='#F9E8D9')
        text12.grid(column=0,row=6)
        #Respective Entry Fields
        entry1 = Entry(addemp_frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry1.grid(column=1,row=0)
        entry2 = Entry(addemp_frame, textvariable=emp_name ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry2.grid(column=1,row=1)
        entry3 = Entry(addemp_frame, textvariable=emp_desig ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry3.grid(column=1,row=2)
        entry4 = Entry(addemp_frame, textvariable=emp_salary ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry4.grid(column=1,row=3)
        entry5 = Entry(addemp_frame, textvariable=emp_age ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry5.grid(column=1,row=4)
        entry6 = OptionMenu(addemp_frame, emp_gender ,'Male','Female')
        entry6.config(bg='lightyellow')
        entry6['menu'].config(bg='lightyellow')
        entry6.grid(column=1,row=5,sticky= E + W,padx=10)
        entry7 = Entry(addemp_frame, textvariable=emp_email ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry7.grid(column=3,row=0)
        entry8 = DateEntry(addemp_frame, textvariable=emp_dob ,bg='lightyellow',bd=3,font=('Times new roman',16),date_pattern='dd/MM/yyyy')
        entry8.grid(column=3,row=1)
        entry9 = DateEntry(addemp_frame, textvariable=emp_doj ,bg='lightyellow',bd=3,font=('Times new roman',16),date_pattern='dd/MM/yyyy')
        entry9.grid(column=3,row=2)
        entry10 = Entry(addemp_frame, textvariable=emp_accno ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry10.grid(column=3,row=3)
        entry11 = Entry(addemp_frame, textvariable=emp_contact ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry11.grid(column=3,row=4)
        entry12 = Entry(addemp_frame, textvariable=emp_add ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry12.grid(column=1,row=6,columnspan=3,sticky= E + W,padx=10)
        
        #Add Employee Button Function
        def saveemp():
            try:
                if emp_id.get()=='':
                    messagebox.showerror("Error","Please Enter All Details first!!!")
                else:
                    cursor.execute("SELECT * FROM EMP_DETAILS WHERE EMP_ID=%s;"%(emp_id.get()))
                    row = cursor.fetchone()
                    if emp_gender.get()=='Select':
                        emp_gender.set('')
                    if row!=None:
                        messagebox.showerror("Error",f"This Employee ID is already in Record!\nEmployee Name:{row[1]}")
                    elif emp_desig.get().upper() == "ADMIN":
                        messagebox.showerror("Error","Admins cannot add other admins.")
                    elif (emp_id.get()=='') or (emp_name.get()=='') or (emp_desig.get()=='') or (emp_salary.get()=='') or (emp_age.get()=='') or (emp_gender.get()=='') or (emp_email.get()=='') or (emp_dob.get()=='') or (emp_doj.get()=='') or (emp_accno.get()=='') or (emp_contact.get()=='') or (emp_add.get()==''):
                        messagebox.showerror("Empty Field","Please fill all the details first and then click on add employee button!")
                        if emp_gender.get()=='':
                            emp_gender.set('Select')
                    else:
                        #changing date format so that it can be uploaded to mysql database
                        dob_str = entry8.get()
                        dob_obj = datetime.strptime(dob_str, '%d/%m/%Y')
                        dob = dob_obj.strftime('%Y-%m-%d')
                        doj_str = entry9.get()
                        doj_obj = datetime.strptime(doj_str, '%d/%m/%Y')
                        doj = doj_obj.strftime('%Y-%m-%d')
                        
                        cursor.execute(f"INSERT INTO EMP_DETAILS VALUES ({emp_id.get()},'{emp_name.get()}','{emp_desig.get()}',{int(emp_salary.get())},{int(emp_age.get())},'{emp_gender.get()}','{emp_email.get()}','{dob}','{doj}','{emp_accno.get()}','{str(emp_contact.get())}','{emp_add.get()}');")
                        cursor.execute(f"INSERT INTO EMP_LOANS VALUES({emp_id.get()},0,0,NULL,0);")
                        cursor.execute(f"INSERT INTO EMP_EXTRA VALUES({emp_id.get()},0,0,0,0,'Net Banking','N/A','{doj}');")
                        connection.commit()
                        messagebox.showinfo("Added :)","Employee Added Successfully...")
                        addemp()
            except Exception as ex:
                messagebox.showerror("Error",f"Error due to: {str(ex)}")
        #Buttons in Add Employee
        
        def on_enter_addemp(e):
            button1.config(bg='#01d449',fg='black')

        def on_leave_addemp(e):
            button1.config(bg='white',fg='#01d449')

        button1 = Button(addemp_frame,text='Add Employee',command=saveemp,bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        button1.bind("<Enter>",on_enter_addemp)
        button1.bind("<Leave>",on_leave_addemp)
        button1.grid(row=7,column=0,columnspan=4,sticky=N,pady=5)

    def manage_loans():
        rightframe.destroy()
        btn4frame = Frame(window,bg='#F9E8D9')
        label.config(text='Manage Loans...')
        activebtn(2)

        btn4frame.columnconfigure(0, weight = 1)
        btn4frame.columnconfigure(1, weight = 1)
        btn4frame.columnconfigure(2, weight = 1)
        btn4frame.columnconfigure(3, weight = 1)

        btn4frame.rowconfigure(0, weight = 1)
        btn4frame.rowconfigure(1, weight = 1)
        #Added extra rows and columns to adjust positioning.
        btn4frame.rowconfigure(2, weight = 1)
        btn4frame.rowconfigure(3, weight = 1)
        btn4frame.rowconfigure(4, weight = 1)
        btn4frame.rowconfigure(5, weight = 1)
        btn4frame.rowconfigure(6, weight = 1)
        btn4frame.rowconfigure(7, weight = 1)

        btn4frame.place(x=350,y=110,width=840,height=508)

        emp_id = StringVar()

        text1 = Label(btn4frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text1.grid(column=0,row=0)

        entry1 = Entry(btn4frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry1.grid(column=1,row=0)

        def on_enter_showrecemp(e):
            search_btn.config(bg='#01d449',fg='black')
            
        def on_leave_showrecemp(e):
            search_btn.config(bg='white',fg='#01d449')

        def emp_loan():
            empid = emp_id.get()

            if empid == "":
                messagebox.showerror("Empty Field", "Please enter the required data.")
            elif empid.isnumeric() != True:
                messagebox.showerror("Error", "Please enter a valid ID.")
            else:             
                cursor.execute(f"SELECT * FROM EMP_LOANS WHERE EMP_ID = {empid}")
                details = cursor.fetchone()
                
                if details == None:
                    messagebox.showerror("Error", f"No Employee with ID:{empid} exists.")
                else:

                    text1.destroy()
                    entry1.destroy()
                    search_btn.destroy()

                    if details[1] == 0:
                        text2 = Label(btn4frame,text=f'This employee (ID = {empid}) has no loans.',font=('times new roman',16),bg='#F9E8D9')
                        text2.grid(column=0,row=0)
                        
                        def on_enter_showrecemp1(e):
                            addloan.config(bg='#01d449',fg='black')
                    
                        def on_leave_showrecemp1(e):
                            addloan.config(bg='white',fg='#01d449')

                        def on_enter_showrecemp2(e):
                            back.config(bg='#01d449',fg='black')
                    
                        def on_leave_showrecemp2(e):
                            back.config(bg='white',fg='#01d449')

                        def add_loan():
                            text2.destroy()
                            addloan.destroy()
                            back.destroy()

                            text3 = Label(btn4frame,text='Amount(in ₹):',font=('times new roman',16),bg='#F9E8D9')
                            text3.grid(column=0,row=0,)
                            text4 = Label(btn4frame,text='Interest(% per month):',font=('times new roman',16),bg='#F9E8D9')
                            text4.grid(column=0,row=1)
                            text5 = Label(btn4frame,text='Repayment Time(in Years):',font=('times new roman',16),bg='#F9E8D9')
                            text5.grid(column=0,row=2)

                            entry1 = Entry(btn4frame ,bg='lightyellow',bd=3,font=('Times new roman',16))
                            entry1.grid(column=1,row=0)
                            entry2 = Entry(btn4frame, bg='lightyellow',bd=3,font=('Times new roman',16))
                            entry2.grid(column=1,row=1)
                            entry3 = Entry(btn4frame, bg='lightyellow',bd=3,font=('Times new roman',16))
                            entry3.grid(column=1,row=2)

                            def on_enter_showrecemp3(e):
                                updateloan.config(bg='#01d449',fg='black')
                    
                            def on_leave_showrecemp3(e):
                                updateloan.config(bg='white',fg='#01d449')

                            def update_loan():
                                amt = entry1.get()
                                interest = entry2.get()
                                repay_time = entry3.get()

                                cursor.execute(f"SELECT * FROM EMP_LOANS WHERE EMP_ID = {empid}")
                                details = cursor.fetchone()

                                if amt == "" or interest == "" or repay_time == "":
                                    messagebox.showerror("Empty Field", "Please fill all the details.")
                                elif amt.isnumeric() != True or interest.isnumeric() != True or repay_time.isnumeric() != True:
                                    messagebox.showerror("Error", "Please enter valid data.")
                                
                                else:
                                    cursor.execute("SELECT CURDATE();")
                                    date = cursor.fetchone()[0]
                                    cursor.execute(f"UPDATE EMP_LOANS SET LOAN = {int(amt)}, INTEREST = {int(interest)}, LOAN_DATE = '{str(date)}', REPAYMENT_TIME = {int(repay_time)} WHERE EMP_ID = {empid};")
                                    connection.commit()
                                    cursor.execute(f"SELECT * FROM EMP_LOANS WHERE EMP_ID = {empid}")
                                    details = cursor.fetchone()
                                    messagebox.showinfo("Loan added", f"A loan of details:\nAmount: {details[1]}\nInterest: {details[2]}\nDate of Loan: {str(details[3])[-2]}{str(details[3])[-1]}/{str(details[3])[-5]}{str(details[3])[-4]}/{str(details[3])[-10]}{str(details[3])[-9]}{str(details[3])[-8]}{str(details[3])[-7]}\nRepayment time: {details[4]}\nhas been successfully added to Employee ID:{empid}.")   
                                    manage_loans()                       

                            updateloan = Button(btn4frame,text='Add a Loan',command = update_loan, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                            updateloan.bind("<Enter>",on_enter_showrecemp3)
                            updateloan.bind("<Leave>",on_leave_showrecemp3)
                            updateloan.grid(row=7,column=0,columnspan=4,sticky=N,pady=5)

                        addloan = Button(btn4frame,text='Add a Loan',command = add_loan, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                        addloan.bind("<Enter>",on_enter_showrecemp1)
                        addloan.bind("<Leave>",on_leave_showrecemp1)
                        addloan.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)

                        back = Button(btn4frame,text='Back',command = manage_loans, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                        back.bind("<Enter>",on_enter_showrecemp2)
                        back.bind("<Leave>",on_leave_showrecemp2)
                        back.grid(row=2,column=0,columnspan=4,sticky=N,pady=0)

                    elif details[1] != 0:
                        text2 = Label(btn4frame,text=f'This employee (ID = {empid}) already has a loans.',font=('times new roman',16),bg='#F9E8D9')
                        text2.grid(column=0,row=0)

                        def on_enter_showrecemp1(e):
                            removeloan.config(bg='#01d449',fg='black')
                    
                        def on_leave_showrecemp1(e):
                            removeloan.config(bg='white',fg='#01d449')

                        def on_enter_showrecemp2(e):
                            back.config(bg='#01d449',fg='black')
                    
                        def on_leave_showrecemp2(e):
                            back.config(bg='white',fg='#01d449')

                        def remove_loan():
                            messagebox.showinfo("Loan Removed", f"A loan of details:\nAmount: {details[1]}\nInterest: {details[2]}\nDate of Loan: {str(details[3])[-2]}{str(details[3])[-1]}/{str(details[3])[-5]}{str(details[3])[-4]}/{str(details[3])[-10]}{str(details[3])[-9]}{str(details[3])[-8]}{str(details[3])[-7]}\nRepayment time: {details[4]}\nhas been successfully removed from Employee ID:{empid}.")
                            cursor.execute(f"UPDATE EMP_LOANS SET LOAN = 0, INTEREST = 0, LOAN_DATE = NULL, REPAYMENT_TIME  = 0 WHERE EMP_ID = {empid};")
                            connection.commit()
                            manage_loans()

                        removeloan = Button(btn4frame,text='Remove a Loan',command = remove_loan, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                        removeloan.bind("<Enter>",on_enter_showrecemp1)
                        removeloan.bind("<Leave>",on_leave_showrecemp1)
                        removeloan.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)

                        back = Button(btn4frame,text='Back',command = manage_loans, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                        back.bind("<Enter>",on_enter_showrecemp2)
                        back.bind("<Leave>",on_leave_showrecemp2)
                        back.grid(row=2,column=0,columnspan=4,sticky=N,pady=0)

        search_btn = Button(btn4frame,text='Show Loans',command = emp_loan, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        search_btn.bind("<Enter>",on_enter_showrecemp)
        search_btn.bind("<Leave>",on_leave_showrecemp)
        search_btn.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)
        
    def allemp_rec():
        rightframe.destroy()

        btn3frame = Frame(window,bg='#F9E8D9')
        btn3frame.place(x=350,y=110,width=840,height=508)

        label.config(text='Records of all Employee...')
        activebtn(3)

        style=ttk.Style()
        style.theme_use('clam')

        tree = ttk.Treeview(btn3frame,columns=('id','name','desig','salary','age','gender','email','dob','doj','accno','contact','add',"loan","interest","loan_date","repayment_time","bonus","other_gain","fine","other_ded","mop","note"),show='headings',height=10,)
        tree.pack(fill='both',expand=True)
        tree.column('id',anchor='center')
        tree.heading('id',text='Employee ID')
        tree.column('name',anchor='center')
        tree.heading('name',text='NAME')
        tree.column('desig',anchor='center')
        tree.heading('desig',text='DESIGNATION')
        tree.column('salary',anchor='center')
        tree.heading('salary',text='SALARY(in ₹)')
        tree.column('age',anchor='center')
        tree.heading('age',text='AGE')
        tree.column('gender',anchor='center')
        tree.heading('gender',text='GENDER')
        tree.column('email',anchor='center')
        tree.heading('email',text='EMAIL')
        tree.column('dob',anchor='center')
        tree.heading('dob',text='D.O.B')
        tree.column('doj',anchor='center')
        tree.heading('doj',text='D.O.J')
        tree.column('accno',anchor='center')
        tree.heading('accno',text='ACCOUNT NO.')
        tree.column('contact',anchor='center')
        tree.heading('contact',text='CONTACT NO.')
        tree.column('add',anchor='center')
        tree.heading('add',text='ADDRESS')
        tree.column('loan',anchor='center')
        tree.heading('loan',text='LOANS(in ₹)')
        tree.column('interest',anchor='center')
        tree.heading('interest',text='INTEREST(%)')
        tree.column('loan_date',anchor='center')
        tree.heading('loan_date',text='DATE OF LOAN')
        tree.column('repayment_time',anchor='center')
        tree.heading('repayment_time',text='REPAYMENT TIME(in Years)')
        tree.column('bonus',anchor='center')
        tree.heading('bonus',text='BONUS(in ₹)')
        tree.column('other_gain',anchor='center')
        tree.heading('other_gain',text='OTHER GAINS(in ₹)')
        tree.column('fine',anchor='center')
        tree.heading('fine',text='FINES(in ₹)')
        tree.column('other_ded',anchor='center')
        tree.heading('other_ded',text='OTHER DEDUCTIONS(in ₹)')
        tree.column('mop',anchor='center')
        tree.heading('mop',text='MODE OF PAYMENT')
        tree.column('note',anchor='center')
        tree.heading('note',text='NOTE')
        
        hor_scrollbar = ttk.Scrollbar(btn3frame,orient='horizontal',command=tree.xview)
        tree.configure(xscrollcommand=hor_scrollbar.set)
        hor_scrollbar.pack(side='bottom',fill='x')

        cursor.execute("SELECT * FROM EMP_DETAILS;")
        details = cursor.fetchall()
        cursor.execute("SELECT * FROM EMP_LOANS;")
        loan_details = cursor.fetchall()
        cursor.execute("SELECT * FROM EMP_EXTRA;")
        extra_details = cursor.fetchall()

        if len(details) != 0:
            for i in range(0, len(details)):
                lis = list(details[i])
                loan_lis = list(loan_details[i])
                extra_lis = list(extra_details[i])

                date = ""
                for j in str(lis[7]):
                    if j == "-":
                        date += "/"
                    else:
                        date += j
                lis[7] = date[-2] + date[-1] + date[-3] + date[-5] + date[-4] + date[-6] + date[-10] + date[-9] + date[-8] + date[-7]

                date = ""
                for j in str(lis[8]):
                    if j == "-":
                        date += "/"
                    else:
                        date += j
                lis[8] = date[-2] + date[-1] + date[-3] + date[-5] + date[-4] + date[-6] + date[-10] + date[-9] + date[-8] + date[-7]

                if loan_lis[-1] == 0:
                    loan_lis[-1] = "-"
                else:
                    cursor.execute("SELECT CURDATE()")
                    curdate = cursor.fetchone()[0]
                    cursor.execute(f"SELECT DATEDIFF(CURRENT_DATE, '{loan_lis[-2]}');")
                    days = int(cursor.fetchone()[0])

                    if int(str(curdate)[:4]) % 4 == 0:
                        time_left = loan_lis[-1] - (days/366)
                        loan_lis[-1] = f"{math.modf(time_left)[1]} years, {math.modf(time_left)[0] * 366} days"
                        if math.modf(time_left)[1] == 0 and math.modf(time_left)[0] * 366 == 0:
                            loan_lis[-1] = "-"
                            cursor.execute(f"UPDATE EMP_LOANS SET LOAN = 0, INTEREST = 0, LOAN_DATE = NULL, REPAYMENT_TIME = 0 WHERE EMPID = {lis[0]};")
                            connection.commit()
                    else:
                        time_left = loan_lis[-1] - (days/365)
                        loan_lis[-1] = f"{math.modf(time_left)[1]} years, {math.modf(time_left)[0] * 365} days" 

                        if math.modf(time_left)[1] == 0 and math.modf(time_left)[0] * 365 == 0:
                            loan_lis[-1] = "-"
                            cursor.execute(f"UPDATE EMP_LOANS SET LOAN = 0, INTEREST = 0, LOAN_DATE = NULL, REPAYMENT_TIME = 0 WHERE EMPID = {lis[0]};")
                            connection.commit()

                if loan_lis[-2] == None:
                    loan_lis[-2] = "-"
                else:
                    date = ""
                    for j in str(loan_lis[-2]):
                        if j == "-":
                            date += "/"
                        else:
                            date += j
                    loan_lis[-2] = date[-2] + date[-1] + date[-3] + date[-5] + date[-4] + date[-6] + date[-10] + date[-9] + date[-8] + date[-7]

                if float(loan_lis[-3]) == 0:
                    loan_lis[-3] = "-"

                if float(loan_lis[-4]) == 0:
                    loan_lis[-4] = "-"
                    loan_lis.append("-")

                cursor.execute("SELECT CURDATE()")
                curdate = str(cursor.fetchone()[0])

                bonus_date = str(extra_lis[-1])[0:8] + "01"

                cursor.execute(f"SELECT DATEDIFF('{bonus_date}', CURDATE())")
                date_diff = int(cursor.fetchone()[0])

                if bonus_date[6:8] in ["01","03","05","07","08","10","12"]:
                    if date_diff > 31:
                        cursor.execute(f"UPDATE EMP_EXTRA SET BONUS = 0, OTHER_GAIN = 0, FINES = 0, OTHER_DED = 0, BONUS_MONTH = {curdate} WHERE EMP_ID = {lis[0]};")
                        connection.commit()
                        extra_lis = [lis[0],0,0,0,0,extra_lis[-3],extra_lis[-2]]

                elif bonus_date[6:8] in ["04","06","09","11"]:
                    if date_diff > 30:
                        cursor.execute(f"UPDATE EMP_EXTRA SET BONUS = 0, OTHER_GAIN = 0, FINES = 0, OTHER_DED = 0, BONUS_MONTH = {curdate} WHERE EMP_ID = {lis[0]};")
                        connection.commit()
                        extra_lis = [lis[0],0,0,0,0,extra_lis[-3],extra_lis[-2]]

                elif bonus_date[6:8] in ["02"]:
                    if date_diff > 31:
                        cursor.execute(f"UPDATE EMP_EXTRA SET BONUS = 0, OTHER_GAIN = 0, FINES = 0, OTHER_DED = 0, BONUS_MONTH = {curdate} WHERE EMP_ID = {lis[0]};")
                        connection.commit()
                        extra_lis = [lis[0],0,0,0,0,extra_lis[-3],extra_lis[-2]]
                
                for j in range(1,5):
                    lis.append(loan_lis[j])
                for j in range(1,7):
                    lis.append(extra_lis[j])

                tree.insert(parent='',index=END,values=lis)

    def particularemp_rec():
        rightframe.destroy()
        label.config(text='Search Record of a Particular Employee...')
        activebtn(4)

        rec_frame = Frame(window,bg='#F9E8D9')
        rec_frame.columnconfigure(0, weight = 1)
        rec_frame.columnconfigure(1, weight = 1)
        rec_frame.columnconfigure(2, weight = 1)
        rec_frame.columnconfigure(3, weight = 1)

        rec_frame.rowconfigure(0, weight = 1)
        rec_frame.rowconfigure(1, weight = 1)
        #Added extra rows and columns to adjust positioning.
        rec_frame.rowconfigure(2, weight = 1)
        rec_frame.rowconfigure(3, weight = 1)
        rec_frame.rowconfigure(4, weight = 1)
        rec_frame.rowconfigure(5, weight = 1)
        rec_frame.rowconfigure(6, weight = 1)
        rec_frame.place(x=350,y=110,width=840,height=508)

        emp_id = StringVar()

        text1 = Label(rec_frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text1.grid(column=0,row=0)

        entry1 = Entry(rec_frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry1.grid(column=1,row=0)

        def on_enter_showrecemp(e):
            button2.config(bg='#01d449',fg='black')
            
        def on_leave_showrecemp(e):
            button2.config(bg='white',fg='#01d449')

        def locate_emp():
            empid = emp_id.get()

            if empid == "":
                messagebox.showerror("Error","Please enter an Employee ID.")
            elif empid.isnumeric() == False:
                messagebox.showerror("Error","Please enter a valid Employee ID.")
            else:
                cursor.execute(f"SELECT * FROM EMP_DETAILS WHERE EMP_ID = {empid};") 
                rec = cursor.fetchone()

                if rec == (None):
                    messagebox.showerror("Error",f"No employee with ID {empid} exists.")
                    particularemp_rec()
                else:
                    reclis = list(rec) 

                    text1.destroy()
                    entry1.destroy()
                    button2.destroy()

                    btn4frame = Frame(window,bg='#F9E8D9')
                    btn4frame.place(x=350,y=110,width=840,height=250)

                    def on_enter_showrecemp2(e):
                        back_btn.config(bg='#01d449',fg='black')
            
                    def on_leave_showrecemp2(e):
                        back_btn.config(bg='white',fg='#01d449')

                    back_btn = Button(rec_frame,text='Back',command = particularemp_rec, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                    back_btn.bind("<Enter>",on_enter_showrecemp2)
                    back_btn.bind("<Leave>",on_leave_showrecemp2)
                    back_btn.grid(row=4,column=0,columnspan=4,sticky=N,pady=5)


                    style=ttk.Style()
                    style.theme_use('clam')

                    tree = ttk.Treeview(btn4frame,columns=('id','name','desig','salary','age','gender','email','dob','doj','accno','contact','add',"loan","interest","loan_date","repayment_time","bonus","other_gain","fine","other_ded","mop","note"),show='headings',height=10,)
                    tree.pack(fill='both',expand=True)

                    tree.column('id',anchor='center')
                    tree.heading('id',text='Employee ID')
                    tree.column('name',anchor='center')
                    tree.heading('name',text='NAME')
                    tree.column('desig',anchor='center')
                    tree.heading('desig',text='DESIGNATION')
                    tree.column('salary',anchor='center')
                    tree.heading('salary',text='SALARY(in ₹)')
                    tree.column('age',anchor='center')
                    tree.heading('age',text='AGE')
                    tree.column('gender',anchor='center')
                    tree.heading('gender',text='GENDER')
                    tree.column('email',anchor='center')
                    tree.heading('email',text='EMAIL')
                    tree.column('dob',anchor='center')
                    tree.heading('dob',text='D.O.B')
                    tree.column('doj',anchor='center')
                    tree.heading('doj',text='D.O.J')
                    tree.column('accno',anchor='center')
                    tree.heading('accno',text='ACCOUNT NO.')
                    tree.column('contact',anchor='center')
                    tree.heading('contact',text='CONTACT NO.')
                    tree.column('add',anchor='center')
                    tree.heading('add',text='ADDRESS')
                    tree.column('loan',anchor='center')
                    tree.heading('loan',text='LOANS(in ₹)')
                    tree.column('interest',anchor='center')
                    tree.heading('interest',text='INTEREST(%)')
                    tree.column('loan_date',anchor='center')
                    tree.heading('loan_date',text='DATE OF LOAN')
                    tree.column('repayment_time',anchor='center')
                    tree.heading('repayment_time',text='REPAYMENT TIME(in Years)')
                    tree.column('bonus',anchor='center')
                    tree.heading('bonus',text='BONUS(in ₹)')
                    tree.column('other_gain',anchor='center')
                    tree.heading('other_gain',text='OTHER GAINS(in ₹)')
                    tree.column('fine',anchor='center')
                    tree.heading('fine',text='FINES(in ₹)')
                    tree.column('other_ded',anchor='center')
                    tree.heading('other_ded',text='OTHER DEDUCTIONS(in ₹)')
                    tree.column('mop',anchor='center')
                    tree.heading('mop',text='MODE OF PAYMENT')
                    tree.column('note',anchor='center')
                    tree.heading('note',text='NOTE')
                    
                    style1 = ttk.Style()
                    style1.configure("Treeview.Scrollbar",
                            background="gray",
                            troughcolor="light gray",
                            gripcount=0,
                            gripcolor="white",
                            gripinset=2,
                            gripborderwidth=0,
                            thickness=10)
                    
                    hor_scrollbar = ttk.Scrollbar(btn4frame,orient='horizontal',command=tree.xview)
                    tree.configure(xscrollcommand=hor_scrollbar.set)
                    hor_scrollbar.pack(side="bottom",fill='x')
                    
                    cursor.execute(f"SELECT * FROM EMP_LOANS WHERE EMP_ID = {empid};")
                    loan_details = cursor.fetchone()
                    loan_lis = list(loan_details)
                    
                    cursor.execute(f"SELECT * FROM EMP_EXTRA WHERE EMP_ID = {empid};")
                    extra_details = cursor.fetchone()
                    extra_lis = list(extra_details)

                    date = ""
                    for j in str(reclis[7]):
                        if j == "-":
                            date += "/"
                        else:
                            date += j
                    reclis[7] = date[-2] + date[-1] + date[-3] + date[-5] + date[-4] + date[-6] + date[-10] + date[-9] + date[-8] + date[-7]

                    date = ""
                    for j in str(reclis[8]):
                        if j == "-":
                            date += "/"
                        else:
                            date += j
                    reclis[8] = date[-2] + date[-1] + date[-3] + date[-5] + date[-4] + date[-6] + date[-10] + date[-9] + date[-8] + date[-7]

                    if loan_lis[-1] == 0:
                        loan_lis[-1] = "-"
                    else:
                        cursor.execute("SELECT CURDATE()")
                        curdate = cursor.fetchone()[0]
                        cursor.execute(f"SELECT DATEDIFF(CURRENT_DATE, '{loan_lis[-2]}');")
                        days = int(cursor.fetchone()[0])

                        if int(str(curdate)[:4]) % 4 == 0:
                            time_left = loan_lis[-1] - (days/366)
                            loan_lis[-1] = f"{math.modf(time_left)[1]} years, {math.modf(time_left)[0] * 366}"
                        else:
                            time_left = loan_lis[-1] - (days/365)
                            loan_lis[-1] = f"{math.modf(time_left)[1]} years, {math.modf(time_left)[0] * 365} days"     

                    if loan_lis[-2] == None:
                        loan_lis[-2] = "-"
                    else:
                        date = ""
                        for j in str(loan_lis[-2]):
                            if j == "-":
                                date += "/"
                            else:
                                date += j
                        loan_lis[-2] = date[-2] + date[-1] + date[-3] + date[-5] + date[-4] + date[-6] + date[-10] + date[-9] + date[-8] + date[-7]
                
                    if loan_lis[-3] == 0:
                        loan_lis[-3] = "-"

                    if loan_lis[-4] == 0:
                        loan_lis[-4] = "-"
                        loan_lis.append("-")
                    
                    for i in range(1,5):
                        reclis.append(loan_lis[i])

                    for j in range(1,7):
                        reclis.append(extra_lis[j])

                    tree.insert(parent='',index=END,values=reclis)

        button2 = Button(rec_frame,text='Show Record',command = locate_emp, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        button2.bind("<Enter>",on_enter_showrecemp)
        button2.bind("<Leave>",on_leave_showrecemp)
        button2.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)
        
    def delete_rec():
        rightframe.destroy()
        btn5frame = Frame(window,bg='#F9E8D9')
        label.config(text='Delete record of a Particular Employee...')
        activebtn(5)

        btn5frame.columnconfigure(0, weight = 1)
        btn5frame.columnconfigure(1, weight = 1)
        btn5frame.columnconfigure(2, weight = 1)
        btn5frame.columnconfigure(3, weight = 1)

        btn5frame.rowconfigure(0, weight = 1)
        btn5frame.rowconfigure(1, weight = 1)
        #Added extra rows and columns to adjust positioning.
        btn5frame.rowconfigure(2, weight = 1)
        btn5frame.rowconfigure(3, weight = 1)
        btn5frame.rowconfigure(4, weight = 1)
        btn5frame.rowconfigure(5, weight = 1)
        btn5frame.rowconfigure(6, weight = 1)
        btn5frame.place(x=350,y=110,width=840,height=508)

        emp_id = StringVar()

        text1 = Label(btn5frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text1.grid(column=0,row=0)

        entry1 = Entry(btn5frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry1.grid(column=1,row=0)

        def on_enter_showrecemp(e):
            delete_btn.config(bg='#01d449',fg='black')
            
        def on_leave_showrecemp(e):
            delete_btn.config(bg='white',fg='#01d449')

        def delete_emp():
            empid = emp_id.get()

            if empid == "":
                messagebox.showerror("Error","Please enter an Employee ID.")
            elif empid.isnumeric() == False:
                messagebox.showerror("Error","Please enter a valid Employee ID.")
            elif empid in ["1","2","3"]:
                messagebox.showerror("Error","Admins cannot remove other admins.")
            else:
                cursor.execute(f"SELECT * FROM EMP_DETAILS WHERE EMP_ID = {empid};") 
                rec = cursor.fetchone()

                if rec == (None):
                    messagebox.showerror("Error",f"No employee with ID {empid} exists.")
                else:
                    cursor.execute(f"DELETE FROM EMP_DETAILS WHERE EMP_ID = {empid};")
                    cursor.execute(f"DELETE FROM EMP_LOANS WHERE EMP_ID = {empid};")
                    cursor.execute(f"DELETE FROM EMP_EXTRA WHERE EMP_ID = {empid};")
                    messagebox.showinfo("Deleted", f"Employee record successfully deleted.\nEmployee ID:{rec[0]}\nEmployee Name:{rec[1]}")
                    connection.commit()
                    delete_rec()

        delete_btn = Button(btn5frame,text='Delete Record',command = delete_emp, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        delete_btn.bind("<Enter>",on_enter_showrecemp)
        delete_btn.bind("<Leave>",on_leave_showrecemp)
        delete_btn.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)

    def modify_rec():
        rightframe.destroy()
        btn6frame = Frame(window,bg='#F9E8D9')
        btn6frame.place(x=350,y=110,width=840,height=508)
        label.config(text='Modify a Record...')
        activebtn(6)

        btn6frame.columnconfigure(0, weight = 1)
        btn6frame.columnconfigure(1, weight = 1)
        btn6frame.columnconfigure(2, weight = 1)
        btn6frame.columnconfigure(3, weight = 1)
        btn6frame.rowconfigure(0, weight = 1)
        btn6frame.rowconfigure(1, weight = 1)
        btn6frame.rowconfigure(2, weight = 1)
        btn6frame.rowconfigure(3, weight = 1)
        btn6frame.rowconfigure(4, weight = 1)
        btn6frame.rowconfigure(5, weight = 1)
        btn6frame.rowconfigure(6, weight = 1)
        btn6frame.rowconfigure(7, weight = 1)

        emp_id1 = StringVar()

        text = Label(btn6frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text.grid(column=0,row=0)

        entry = Entry(btn6frame, textvariable=emp_id1 ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry.grid(column=1,row=0)

        def id_check():
            empid = emp_id1.get()

            if empid == "":
                messagebox.showerror("Error","Please enter an Employee ID.")
            elif empid.isnumeric() == False:
                messagebox.showerror("Error","Please enter a valid Employee ID.")
            else:
                cursor.execute(f"SELECT * FROM EMP_DETAILS WHERE EMP_ID = {empid};") 
                rec = cursor.fetchone()

                if rec == (None):
                    messagebox.showerror("Error",f"No employee with ID {empid} exists.")
                else:
                    
                    text.destroy()
                    entry.destroy()
                    check_btn.destroy()

                    emp_id = StringVar()
                    emp_id.set(f"{rec[0]}")
                    emp_name = StringVar()
                    emp_name.set(f"{rec[1]}")
                    emp_desig = StringVar()
                    emp_desig.set(f"{rec[2]}")
                    emp_salary = StringVar()
                    emp_salary.set(f"{rec[3]}")
                    emp_age = StringVar()
                    emp_age.set(f"{rec[4]}")
                    emp_gender = StringVar()
                    emp_gender.set(f"{rec[5]}")
                    emp_email = StringVar()
                    emp_email.set(f"{rec[6]}")
                    emp_dob = StringVar()
                    dob_string = str(rec[7])
                    dob = dob_string[-2] + dob_string[-1] + "/" + dob_string[-5] + dob_string[-4] + "/" + dob_string[-10] + dob_string[-9] + dob_string[-8] + dob_string[-7]
                    
                    emp_doj = StringVar()
                    doj_string = str(rec[8])
                    doj = doj_string[-2] + doj_string[-1] + "/" + doj_string[-5] + doj_string[-4] + "/" + doj_string[-10] + doj_string[-9] + doj_string[-8] + doj_string[-7]
                    emp_accno = StringVar()
                    emp_accno.set(f"{rec[9]}")
                    emp_contact = StringVar()
                    emp_contact.set(f"{rec[10]}")
                    emp_add = StringVar()
                    emp_add.set(f"{rec[11]}")
                        
                    text1 = Label(btn6frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
                    text1.grid(column=0,row=0)
                    text2 = Label(btn6frame,text='Employee Name:',font=('times new roman',16),bg='#F9E8D9')
                    text2.grid(column=0,row=1)
                    text3 = Label(btn6frame,text='Designation:',font=('times new roman',16),bg='#F9E8D9')
                    text3.grid(column=0,row=2)
                    text4 = Label(btn6frame,text='Salary(in ₹):',font=('times new roman',16),bg='#F9E8D9')
                    text4.grid(column=0,row=3)
                    text5 = Label(btn6frame,text='Age:',font=('times new roman',16),bg='#F9E8D9')
                    text5.grid(column=0,row=4)
                    text6 = Label(btn6frame,text='Gender:',font=('times new roman',16),bg='#F9E8D9')
                    text6.grid(column=0,row=5)
                    text7 = Label(btn6frame,text='Email:',font=('times new roman',16),bg='#F9E8D9')
                    text7.grid(column=2,row=0)
                    text8 = Label(btn6frame,text='D.O.B:',font=('times new roman',16),bg='#F9E8D9')
                    text8.grid(column=2,row=1)
                    text9 = Label(btn6frame,text='D.O.J:',font=('times new roman',16),bg='#F9E8D9')
                    text9.grid(column=2,row=2)
                    text10 = Label(btn6frame,text='Acc No.:',font=('times new roman',16),bg='#F9E8D9')
                    text10.grid(column=2,row=3)
                    text11 = Label(btn6frame,text='Contact No.:',font=('times new roman',16),bg='#F9E8D9')
                    text11.grid(column=2,row=4)
                    text12 = Label(btn6frame,text='Address:',font=('times new roman',16),bg='#F9E8D9')
                    text12.grid(column=0,row=6)
                        
                    entry1 = Entry(btn6frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry1.grid(column=1,row=0)
                    entry2 = Entry(btn6frame, textvariable=emp_name ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry2.grid(column=1,row=1)
                    entry3 = Entry(btn6frame, textvariable=emp_desig ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry3.grid(column=1,row=2)
                    entry4 = Entry(btn6frame, textvariable=emp_salary ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry4.grid(column=1,row=3)
                    entry5 = Entry(btn6frame, textvariable=emp_age ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry5.grid(column=1,row=4)
                    entry6 = OptionMenu(btn6frame, emp_gender ,'Male','Female')
                    entry6.config(bg='lightyellow')
                    entry6['menu'].config(bg='lightyellow')
                    entry6.grid(column=1,row=5,sticky= E + W,padx=10)
                    entry7 = Entry(btn6frame, textvariable=emp_email ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry7.grid(column=3,row=0)
                    entry8 = DateEntry(btn6frame, textvariable=emp_dob ,bg='lightyellow',bd=3,font=('Times new roman',16),date_pattern='dd/MM/yyyy')
                    entry8.grid(column=3,row=1)
                    entry8.set_date(f"{dob}")
                    entry9 = DateEntry(btn6frame, textvariable=emp_doj ,bg='lightyellow',bd=3,font=('Times new roman',16),date_pattern='dd/MM/yyyy')
                    entry9.grid(column=3,row=2)
                    entry9.set_date(f"{doj}")
                    entry10 = Entry(btn6frame, textvariable=emp_accno ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry10.grid(column=3,row=3)
                    entry11 = Entry(btn6frame, textvariable=emp_contact ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry11.grid(column=3,row=4)
                    entry12 = Entry(btn6frame, textvariable=emp_add ,bg='lightyellow',bd=3,font=('Times new roman',16))
                    entry12.grid(column=1,row=6,columnspan=3,sticky= E + W,padx=10)
                    
                    def modify_emp():
                        dob_str = str(emp_dob.get())
                        dob = dob_str[-4] + dob_str[-3] + dob_str[-2] + dob_str[-1] + "-" + dob_str[-7] + dob_str[-6] + "-" + dob_str[-10] + dob_str[-9]

                        doj_str = str(emp_doj.get())
                        doj = doj_str[-4] + doj_str[-3] + doj_str[-2] + doj_str[-1] + "-" + doj_str[-7] + doj_str[-6] + "-" + doj_str[-10] + doj_str[-9]

                        modify_lis = [emp_id.get(), emp_name.get(), emp_desig.get(), emp_salary.get(), emp_age.get(), emp_gender.get(), emp_email.get(), dob, doj, emp_accno.get(), emp_contact.get(), emp_add.get()]

                        flag = 0

                        if modify_lis[0].isnumeric() == False or str(modify_lis[0]) == "" or modify_lis[3].isnumeric() == False or str(modify_lis[3]) == "" or modify_lis[4].isnumeric() == False or str(modify_lis[4]) == "" or modify_lis[9].isnumeric() == False or str(modify_lis[9]) == "" or modify_lis[10].isnumeric() == False or str(modify_lis[10]) == "" or str(modify_lis[1]).isalpha() == False or str(modify_lis[1]) == "" or str(modify_lis[2]).isalpha() == False or str(modify_lis[2]) == "" or str(modify_lis[5]).isalpha() == False or str(modify_lis[5]) == "" or str(modify_lis[11]) == "":
                            messagebox.showerror("Error", "Please enter valid values.")
                            id_check()
                        elif modify_lis[2].upper() == "ADMIN":
                            if rec[2].upper() != "ADMIN":
                                messagebox.showerror("Error", "Admins cannot add more admins.")
                                flag = 1
                            else:
                                pass
                        if flag == 0:
                            try:
                                cursor.execute(f"UPDATE EMP_DETAILS SET EMP_ID = {modify_lis[0]}, NAME = '{modify_lis[1]}', DESIGNATION = '{modify_lis[2]}', SALARY = {modify_lis[3]}, AGE = {modify_lis[4]}, GENDER = '{modify_lis[5]}', EMAIL = '{modify_lis[6]}', DOB = '{modify_lis[7]}', DOJ = '{modify_lis[8]}', ACCOUNT_NO = {modify_lis[9]}, CONTACT_NO = {modify_lis[10]}, ADDRESS = '{modify_lis[11]}' WHERE EMP_ID = {empid};")
                                cursor.execute(f"UPDATE EMP_LOANS SET EMP_ID = {modify_lis[0]} WHERE EMP_ID = {empid}")
                                cursor.execute(f"UPDATE EMP_EXTRA SET EMP_ID = {modify_lis[0]} WHERE EMP_ID = {empid}")
                                connection.commit()
                                messagebox.showinfo("Updated", "Employee info successfully updated.")
                                modify_rec()
                            except Exception as ex:
                                messagebox.showerror("Error",f"Error: {str(ex)}")

                    def on_enter_addemp(e):
                        modify_btn.config(bg='#01d449',fg='black')

                    def on_leave_addemp(e):
                        modify_btn.config(bg='white',fg='#01d449')

                    modify_btn = Button(btn6frame,text='Modify Employee',command=modify_emp,bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                    modify_btn.bind("<Enter>",on_enter_addemp)
                    modify_btn.bind("<Leave>",on_leave_addemp)
                    modify_btn.grid(row=7,column=0,columnspan=4,sticky=N,pady=5)

        def on_enter_addemp(e):
            check_btn.config(bg='#01d449',fg='black')

        def on_leave_addemp(e):
            check_btn.config(bg='white',fg='#01d449')

        check_btn = Button(btn6frame,text='Check ID',command=id_check,bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        check_btn.bind("<Enter>",on_enter_addemp)
        check_btn.bind("<Leave>",on_leave_addemp)
        check_btn.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)

    def emp_others():
        rightframe.destroy()
        btn7frame = Frame(window,bg='#F9E8D9')
        btn7frame.place(x=350,y=110,width=840,height=508)
        label.config(text='Add Bonus, Fines, etc...')
        activebtn(7)

        btn7frame.columnconfigure(0, weight = 1)
        btn7frame.columnconfigure(1, weight = 1)
        btn7frame.columnconfigure(2, weight = 1)
        btn7frame.columnconfigure(3, weight = 1)

        btn7frame.rowconfigure(0, weight = 1)
        btn7frame.rowconfigure(1, weight = 1)
        btn7frame.rowconfigure(2, weight = 1)
        btn7frame.rowconfigure(3, weight = 1)
        btn7frame.rowconfigure(4, weight = 1)
        btn7frame.rowconfigure(5, weight = 1)
        btn7frame.rowconfigure(6, weight = 1)
        btn7frame.rowconfigure(7, weight = 1)
        btn7frame.rowconfigure(8, weight = 1)

        btn7frame.place(x=350,y=110,width=840,height=508)

        emp_id = StringVar()

        text = Label(btn7frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text.grid(column=0,row=0)

        entry = Entry(btn7frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry.grid(column=1,row=0)

        def on_enter_showrecemp(e):
            search_btn.config(bg='#01d449',fg='black')
            
        def on_leave_showrecemp(e):
            search_btn.config(bg='white',fg='#01d449')

        def other_details():
            empid = entry.get()
            cursor.execute(f"SELECT * FROM EMP_EXTRA WHERE EMP_ID = {empid};")
            rec = list(cursor.fetchone())
            
            if empid == "":
                messagebox.showerror("Error","Please enter an ID.")
            elif rec == None:
                messagebox.showerror("Error","Employee not found.")
            elif empid.isnumeric() == False:
                messagebox.showerror("Error","Please enter a valid ID.")
            else:
                text.destroy()
                entry.destroy()
                search_btn.destroy()

                bonus = StringVar()
                bonus.set(f"{rec[1]}")
                other_gain = StringVar()
                other_gain.set(f"{rec[2]}")
                fine = StringVar()
                fine.set(f"{rec[3]}")
                other_ded = StringVar()
                other_ded.set(f"{rec[4]}")
                mop = StringVar()
                mop.set(f"{rec[5]}")
                note = StringVar()
                note.set(f"{rec[6]}")

                text1 = Label(btn7frame,text='Bonus(in ₹):',font=('times new roman',16),bg='#F9E8D9')
                text1.grid(column=0,row=0)
                text2 = Label(btn7frame,text='Other Gains(in ₹):',font=('times new roman',16),bg='#F9E8D9')
                text2.grid(column=0,row=1)
                text3 = Label(btn7frame,text='Fine(in ₹):',font=('times new roman',16),bg='#F9E8D9')
                text3.grid(column=2,row=0)
                text4 = Label(btn7frame,text='Other Deductions(in ₹):',font=('times new roman',16),bg='#F9E8D9')
                text4.grid(column=2,row=1)
                text5 = Label(btn7frame,text='Mode of Payment:',font=('times new roman',16),bg='#F9E8D9')
                text5.grid(column=0,row=2)
                text6 = Label(btn7frame,text='Note:',font=('times new roman',16),bg='#F9E8D9')
                text6.grid(column=0,row=3)

                Bonus = Entry(btn7frame,textvariable=bonus,bg='lightyellow',bd=3,font=('Times new roman',16))
                Bonus.grid(column=1,row=0)
                Other_gain = Entry(btn7frame,textvariable=other_gain,bg='lightyellow',bd=3,font=('Times new roman',16))
                Other_gain.grid(column=1,row=1)
                Fine = Entry(btn7frame,textvariable=fine,bg='lightyellow',bd=3,font=('Times new roman',16))
                Fine.grid(column=3,row=0)
                Other_ded = Entry(btn7frame,textvariable=other_ded,bg='lightyellow',bd=3,font=('Times new roman',16))
                Other_ded.grid(column=3,row=1)
                Mop = Entry(btn7frame,textvariable=mop,bg='lightyellow',bd=3,font=('Times new roman',16))
                Mop.grid(column=1,row=2,columnspan=3,padx=10,sticky= E + W)
                Note = Entry(btn7frame,textvariable=note,bg='lightyellow',bd=3,font=('Times new roman',16))
                Note.grid(column=1,row=3,columnspan=3,padx=10,sticky= E + W)

                def on_enter_showrecemp(e):
                    modify_btn.config(bg='#01d449',fg='black')
            
                def on_leave_showrecemp(e):
                    modify_btn.config(bg='white',fg='#01d449')
                
                def on_enter_showrecemp2(e):
                    back.config(bg='#01d449',fg='black')
            
                def on_leave_showrecemp2(e):
                    back.config(bg='white',fg='#01d449')

                def modify_extra():
                    if Note.get() == "":
                        note1 = "N/A"
                    if Mop.get() == "":
                        mop1 = "Net Banking"
                    if Bonus.get() == "" or Other_gain.get() == "" or Fine.get() == "" or other_ded.get() == "":
                        messagebox.showerror("Error","Empty Fields.")
                    elif Bonus.get().isnumeric() == False or Other_gain.get().isnumeric() == False or Fine.get().isnumeric() == False or Other_ded.get().isnumeric() == False:
                        messagebox.showerror("Error","Invalid Values.")
                    else:
                        note1 = Note.get()
                        mop1 = Mop.get()
                        cursor.execute("SELECT CURDATE();")
                        curdate = cursor.fetchone()[0]
                        cursor.execute(f"UPDATE EMP_EXTRA SET BONUS = {Bonus.get()}, OTHER_GAIN = {Other_gain.get()}, FINES = {Fine.get()}, OTHER_DED = {Other_ded.get()}, MOP = '{mop1}', NOTE = '{note1}', BONUS_MONTH = '{curdate}' WHERE EMP_ID = {empid};")
                        connection.commit()
                        messagebox.showinfo("Updation Successful","Fine, Bonus etc successfully updated.")
                        emp_others()

                modify_btn = Button(btn7frame,text='Modify Bonus, Fines etc',command = modify_extra, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                modify_btn.bind("<Enter>",on_enter_showrecemp)
                modify_btn.bind("<Leave>",on_leave_showrecemp)
                modify_btn.grid(row=7,column=0,columnspan=4,sticky=N,pady=5)

                back = Button(btn7frame,text='Back',command = emp_others, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                back.bind("<Enter>",on_enter_showrecemp2)
                back.bind("<Leave>",on_leave_showrecemp2)
                back.grid(row=8,column=0,columnspan=4,sticky=N,pady=5)

        search_btn = Button(btn7frame,text='Show Bonus, Fines etc',command = other_details, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        search_btn.bind("<Enter>",on_enter_showrecemp)
        search_btn.bind("<Leave>",on_leave_showrecemp)
        search_btn.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)
    
    def display_payslip():
        rightframe.destroy()
        btn9frame = Frame(window,bg='#F9E8D9')
        btn9frame.place(x=350,y=110,width=840,height=508)
        label.config(text='Salary Slip of a Particular Employee...')
        activebtn(9)

        btn9frame.columnconfigure(0, weight = 1)
        btn9frame.columnconfigure(1, weight = 1)
        btn9frame.columnconfigure(2, weight = 1)
        btn9frame.columnconfigure(3, weight = 1)

        btn9frame.rowconfigure(0, weight = 1)
        btn9frame.rowconfigure(1, weight = 1)
        #Added extra rows and columns to adjust positioning.
        btn9frame.rowconfigure(2, weight = 1)
        btn9frame.rowconfigure(3, weight = 1)
        btn9frame.rowconfigure(4, weight = 1)
        btn9frame.rowconfigure(5, weight = 1)
        btn9frame.rowconfigure(6, weight = 1)

        emp_id = StringVar()

        text = Label(btn9frame,text='Employee ID:',font=('times new roman',16),bg='#F9E8D9')
        text.grid(column=0,row=0)

        entry = Entry(btn9frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry.grid(column=1,row=0)

        def on_enter_showrecemp(e):
            search_btn.config(bg='#01d449',fg='black')
            
        def on_leave_showrecemp(e):
            search_btn.config(bg='white',fg='#01d449')

        def payslip():

            empid = emp_id.get()

            if empid == "":
                messagebox.showerror("Empty Field","Please enter the required details.")
            elif empid.isnumeric() != True:
                messagebox.showerror("Error","Please enter a valid ID.")

            else:
                cursor.execute(f"SELECT * FROM EMP_DETAILS WHERE EMP_ID = {empid}")
                rec = cursor.fetchone()

                if rec == None:
                    messagebox.showerror("Error",f"No employee with ID:{empid} exists.")
                else:
                    text.destroy()
                    entry.destroy()
                    search_btn.destroy()
                    btn9frame.destroy()

                    btn9frame2 = Frame(window,bg='#F9E8D9')
                    btn9frame2.place(x=350,y=110,width=840,height=508)

                    tree = ttk.Treeview(btn9frame2,columns=('fields','data'),height=20,show='headings')
                    tree.pack(fill='both',expand=False)
                    tree.column('fields',anchor='w')
                    tree.column('data',anchor='w')
    
                    cursor.execute("SELECT CURDATE(), CURTIME();")
                    lis = cursor.fetchone()

                    receipt_date =  f"01/{str(lis[0])[-5]+str(lis[0])[-4]}/{str(lis[0])[0] + str(lis[0])[1] + str(lis[0])[2] + str(lis[0])[3]}"
                    receipt_time = "00:00"

                    cursor.execute(f"SELECT * FROM EMP_EXTRA WHERE EMP_ID = {empid}")
                    extra_lis = list(cursor.fetchone())

                    bonus = extra_lis[1]
                    other_gain = extra_lis[2]
                    gross_sal = int(rec[3]) + bonus + other_gain
                    
                    tax = 0
                    surcharge = 0

                    if gross_sal*12 <= 300000:
                        tax = 0
                    elif gross_sal*12 > 300000 and gross_sal*12 <= 600000:
                        tax = 5
                    elif gross_sal*12 > 600000 and gross_sal*12 <= 900000:
                        tax = 10
                    elif gross_sal*12 > 900000 and gross_sal*12 <= 1200000:
                        tax = 15
                    elif gross_sal*12 > 1200000 and gross_sal*12 <= 1500000:
                        tax = 20
                    elif gross_sal*12 > 1500000:
                        tax = 30
                        if gross_sal*12 > 5000000 and gross_sal*12 <= 10000000:
                            surcharge = 10
                        elif gross_sal*12 > 10000000 and gross_sal*12 <= 20000000:
                            surcharge = 15
                        elif gross_sal*12 > 20000000 and gross_sal*12 <= 50000000:
                            surcharge = 25
                        elif gross_sal*12 > 50000000:
                            surcharge = 25

                    tax1 = (gross_sal*12) * (tax/100)
                    tax2 = tax1 * (surcharge/100)
                    net_tax = (tax1 + tax2)/12

                    fine = extra_lis[3]
                    other_ded = extra_lis[4]

                    cursor.execute(f"SELECT * FROM EMP_LOANS WHERE EMP_ID = {empid}")
                    loan_lis = list(cursor.fetchone())
                    if loan_lis[4] != 0:
                        loan = round(((loan_lis[1] * ((1 + (loan_lis[2])) ** (loan_lis[4])))/(loan_lis[4]*12)),2)
                    else:
                        loan = 0

                    total_ded = net_tax + fine + other_ded + loan

                    net_pay = gross_sal - total_ded

                    receipt_code = random.randint(1000000000,9999999999) 

                    note = extra_lis[-2]
                    mop = extra_lis[-3]

                    list1 = [
                            ("  Receipt Date and Time:",f"{receipt_date} | {receipt_time}"),
                            ("  Employee ID:", f"{rec[0]}"),
                            ("  Employee Name:",f"{rec[1]}"),
                            ("  Receipt Code:",f"{receipt_code}"),
                            ("  Details:",""),
                            ("------------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------"),
                            ("  Gains:",""),
                            ("------------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------"),
                            ("  Basic Salary:",f"₹{rec[3]}"),
                            ("  Bonus:",f"₹{bonus}"),
                            ("  Others:",f"₹{other_gain}"),
                            ("  Gross Salary:",f"₹{gross_sal}"),
                            ("------------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------"),
                            ("  Deductions:",""),
                            ("------------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------"),
                            ("  Tax Deductions:",f"-₹{round(net_tax,2)}"),
                            ("  Loans:",f"-₹{loan}"),
                            ("  Fines:",f"-₹{fine}"),
                            ("  Others:",f"-₹{other_ded}"),
                            ("  Total Deductions:",f"-₹{round(total_ded,2)}"),
                            ("------------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------"),
                            ("  Net Pay:",f"₹{round(net_pay, 2)}"),
                            ("------------------------------------------------------------------------------------","-----------------------------------------------------------------------------------------------"),
                            ("  Mode of Payment:", f"{mop}"),
                            ("  Note:",f"{note}")
                            ]
                    
                    for i in list1:
                        tree.insert(parent='',index=END,values=i)

                    def on_enter_showrecemp1(e):
                        download_btn.config(bg='#01d449',fg='black')
                
                    def on_leave_showrecemp1(e):
                        download_btn.config(bg='white',fg='#01d449')
                    
                    def download_payslip():
                        empinfo = [rec[0], rec[1], f"{receipt_date} | {receipt_time}", receipt_code]
                        paygain = [rec[3], bonus, other_gain, round(gross_sal,2)]
                        paydeduction = [round(net_tax,2), loan, fine, other_ded, round(total_ded,2), round(net_pay,2)]
                        others = [mop, note]
                        payreceipt.payslip(empinfo, paygain, paydeduction, others)
                        messagebox.showinfo("Downloaded","Payslip Downloaded Successfully!")

                    download_btn = Button(btn9frame2,text='Download Payslip',command = download_payslip, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
                    download_btn.bind("<Enter>",on_enter_showrecemp1)
                    download_btn.bind("<Leave>",on_leave_showrecemp1)
                    download_btn.pack(pady = 20)

        search_btn = Button(btn9frame,text='Show payslip',command = payslip, bg='white',fg='#01d449',font=('lato',14),bd=1,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        search_btn.bind("<Enter>",on_enter_showrecemp)
        search_btn.bind("<Leave>",on_leave_showrecemp)
        search_btn.grid(row=1,column=0,columnspan=4,sticky=N,pady=5)
    
    def logout():
        messagebox.showinfo('Logging out','Logout  Successful!')
        window.destroy()
        login()
    
    leftframe_text = Label(left_frame, text = "Welcome Admin!!!", font=('Comic Sans MS',20), height = 1, border = 3,background='burlywood1',relief=RIDGE)
    leftframe_text.grid(row = 0, column=0, sticky= E + W, padx = 5, pady = 2.5)
    
    #Menu Buttons
    btn1 = Button(left_frame, text = "Add Employee Record", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = addemp,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn1.grid(row = 1, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn2 = Button(left_frame, text = "Manage Loans", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = manage_loans,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn2.grid(row = 2, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn3 = Button(left_frame, text = "Display Record of All Employees", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = allemp_rec,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn3.grid(row = 3, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn4 = Button(left_frame, text = "Search Record for a Particular Employee", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = particularemp_rec,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn4.grid(row = 4, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn5 = Button(left_frame, text = "Delete Record of a Particular Employee", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = delete_rec,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn5.grid(row = 5, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn6 = Button(left_frame, text = "Modify a Record", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = modify_rec,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn6.grid(row = 6, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn7 = Button(left_frame, text = "Add Bonus, Fines etc", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = emp_others,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn7.grid(row = 7, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn8 = Button(left_frame, text = "Display Salary Slip a of Particular Employee", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = display_payslip,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn8.grid(row = 8, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn9 = Button(left_frame, text = "Logout", font=('helvetica',10),bg='#E6DDC4', height = 1, border = 0, command = logout,cursor='hand2', activebackground='gold', activeforeground='black',pady=5)
    btn9.grid(row = 9, column=0, sticky= E + W, padx = 20, pady = 2.5)
    
    #Footer Frame
    footer_frame = Frame(window,bg='#41b3a3',width=1200,height=25)
    footer_frame.place(x=0,y=615)
    footer_text=Label(footer_frame,text='Developed by Aagman -- Class XII-A',font=('helvetica',10,'bold'),fg='black',bg='#41b3a3')
    footer_text.place(x=490,y=2)

    window.mainloop()

def login():
    
    root = Tk()
    root.geometry("626x417+400+150")
    root.resizable(False,False)
    root.title("Login Page")
    root.iconbitmap('Payroll-Management-main/assets/user.ico')
    loginframe = Frame(root)

    loginframe.columnconfigure(0, weight = 1)
    loginframe.columnconfigure(1, weight = 1)
    loginframe.rowconfigure(0, weight = 1)
    loginframe.rowconfigure(1, weight = 1)
    loginframe.rowconfigure(2, weight = 1)
    loginframe.rowconfigure(3, weight = 1)
    loginframe.place(x=105,y=40)

    logo = PhotoImage(file="Payroll-Management-main/assets/login logo.png")
    logolabel = Label(loginframe,image=logo)
    logolabel.grid(row=0,column=0,columnspan=2)

    userimage = PhotoImage(file="Payroll-Management-main/assets/user.png")
    usernamelabel = Label(loginframe,image=userimage,text=" Username:",compound=LEFT,font=('helvetica',18,'bold'))
    usernamelabel.grid(row=1,column=0)
    usernameentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
    usernameentry.grid(row=1,column=1)

    padlock = PhotoImage(file="Payroll-Management-main/assets/padlock.png")
    passwordlabel = Label(loginframe,image=padlock,text=" Password:",compound=LEFT,font=('helvetica',18,'bold'))
    passwordlabel.grid(row=2,column=0)
    passwordentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
    passwordentry.grid(row=2,column=1)
        
    def adminlogin():
        if usernameentry.get()=='' or passwordentry.get()=='':
            messagebox.showerror('Error','Fields cannot be empty!')
        elif (usernameentry.get(),passwordentry.get()) in admins:
            messagebox.showinfo('Success',"You've been logged in sucessfully!")
            root.destroy()
            adminmain()
        else:
            messagebox.showerror('Incorrect details','Please enter correct credentials!')
        
    loginbutton = Button(loginframe,text='Login',font=('helvetica',14),width=6,bg='black',fg='white',activebackground='black',activeforeground='white',cursor='hand2',command=adminlogin)
    loginbutton.grid(row=3,column=0,pady=40,columnspan=2)
    
    root.mainloop() 

login()
