from tkinter import *
from tkinter import messagebox
import os
import re
import numpy as np
import cv2
import os
import time
import pandas as pd


root = Tk()
root.geometry('500x500')
root.title("Attandance System")
root.resizable(width=False, height=False)
values = []
def class1(value):
    values.append(value)
def cammodule():
    print(values)
    labels=[]

    #label for training dataset of person 1
    for _ in range(50):
        labels.append(1)

    #label for training dataset of person 2
    for _ in range(50):
        labels.append(32)
    
    #label for training dataset of person 3
    for _ in range(50):
        labels.append(26)
    faces=[]
    for i in range(0,50):
        sre="dhwani_{}.jpg".format(i)
        img=cv2.imread(sre)
        print(i)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces.append(img)
    for i in range(0,50):
        sre="hetvi_{}.jpg".format(i)
        img=cv2.imread(sre)
        print(i)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces.append(img)
    for i in range(0,50):
        sre="mansi_{}.jpg".format(i)
        img=cv2.imread(sre)
        print(i)
        img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        faces.append(img)

    print(faces)
    print(len(labels))
    print(len(faces))

    face_recognizer = cv2.face.LBPHFaceRecognizer_create()

    face_recognizer.train(faces, np.array(labels)) 

    detector= cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    faces=None
    img=None
    temp = []
    excel_enroll = []
    excel_pred = []
    while(True):
        ret, img = cap.read() 
        img = cv2.flip(img, 1)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, 1.3, 5)
        i=0
        j=0
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

        cv2.imshow('frame',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            for (x,y,w,h) in faces:
                f=img[y:y+h,x:x+w]
                f=cv2.cvtColor(f, cv2.COLOR_BGR2GRAY)
                gray_pics="{}.jpg".format(j)
                clr_image=cv2.imwrite(gray_pics,f)
                j=j+1
                label= face_recognizer.predict(f)
                temp = list(label)
                print(label)
                a,b = temp
                excel_enroll.append(a)
                excel_pred.append(b)
            break
    print(excel_enroll)
    print(excel_pred)
    clr_image=cv2.imwrite("p1.jpg",img)
    gray_image=cv2.imwrite("p2.jpg",gray)

    # Wait for 5 seconds
    cap.release()
    cv2.destroyAllWindows()
    date=time.strftime("%d-%m-%Y")
    students=50
    enn=[]  #enrollment number list
    attendance=len(enn)
    for i in range(0,students):
        enn.append(i+1)
    df = pd.DataFrame()
    print (date)
    print (enn)
    sheetname = '_'.join(values)
    print(sheetname)
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter('attendance.xlsx', engine='xlsxwriter')
    # Convert the dataframe to an XlsxWriter Excel object.
    df.to_excel(writer, sheet_name=sheetname,index=False)

    workbook=writer.book
    worksheet=writer.sheets[sheetname]

    worksheet.write('A1', "en_no")
    worksheet.write('B1', date)

    for i in range(1,len(enn)+1):
        worksheet.write(i,0,i)
        worksheet.write(i,1,0)
    
    for k in range(0,len(excel_enroll)):
        for j in range(1,students):
            if excel_enroll[k] == j:
                worksheet.write(j,1,1)
    writer.save()
    present=pd.read_excel('attendance.xlsx', sheet_name=sheetname, index_col=1) 


label_0 = Label(root, text="Welcome!",height="7",width=20,font=("bold", 20),fg="#212121")
label_0.place(x=90)

tkvar = StringVar(root)
choices_class = { 'CO','IT','D2D Co','D2D IT'} 
popupMenu = OptionMenu(root, tkvar, *choices_class,command=class1).place(x=250,y=160)
Label(root, text="Choose class1",font=("bold",13),fg="#263238").place(x=120,y=165)

#tkvar11 = StringVar(root)
#choices_class1 = { 'CO','IT','D2D Co','D2D IT','None'} 
#popupMenu = OptionMenu(root, tkvar11, *choices_class1,command=class1).place(x=250,y=210)
#Label(root, text="Choose class2",font=("bold",13),fg="#263238").place(x=120,y=215)


tkvar1 = StringVar(root)
choices_sem = { '5th','7th'} 
popupMenu = OptionMenu(root, tkvar1, *choices_sem,command=class1).place(x=250,y=210)
Label(root, text="Choose semester",font=("bold",13),fg="#263238").place(x=95,y=215)

tkvar2 = StringVar(root)
choices_subcode = {'DC','MI','CD','MP'} 
popupMenu = OptionMenu(root, tkvar2, *choices_subcode,command=class1).place(x=250,y=260)
Label(root, text="Choose sub_code",font=("bold",13),fg="#263238").place(x=94,y=265)

Button(root, text='Capture photo',font=("bold",11),width=20,bg='brown',fg='white',command=cammodule).place(x=180,y=310)

root.mainloop()
