from tkinter import *
import tkinter as tk
import pymysql
from tkinter import messagebox
import csv


root=tk.Tk()
root.geometry('1480x760')
root.configure(bg="lightskyblue")

fon=("Palatino",30,"bold")
l1=tk.Label(root,text="JAWAHAR  NAVODAYA VIDYALAYA",font=fon,bg="lightskyblue").place(relx=0.5, rely=0.1, anchor="center")
fo=("Garamond",24,"bold")
l1=tk.Label(root,text="SIJULATA-SERAIKELLA",font=fo,bg="lightskyblue").place(relx=0.5, rely=0.17, anchor="center")
f=("Trebuchet MS",10,"bold")
l1=tk.Label(root,text="@nikhlesh_mahato",font=f,bg="lightskyblue").place(relx=0.5, rely=0.95, anchor="center")

button_font=("Helvetica",10,"bold")
def sh_pass():
    if password.cget('show')=="*":
        password.config(show="")

    else:
        password.config(show="*")
def teacher():
    framet=tk.Frame(root,height=250,width=400,borderwidth=2,relief=RAISED,bg="lightblue")
    framet.place(relx=0.5, rely=0.55, anchor="center")

    l1=tk.Label(framet,text="HOST       :",bg="lightblue",font="Helvetica").place(x=40,y=40)
    host = tk.Entry(framet)
    host.place(x=180,y=40)

    l2=tk.Label(framet,text="USERNAME :",bg="lightblue",font="Helvetica").place(x=40,y=80)
    user = tk.Entry(framet)
    user.place(x=180,y=80)

    l3=tk.Label(framet,text="PASSWORD :",bg="lightblue",font="Helvetica").place(x=40,y=120)
    password = tk.Entry(framet,show="*")
    password.place(x=180,y=120)

    l4=tk.Label(framet,text="DATABASE   :",bg="lightblue",font="Helvetica").place(x=40,y=160)
    db = tk.Entry(framet)
    db.place(x=180,y=160)
    
    cb = Checkbutton(framet, text="",bg="lightblue", command=lambda: password.config(show="") if password.cget('show') == "*" else password.config(show="*"))
    cb.place(x=305, y=118)
    
    

    tok=tk.Button(framet,text="OK",font="Helvetica", command=lambda: teacher_login(framet,host.get(),user.get(),password.get(),db.get()))
    tok.place(x=180,y=200)


def teacher_login(framet,h,u,p,d):
    
    


    try:
        global conn
        conn=pymysql.connect(host="localhost",user="root",password=p,db=d)
        global cur
        cur=conn.cursor()
        
        stu.destroy()
        tea.destroy()
        stu.destroy()
                
        f=tk.Frame(root,height=450,width=1100,borderwidth=2,relief=RAISED,bg="lightblue")
        f.place(relx=0.5, rely=0.5, anchor="center")

                #teacher_introduction
        l=tk.Label(f,text="NAME : RAVI VERMA",bg="lightblue",font="Helvetica").place(x=100,y=10)
        l=tk.Label(f,text="TEACHER POST : P.G.T COMPUTER SCIENCE",bg="lightblue",font="Helvetica").place(x=100,y=40)

                #output frame
        global f2
        f2=tk.Frame(f,height=400,width=600,borderwidth=2,relief=RAISED,bg="lightblue")
        f2.place(x=520,y=70)
                
        b=Button(f,text="class 10",font=button_font,command=class10).place(x=160,y=120)
        b=Button(f,text="class 11",font=button_font,command=class11).place(x=250,y=120)
        b=Button(f,text="class 12",font=button_font,command=class12).place(x=340,y=120)

        b=Button(f,text="search",font=button_font,command=search).place(x=50,y=150)
        b=Button(f,text="add",font=button_font,command=add).place(x=50,y=180)
        b=Button(f,text="remove",font=button_font,command=remove).place(x=50,y=210)
        b=Button(f,text="update",font=button_font,command=update).place(x=50,y=240)

        framet.destroy()

    except:
        messagebox.showinfo("Information", "LOG IN FAILED!")

            

    


    
def class10():
    global conn
    global cur
    global f2
    
    s = "select * from class_10"
    cur.execute(s)
    b=cur.fetchall()
    col=0
    for i in b:
        l=tk.Label(f2,text=i).grid(column=0,row=col)
        col+=1

def class11():
    global conn
    global cur
    global f2
    
    s = "select * from class_11"
    cur.execute(s)
    b=cur.fetchall()
    col=0
    for i in b:
        l=tk.Label(f2,text=i).grid(column=0,row=col)
        col+=1


