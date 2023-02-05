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
    confirm = entry_3.get()
    #email validation
    if re.match(r'[a-zA-Z0-9\.]+@[a-zA-Z]+\.[a-zA-Z\.]+', email_check):
        temp=temp+1
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
                    print("valid password")
                    temp+=1
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
    
    #password confirmation
    if password_check == confirm:
        print("password reentered is valid")
        temp+=1
    else:
        messagebox.showerror("Error", "Enter password as entered in above password field")
        return
    if temp == 3:
        conn = sqlite3.connect('Registration.db')
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS faculty (
            email_id VARCHAR(320)PRIMARY KEY,
            password TEXT NOT NULL
            )""")
        params = (email_check,password_check)
        c.execute("INSERT OR IGNORE INTO faculty VALUES (?, ?)",params)
        conn.commit()
        conn.close()
        os.system('python details.py')
              
#GUI for Registration
label_0 = Label(root, text="Registration form",height="7",width=20,font=("bold", 20),fg="#212121")
label_0.place(x=90)
label_1 = Label(root, text="Email id", width="20",font=("bold",13),fg="#263238")
label_1.place(x=50,y=170)
entry_1 = Entry(root,font=13,fg="#263238")
entry_1.place(x=200,y=170)
label_2 = Label(root, text="Password", width="20",font=("bold",13),fg="#263238")
label_2.place(x=50,y=220)
entry_2 = Entry(root,font=13,fg="#263238",show='*')
entry_2.place(x=200,y=220)
label_3 = Label(root, text="Confirm", width="20",font=("bold",13),fg="#263238")
label_3.place(x=50,y=260)
label_4 = Label(root, text="Password", width="20",font=("bold",13),fg="#263238")
label_4.place(x=50,y=280)
entry_3 = Entry(root,font=13,fg="#263238",show='*')
entry_3.place(x=200,y=270)




Button(root, text='Register',font=("bold",11),width=20,bg='black',fg='white',command=check).place(x=200,y=320)

root.mainloop()

