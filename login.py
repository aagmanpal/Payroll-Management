from tkinter import *
from tkinter import messagebox

#Functions Defining

def login():
    if usernameentry.get()=='' or passwordentry.get()=='':
         messagebox.showerror('Error','Fields cannot be empty!')
    elif usernameentry.get()=='aagmanpal' and passwordentry.get()=='123':
        messagebox.showinfo('Success',"You've been logged in sucessfully!")
        root.destroy()
        main()
    else:
        messagebox.showerror('Incorrect details','Please enter correct credentials!')

def main():
    window=Tk()
    window.title('Payroll Management System | Developed by Aagman, Shivaansh, Pranjal')
    window.geometry('1200x700+150+35')
    window.minsize(1200,700)
    window.state('zoomed')
    
    
    window.mainloop()

#GUI Part

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

loginbutton = Button(loginframe,text='Login',font=('times new roman',14),width=12,bg='black',fg='white',activebackground='black',activeforeground='white',cursor='hand2',command=login)
loginbutton.grid(row=3,column=1,pady=20)
  
root.mainloop() 