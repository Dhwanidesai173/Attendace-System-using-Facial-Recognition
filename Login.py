from tkinter import *
from tkinter import messagebox
import os
import re
import sqlite3
root = Tk()
root.geometry('500x500')
root.title("Attandance System")
root.resizable(width=False, height=False)

#validation method
def check():
    temp=0
    email_check = entry_1.get()
    password_check = entry_2.get()
    #email validation
    if re.match(r'[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z\.]+', email_check):
        temp+=1
        print("valid")
    else:
        messagebox.showerror("Error", "Enter valid email")
        return

    #password validation
    if len(password_check) < 6:
        messagebox.showinfo("info", "Password should contain minimum length of six")
        return
    if re.search(r'[a-z]+', password_check):
        if re.search(r'[A-Z]+', password_check):
            if re.search(r'[0-9]+', password_check):
                if re.search(r'[\!\@\#\$\%\.]+', password_check):
                    temp+=1
                    print("valid password")
                else:
                    messagebox.showinfo("Error", "Password should contain atleast one special character eg:!,@,#,$,%")
                    return
            else:
                messagebox.showinfo("Error", "Password should contain atleast one number")
                return
        else:
            messagebox.showinfo("Error", "Password should contain atleast one Capital letter")
            return
    else:
        messagebox.showinfo("Error", "Password should contain atleast one small letter")
        return

    if temp == 2:
        conn = sqlite3.connect('Registration.db')
        c = conn.cursor()
        c.execute("SELECT * FROM faculty where  email_id =?", (email_check,))
        if c.fetchone() is None:
            messagebox.showinfo("Error", "Enter valid details")
        else:
            os.system('python details.py')

def registerlink():
    os.system('python Register.py')

              
#GUI for Registration
label_0 = Label(root, text="Login form",height="7",width=20,font=("bold", 20),fg="#212121")
label_0.place(x=90)
label_1 = Label(root, text="Email id", width="20",font=("bold",13),fg="#263238")
label_1.place(x=50,y=170)
entry_1 = Entry(root,font=13,fg="#263238")
entry_1.place(x=200,y=170)
label_2 = Label(root, text="Password", width="20",font=("bold",13),fg="#263238")
label_2.place(x=50,y=220)
entry_2 = Entry(root,font=13,fg="#263238",show='*')
entry_2.place(x=200,y=220)
Button(root, text='Login',font=("bold",11),width=20,bg='brown',fg='white',command=check).place(x=200,y=270)
label_3 = Label(root, text="New user ?", width="20",font=("bold",13),fg="#263238")
label_3.place(x=50,y=345)
Button_1 = Button(root, text = "Register Here", font=("bold",11), command=registerlink,bg='brown',fg='white')
Button_1.place(x=220,y=340)
root.mainloop()

