from tkinter import *
from tkinter import messagebox

emp = [['pranjal','pass'],['pallavi','pass'],['','']]
admins = [['aagman','123'],['shivaansh','123'],['','']]

#Functions Defining



def adminmain():
    window=Tk()
    window.title('Payroll Management System | Developed by Aagman, Shivaansh, Pranjal')
    window.geometry('1200x640+150+60')
    window.minsize(1200,640)
    window.resizable(False,False)
    window.iconbitmap("salary.ico")
    window.configure(bg='black')
    #===========Header Frame===========
    header_frame = Frame(window,bg='black', height=60, width = 1280)
    header_frame.place(x=0,y=0)
    header_image=PhotoImage(file='salary.png')
    header_text=Label(header_frame,image=header_image,text='PAYROLL SYSTEM',font=('Adobe Garamond Pro',28,'bold'),compound=LEFT,fg='white',bg='black')
    header_text.place(x=440,y=3)
    
    #==========Menu Panel Frame=========
    left_frame = Frame(window, bg='black')
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
    
    #Defining btn functions
    def addemp():
        rightframe.destroy()
        addemp_frame = Frame(window,bg='white')
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
        addemp_frame.place(x=350,y=110,width=840,height=508)
        #==========================Employee Details Variable========================================================
        emp_id = StringVar()
        emp_name = StringVar()
        emp_desig = StringVar()
        emp_age = StringVar()
        emp_gender = StringVar()
        emp_email = StringVar()
        emp_dob = StringVar()
        emp_doj = StringVar()
        emp_accno = StringVar()
        emp_contact = StringVar()
        emp_add = StringVar()
        #================== Details of Employess to Add==============================================================
        text1 = Label(addemp_frame,text='Employee ID:',font=('times new roman',16),bg='white')
        text1.grid(column=0,row=0)
        text2 = Label(addemp_frame,text='Employee Name:',font=('times new roman',16),bg='white')
        text2.grid(column=0,row=1)
        text3 = Label(addemp_frame,text='Designation:',font=('times new roman',16),bg='white')
        text3.grid(column=0,row=2)
        text4 = Label(addemp_frame,text='Age:',font=('times new roman',16),bg='white')
        text4.grid(column=0,row=3)
        text5 = Label(addemp_frame,text='Gender:',font=('times new roman',16),bg='white')
        text5.grid(column=0,row=4)
        text6 = Label(addemp_frame,text='Email:',font=('times new roman',16),bg='white')
        text6.grid(column=2,row=0)
        text7 = Label(addemp_frame,text='D.O.B:',font=('times new roman',16),bg='white')
        text7.grid(column=2,row=1)
        text8 = Label(addemp_frame,text='D.O.J:',font=('times new roman',16),bg='white')
        text8.grid(column=2,row=2)
        text9 = Label(addemp_frame,text='Acc No.:',font=('times new roman',16),bg='white')
        text9.grid(column=2,row=3)
        text10 = Label(addemp_frame,text='Contact No.:',font=('times new roman',16),bg='white')
        text10.grid(column=2,row=4)
        text11 = Label(addemp_frame,text='Address:',font=('times new roman',16),bg='white')
        text11.grid(column=0,row=5)
        #==============================Respective Entry Fields=======================================================
        entry1 = Entry(addemp_frame, textvariable=emp_id ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry1.grid(column=1,row=0)
        entry2 = Entry(addemp_frame, textvariable=emp_name ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry2.grid(column=1,row=1)
        entry3 = Entry(addemp_frame, textvariable=emp_desig ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry3.grid(column=1,row=2)
        entry4 = Entry(addemp_frame, textvariable=emp_age ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry4.grid(column=1,row=3)
        entry5 = Entry(addemp_frame, textvariable=emp_gender ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry5.grid(column=1,row=4)
        entry6 = Entry(addemp_frame, textvariable=emp_email ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry6.grid(column=3,row=0)
        entry7 = Entry(addemp_frame, textvariable=emp_dob ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry7.grid(column=3,row=1)
        entry8 = Entry(addemp_frame, textvariable=emp_doj ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry8.grid(column=3,row=2)
        entry9 = Entry(addemp_frame, textvariable=emp_accno ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry9.grid(column=3,row=3)
        entry10 = Entry(addemp_frame, textvariable=emp_contact ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry10.grid(column=3,row=4)
        entry11 = Entry(addemp_frame, textvariable=emp_add ,bg='lightyellow',bd=3,font=('Times new roman',16))
        entry11.grid(column=1,row=5,columnspan=3,sticky= E + W,padx=10)
        #=====================Add Employee Button Function============================
        def fun():
            pass
        #================================Buttons in Add Employee========================================================
        button1 = Button(addemp_frame,text='Add Employee',command=fun,bg='#F4CE14',fg='black',font=('helvetica',14),bd=3,relief=SOLID,cursor='hand2',activebackground='black',activeforeground='white')
        button1.grid(row=6,column=0,columnspan=4)

    def btn2_fun():
        pass

    def btn3_fun():
        pass

    def btn4_fun():
        pass

    def btn5_fun():
        pass

    def btn6_fun():
        pass

    def btn7_fun():
        pass

    def btn8_fun():
        pass
    
    def btn9_fun():
        pass
    
    def logout():
        messagebox.showinfo('Logging out','Logout  Successful!')
        window.destroy()
        login()
    
    leftframe_text = Label(left_frame, text = "Welcome Employee!", font=('Comic Sans MS',20), height = 1, border = 3,background='burlywood1',relief=RIDGE)
    leftframe_text.grid(row = 0, column=0, sticky= E + W, padx = 5, pady = 2.5)
    
    #======================Menu Buttons======================================================
    
    btn1 = Button(left_frame, text = "Add Employee Record", font=('helvetica',10), height = 1, border = 0, command = addemp, activebackground='gold', activeforeground='black',pady=5)
    btn1.grid(row = 1, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn2 = Button(left_frame, text = "Display Record of All Employees", font=('helvetica',10), height = 1, border = 0, command = btn2_fun, activebackground='gold', activeforeground='black',pady=5)
    btn2.grid(row = 2, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn3 = Button(left_frame, text = "Search Record for a Particular Employee", font=('helvetica',10), height = 1, border = 0, command = btn3_fun, activebackground='gold', activeforeground='black',pady=5)
    btn3.grid(row = 3, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn4 = Button(left_frame, text = "Delete Records of all the Employees", font=('helvetica',10), height = 1, border = 0, command = btn4_fun, activebackground='gold', activeforeground='black',pady=5)
    btn4.grid(row = 4, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn5 = Button(left_frame, text = "Delete Record of a Particular Employee", font=('helvetica',10), height = 1, border = 0, command = btn5_fun, activebackground='gold', activeforeground='black',pady=5)
    btn5.grid(row = 5, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn6 = Button(left_frame, text = "Modify a Record", font=('helvetica',10), height = 1, border = 0, command = btn6_fun, activebackground='gold', activeforeground='black',pady=5)
    btn6.grid(row = 6, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn7 = Button(left_frame, text = "Display Payroll", font=('helvetica',10), height = 1, border = 0, command = btn7_fun, activebackground='gold', activeforeground='black',pady=5)
    btn7.grid(row = 7, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn8 = Button(left_frame, text = "Display Salary Slip of all Employees", font=('helvetica',10), height = 1, border = 0, command = btn8_fun, activebackground='gold', activeforeground='black',pady=5)
    btn8.grid(row = 8, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn9 = Button(left_frame, text = "Display Salary Slip of Particular Employee", font=('helvetica',10), height = 1, border = 0, command = btn9_fun, activebackground='gold', activeforeground='black',pady=5)
    btn9.grid(row = 9, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn10 = Button(left_frame, text = "Logout", font=('helvetica',10), height = 1, border = 0, command = logout, activebackground='gold', activeforeground='black',pady=5)
    btn10.grid(row = 10, column=0, sticky= E + W, padx = 20, pady = 2.5)
    
    #=============================================Right Frame==============================================================
    rightframe = Frame(window,bg='yellow')
    rightframe.place(x=350,y=110,width=840,height=508)
    rightframe_header = Frame(window, border = 2,background='burlywood1',relief=SOLID)
    rightframe_header.place(x=350,y=60,width=840,height=50)
    #=============================================Footer Frame=============================================================
    footer_frame = Frame(window,bg='black',width=1200,height=25)
    footer_frame.place(x=0,y=615)
    footer_text=Label(footer_frame,text='Developed by Aagman,Shivaansh, and Pranjal--Class 12th A',font=('helvetica',10,'bold'),fg='white',bg='black')
    footer_text.place(x=435)
    
    
    
    window.mainloop()

    


def login():
    
    root = Tk()
    root.geometry("626x417+400+150")
    root.resizable(False,False)
    root.title("Login Page")
    root.iconbitmap('user.ico')
    loginframe = Frame(root)
    loginframe.place(x=70,y=40)

    logo = PhotoImage(file="login logo.png")
    logolabel = Label(loginframe,image=logo)
    logolabel.grid(row=0,column=1)

    userimage = PhotoImage(file="user.png")
    usernamelabel = Label(loginframe,image=userimage,text=" Username:",compound=LEFT,font=('times new roman',18,'bold'))
    usernamelabel.grid(row=1,column=0)
    usernameentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
    usernameentry.grid(row=1,column=2)

    padlock = PhotoImage(file="padlock.png")
    passwordlabel = Label(loginframe,image=padlock,text=" Password:",compound=LEFT,font=('times new roman',18,'bold'))
    passwordlabel.grid(row=2,column=0)
    passwordentry = Entry(loginframe,font=('helvetica',14),bd=3,fg='grey10')
    passwordentry.grid(row=2,column=2)

    '''def run():
        if admin_flag.get()==True:
            loginbutton = Button(loginframe,text='Login as Admin',font=('times new roman',14),width=12,bg='black',fg='white',activebackground='black',activeforeground='white',cursor='hand2',command=adminlogin)
            loginbutton.grid(row=3,column=1,pady=40)
        else:
            loginbutton = Button(loginframe,text='Employee Login',font=('times new roman',14),width=12,bg='black',fg='white',activebackground='black',activeforeground='white',cursor='hand2',command=emplogin)
            loginbutton.grid(row=3,column=1,pady=40)
        
    
    admin_flag= BooleanVar()
    checkbox=Checkbutton(root,text='Login as Admin',variable=admin_flag,font=('helvetica',10),command=run)
    checkbox.place(x=252,y=285)
    
    
    def emplogin():
        if usernameentry.get()=='' or passwordentry.get()=='':
            messagebox.showerror('Error','Fields cannot be empty!')
        elif [usernameentry.get(),passwordentry.get()] in emp:
            messagebox.showinfo('Success',"You've been logged in sucessfully!")
            root.destroy()
            empmain()
        else:
            messagebox.showerror('Incorrect details','Please enter correct credentials!')'''
        
    def adminlogin():
        #if usernameentry.get()=='' or passwordentry.get()=='':
            #messagebox.showerror('Error','Fields cannot be empty!')
        if [usernameentry.get(),passwordentry.get()] in admins:
            messagebox.showinfo('Success',"You've been logged in sucessfully!")
            root.destroy()
            adminmain()
        else:
            messagebox.showerror('Incorrect details','Please enter correct credentials!')
        
    loginbutton = Button(loginframe,text='Login as Admin',font=('times new roman',14),width=12,bg='black',fg='white',activebackground='black',activeforeground='white',cursor='hand2',command=adminlogin)
    loginbutton.grid(row=3,column=1,pady=40)
    
    root.mainloop() 


login()