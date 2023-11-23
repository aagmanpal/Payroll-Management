from tkinter import *
from tkinter import messagebox

emp = [['pranjal','pass'],['pallavi','pass'],['','']]
admins = [['aagman','123'],['shivaansh','123']]

#Functions Defining



def empmain():
    window=Tk()
    window.title('Payroll Management System | Developed by Aagman, Shivaansh, Pranjal')
    window.geometry('1200x640+150+60')
    window.minsize(1200,640)
    window.resizable(False,False)
    window.iconbitmap("salary.ico")
    
    #===========Header Frame===========
    header_frame = Frame(window,bg='black', height=63, width = 1280)
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
    def btn1_fun():
        pass

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
        window.destroy()
        login()
    
    leftframe_text = Label(left_frame, text = "Welcome Employee!", font=('Comic Sans MS',20), height = 1, border = 3,background='light goldenrod',relief=RIDGE)
    leftframe_text.grid(row = 0, column=0, sticky= E + W, padx = 5, pady = 2.5)
    btn1 = Button(left_frame, text = "Add Employee Record", font=('helvetica',10), height = 1, border = 0, command = btn1_fun, activebackground='gold', activeforeground='black',pady=5)
    btn1.grid(row = 1, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn2 = Button(left_frame, text = "Display Record of All Employees", font=('helvetica',10), height = 1, border = 0, command = btn2_fun, activebackground='gold', activeforeground='black',pady=5)
    btn2.grid(row = 2, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn3 = Button(left_frame, text = "Search record for a particular employee", font=('helvetica',10), height = 1, border = 0, command = btn3_fun, activebackground='gold', activeforeground='black',pady=5)
    btn3.grid(row = 3, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn4 = Button(left_frame, text = "Delete records of all the employees", font=('helvetica',10), height = 1, border = 0, command = btn4_fun, activebackground='gold', activeforeground='black',pady=5)
    btn4.grid(row = 4, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn5 = Button(left_frame, text = "Delete a record of a particular employee", font=('helvetica',10), height = 1, border = 0, command = btn5_fun, activebackground='gold', activeforeground='black',pady=5)
    btn5.grid(row = 5, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn6 = Button(left_frame, text = "Modify a record", font=('helvetica',10), height = 1, border = 0, command = btn6_fun, activebackground='gold', activeforeground='black',pady=5)
    btn6.grid(row = 6, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn7 = Button(left_frame, text = "Display Payroll", font=('helvetica',10), height = 1, border = 0, command = btn7_fun, activebackground='gold', activeforeground='black',pady=5)
    btn7.grid(row = 7, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn8 = Button(left_frame, text = "Display salary slip of all employees", font=('helvetica',10), height = 1, border = 0, command = btn8_fun, activebackground='gold', activeforeground='black',pady=5)
    btn8.grid(row = 8, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn9 = Button(left_frame, text = "Display salary slip of particular employee", font=('helvetica',10), height = 1, border = 0, command = btn9_fun, activebackground='gold', activeforeground='black',pady=5)
    btn9.grid(row = 9, column=0, sticky= E + W, padx = 20, pady = 2.5)
    btn10 = Button(left_frame, text = "Logout", font=('helvetica',10), height = 1, border = 0, command = logout, activebackground='gold', activeforeground='black',pady=5)
    btn10.grid(row = 10, column=0, sticky= E + W, padx = 20, pady = 2.5)
    #==========Right Frame=============
    
    #==========Footer Frame============
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

    def run():
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
        #if usernameentry.get()=='' or passwordentry.get()=='':
            #messagebox.showerror('Error','Fields cannot be empty!')
        if [usernameentry.get(),passwordentry.get()] in emp:
            messagebox.showinfo('Success',"You've been logged in sucessfully!")
            root.destroy()
            empmain()
        else:
            messagebox.showerror('Incorrect details','Please enter correct credentials!')
        
    def adminlogin():
        if usernameentry.get()=='' or passwordentry.get()=='':
            messagebox.showerror('Error','Fields cannot be empty!')
        elif [usernameentry.get(),passwordentry.get()] in admins:
            messagebox.showinfo('Success',"You've been logged in sucessfully!")
            root.destroy()
            empmain()
        else:
            messagebox.showerror('Incorrect details','Please enter correct credentials!')
        
    run()
    
    root.mainloop() 


login()