def class12():
    global conn
    global cur
    global f2

    canvas = tk.Canvas(f2, height=300, width=400, borderwidth=2, relief=tk.RAISED, bg="lightblue")
    canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(f2, orient=tk.VERTICAL, command=canvas.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas
    frame = tk.Frame(canvas, bg="lightblue")
    canvas.create_window((0, 0), window=frame, anchor=tk.NW)
    
    s = "select * from class_12"
    cur.execute(s)
    b=cur.fetchall()
    col=0
    for row, values in enumerate(b):
        for col, value in enumerate(values):
            label = tk.Label(frame, text=value, width=5, borderwidth=1, relief="solid")
            label.grid(row=row, column=col, padx=2, pady=5)
    frame.update_idletasks()
    canvas.config(scrollregion=canvas.bbox("all"))

    
def search():
    frame_button=tk.Frame(root,height=200,width=200,borderwidth=2,relief=RAISED,bg="lightblue")
    frame_button.place(x=220,y=360)
    
    e=tk.Entry(frame_button)
    e.place(x=0,y=0)
    f=tk.Entry(frame_button)
    f.place(x=0,y=50)
    b=tk.Button(frame_button,text="OK",command=lambda:search_data(e.get(),f.get(),frame_button))
    b.place(x=0,y=80)
    
def search_data(clas,name,d):
    global conn
    global cur
    global f2

    s="select * from class_12 where class='s' "
    cur.execute(s)
    b=cur.fetchall()
    r=20
    for i in b:
        l=tk.Label(f2,text=i).place(x=10,y=r)
        r+=1
        print(i)
    d.destroy()
    
def add():
    frame_button=tk.Frame(root,height=250,width=200,borderwidth=2,relief=RAISED,bg="lightblue")
    frame_button.place(x=220,y=350)
    a1=tk.Entry(frame_button)
    a1.place(x=10,y=10)
    a2=tk.Entry(frame_button)
    a2.place(x=10,y=30)
    a3=tk.Entry(frame_button)
    a3.place(x=10,y=60)
    a4=tk.Entry(frame_button)
    a4.place(x=10,y=90)
    a5=tk.Entry(frame_button)
    a5.place(x=10,y=120)
    a6=tk.Entry(frame_button)
    a6.place(x=10,y=150)
    a7=tk.Entry(frame_button)
    a7.place(x=10,y=180)
    a8=tk.Entry(frame_button)
    a8.place(x=10,y=210)

    b=tk.Button(root,text="ok",font=button_font,command=lambda: add_data(a1.get(), a2.get(), a3.get(), a4.get(), a5.get(), a6.get(), a7.get(), a8.get(),frame_button))
    b.place(x=10,y=250)
    
    
def add_data(b1, b2, b3, b4, b5, b6, b7, b8,d):
    global conn
    global cur
   
    s="insert into class_12 values ('%d','%s','%s','%d','%s','%s','%d','%s')"% (b1,b2,b3,b4,b5,b6,b7,b8)
    #s="insert into class_12 values(3,'nikhlesh','sci',17,'phy','book',100,'paid')"
    cur.execute(s)
    conn.commit()
    
    new_row = [b1,b2,b3,b4,b5,b6,b7,b8]
    #filename=glo+".csv"
    # Append the new data to the CSV file
    with open("class_12.csv", 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(new_row)
    
    print("added successfully !")
    d.destroy()
    
def remove():
    frame_button=tk.Frame(root,height=200,width=200,borderwidth=2,relief=RAISED,bg="lightblue")
    frame_button.place(x=220,y=360)
    e=tk.Entry(frame_button)
    e.place(x=0,y=0)
    f=tk.Entry(frame_button)
    f.place(x=0,y=50)
    b=tk.Button(frame_button,text="OK",command=lambda:remove_data(e.get(),f.get(),frame_button))
    b.place(x=0,y=80)
    
def remove_data(clas,name,d):
    global conn
    global cur
    global f2

    s="delete from class_12 where student_name='%s'"
    cur.execute(s)
    b=cur.fetchall()
    r=20
    for i in b:
        l=tk.Label(f2,text=i).place(x=10,y=r)
        r+=1
        print(i)
    print("removed successfully !")
    d.destroy()
def update():
    frame_button=tk.Frame(root,height=200,width=200,borderwidth=2,relief=RAISED,bg="lightblue")
    frame_button.place(x=220,y=360)
    
    b=tk.Button(frame_button,text="OK",command=lambda:button_data(frame_button))
    b.place(x=0,y=80)
def update_data(d):
    global conn
    global cur

    
    a="nikhlesh"
    b="anan"
    s="update class_12 set student_name ='%s' where student_name='%s'"%(a,b)
    cur.execute(s)
    conn.commit()
    print("successfully !")

    


def student():
    frames=tk.Frame(root,height=250,width=400,borderwidth=2,relief=RAISED,bg="lightblue")
    frames.place(relx=0.5, rely=0.55, anchor="center")

    l2=tk.Label(frames,text="NAME :",bg="lightblue").place(x=40,y=40)
    name = tk.Entry(frames)
    name.place(x=180,y=40)

    l2=tk.Label(frames,text="CLASS :",bg="lightblue").place(x=40,y=80)
    clas = tk.Entry(frames)
    clas.place(x=180,y=80)
  

    l4=tk.Label(frames,text="ROLL NO   :",bg="lightblue").place(x=40,y=120)
    roll = tk.Entry(frames)
    roll.place(x=180,y=120)

    l2=tk.Label(frames,text="SUBJECT :",bg="lightblue").place(x=40,y=160)
    sub = tk.Entry(frames)
    sub.place(x=180,y=160)
    global glo
    glo=sub.get()
    
    tok=tk.Button(frames,text="OK", command=lambda: student_login(sub.get(),frames))
    tok.place(x=180,y=200)

def student_login( f,framet):
    
    filename=f+".csv"
    try:
        f=open(filename, 'r')
        c = csv.reader(f)
        print(c)
        # Extract and print header
        header = next(c)
        print("|".join(header))
        print("-" * (13 * len(header) - 1))  # Line separator based on header length

        # Print data in a structured manner
        
        for row in c:
            print("|".join(map(str, row)))
            print(row)
        framet.destroy()
        stu.destroy()
        
    except:
        messagebox.showinfo("Information", "LOG IN FAILED!")



tea=tk.Button(root,text="TEACHER",font=("Trebuchet MS",16,"bold"),command=teacher)
tea.place(relx=0.4, rely=0.3, anchor="center")


stu=tk.Button(root,text="STUDENT",font=("Trebuchet MS",16,"bold"),command=student)
stu.place(relx=0.6, rely=0.3, anchor="center")
















root.mainloop()


    
