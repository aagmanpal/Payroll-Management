from tkinter import *
from tkinter import messagebox

emp = [['pranjal','pass'],['pallavi','pass']]
admins = [['aagman','123'],['shivaansh','123']]

#Functions Defining



def empmain():
    window=Tk()
    window.title('Payroll Management System | Developed by Aagman, Shivaansh, Pranjal')
    window.geometry('1200x700+150+35')
    window.minsize(1200,700)
    window.resizable(False,False)
    
    #===========Header Frame===========
    header_frame = Frame(window,bg='#228B22')
    header_frame.place(x=0,y=0,height=60,width=1200)
    header_image=PhotoImage(file='salary.png')
    header_text=Label(header_frame,image=header_image,text='PAYROLL SYSTEM',font=('helvetica',28,'bold'),compound=LEFT,fg='black',bg='#228B22')
    header_text.place(x=490,y=3)
    
    #==========Menu Panel Frame=========
    left_frame = Frame(window,bg='white')
    left_frame.place(x=0,y=60,width=350,height=620)
    #==========Right Frame=============
    
    #==========Footer Frame============
    footer_frame = Frame(window,bg='#228B22')
    footer_frame.place(x=0,y=680,width=1200,height=20)
    
    
    
    window.mainloop()


def login():
    
    root = Tk()
    root.geometry("626x417+400+150")
    root.resizable(False,False)
    root.title("Login Page")

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
        if usernameentry.get()=='' or passwordentry.get()=='':
            messagebox.showerror('Error','Fields cannot be empty!')
        elif [usernameentry.get(),passwordentry.get()] in emp:
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


empmain()