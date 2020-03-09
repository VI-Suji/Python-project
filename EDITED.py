from tkinter import ttk, StringVar, Tk
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
import time;
import datetime
import sqlite3



with sqlite3.connect("form.db") as db1:
    cursor=db1.cursor()
    
cursor.execute('''
CREATE TABLE IF NOT EXISTS details(
roomno int,
admno int,
name string,
branch string,
place string,
mobileno int,
dategoing String,
datecoming String)
''')

db1.commit()


with sqlite3.connect("project.db") as db:
    cursor=db.cursor()

cursor.execute('''
DROP TABLE students
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS students(
roomno int,
admno int,
name string,
branch string,
mobileno int)
''')

cursor.execute('''
INSERT INTO students(roomno,admno,name,branch,mobileno) VALUES
(000,000000,"SUJITH V I","CSE",0000000000)
''')


db.commit()

now = datetime.datetime.today()



root=Tk()
root.title("HOME GOING REGISTER")
root.geometry('1360x650')
root.config()

USERNAME=IntVar()
PASSWORD=IntVar()
PLACE_TO=StringVar()
SEARCH_NAME=StringVar()
SEARCH_ID=IntVar()

A=IntVar()
B=IntVar()
C=StringVar()
D=StringVar()
E=IntVar()

def login1():
    k=1
    conn=sqlite3.connect('form.db')
    with conn:
        cursor=conn.cursor()
        cursor.execute('SELECT * FROM details')
        res = cursor.fetchall()
        print("   ","ROOMNO","|","ADMNO ","|","NAME","|","BRANCH","|","PLACE","|","MOBILE NO","|","DATE AND TIME OF GOING","|","DATE AND TIME COMING")
    if res:
        for i in res:
            print(k,".",i[0],"| ",i[1],"|",i[2],"|",i[3],"|",i[4],"|",i[5],"|",i[6],"|",i[7])
            k=k+1

def login2():
    R=1
    searchname= simpledialog.askstring("name","Enter The Name")
    searchid= simpledialog.askinteger("admission no","Enter The Id")
    name=searchname.upper()
    adm=searchid
    conn=sqlite3.connect('form.db')
    with conn:
        cursor=conn.cursor()
        find_ = ("SELECT * FROM details WHERE name=? AND admno=?")
        cursor.execute(find_,[(name),(adm)])
        resultS = cursor.fetchall()
    if resultS:
        for i in resultS:
            print(R,".","ROOM NO:",i[0])
            print("   ","ADM NO:",i[1])
            print("   ","NAME:",i[2])
            print("   ","BRANCH:",i[3])
            print("   ","PLACE:",i[4])
            print("   ","MOB NO:",i[5])
            print("   ","DATE OF GOING:",i[6])
            print("   ","DATE OF COMING:",i[7])
            R=R+1
def login():
    while True:
        mobno = PASSWORD.get()
        admno = USERNAME.get()
        F=PLACE_TO.get()
        F=F.upper()
        a= simpledialog.askstring("ARE YOU COMING BACK (Y/N)","ARE YOU COMING BACK (Y/N)?")
        a=a.lower()
        if (a=='y'):
                with sqlite3.connect("form.db") as db1:
                    cursor = db1.cursor()
                cursor.execute('UPDATE details SET datecoming = ? WHERE admno=admno',(now,))
                messagebox.showinfo("registered succesfully!!","you are returned to hostel")
                db1.commit()
                return("exit")
                        
        else :
                conn = sqlite3.connect('project.db')
                with conn:
                        cursor=conn.cursor()
                        find_user = ("SELECT * FROM students WHERE admno=? AND mobileno=?")
                        cursor.execute(find_user,[(admno),(mobno)])
                        results = cursor.fetchall()
                if results:
                        for i in results:
                            A=i[0]
                            B=i[1]
                            C=i[2]
                            D=i[3]
                            E=i[4]
                        with sqlite3.connect("form.db") as db1:
                            cursor = db1.cursor()
                        cursor.execute('INSERT INTO details(roomno,admno,name,place,branch,mobileno,dategoing) VALUES (?,?,?,?,?,?,?)',(A,B,C,F,D,E,now))
                        messagebox.showinfo("registered succesfully","your registration succeded")
                        db1.commit()
                        return("exit")
                                        
                else:
                        print("password not recognised")
                        again=input("do you want to try again (y/n) : ")
                        if (again.lower()=='n'):
                            print ("good bye")
                            break;
                            return("exit")

                
LeftMayFrame=Frame(root,width=700, height=800, bd=8, background="red", relief="raise")
LeftMayFrame.pack(side=LEFT)
RightMayFrame=Frame(root,width=700, height=800, bd=8, background="blue", relief="raise")
RightMayFrame.pack(side=RIGHT)

student=Label(LeftMayFrame, text="STUDENT LOGIN PORTAL", bg="red", width=40, font=("bold",20))
student.place(x=20,y=53)

username=Label(LeftMayFrame, text="USERNAME", bg="white", font=('arial',10,'bold'), bd=16)
username.place(x=200,y=200)

userentry1=Entry(LeftMayFrame,textvar=USERNAME, bd=16, bg="white")
userentry1.place(x=400,y=200)

password=Label(LeftMayFrame, text="PASSWORD", bg="white", font=('arial',10,'bold'), bd=16)
password.place(x=200,y=300)

passentry1=Entry(LeftMayFrame,textvar=PASSWORD, bd=16, bg="white")
passentry1.place(x=400,y=300)

place=Label(LeftMayFrame, text="PLACE_TO", bg="white", font=('arial',10,'bold'), bd=16)
place.place(x=200,y=400)

placeentry1=Entry(LeftMayFrame,textvar=PLACE_TO, bd=16, bg="white")
placeentry1.place(x=400,y=400)

Button(LeftMayFrame, text="SUBMIT", bg="yellow", bd=20, command=login).place(x=300,y=500)
Button(LeftMayFrame, text="CANCEL", bg="yellow", bd=20).place(x=400,y=500)

admin=Label(RightMayFrame, text="ADMIN LOGIN PORTAL", bg="blue", width=40, font=("bold",20))
admin.place(x=20,y=53)

username=Label(RightMayFrame, text="USERNAME", bg="white", font=('arial',10,'bold'), bd=16)
username.place(x=200,y=250)

userentry=Entry(RightMayFrame,textvar=username, bd=16, bg="white")
userentry.place(x=400,y=250)

password=Label(RightMayFrame, text="PASSWORD", bg="white", font=('arial',10,'bold'), bd=16)
password.place(x=200,y=400)

passentry=Entry(RightMayFrame,textvar=password, bd=16, bg="white")
passentry.place(x=400,y=400)

Button(RightMayFrame, text="SUBMIT", bg="purple", bd=20, command=login1).place(x=150,y=500)
Button(RightMayFrame, text="CANCEL", bg="violet", bd=20).place(x=250,y=500)
Button(RightMayFrame, text="SEARCH", bg="yellow", bd=20, command=login2).place(x=350,y=500)

root.mainloop ();
