from tkinter import *
from PIL import ImageTk, Image  
from tkmacosx import Button
from tkinter import font
import mysql.connector
from datetime import datetime
from tkinter import messagebox

def issue():
    global con,cur,num,name
    temp1 = num.get()
    temp2 = name.get()
    now = datetime.now()
    temp3 = now.strftime('%Y-%m-%d %H:%M:%S')
    sql = "INSERT INTO books_issued (book_id, issued_to, date) VALUES (%s, '%s', '%s');" % (temp1,temp2,temp3)
    try:
        cur.execute(sql) 
        update = "UPDATE books set status='issued' where book_id =%s;" %temp1
        cur.execute(update)
        con.commit()
        messagebox.showinfo("info", "Details added succesfully.")
        num.set("0")
        name.set("")
    except:
        messagebox.showerror("Error", "Please check the input values. The book may be issued already!")

def issuebook():
    global con,cur,num,name
    
    con = mysql.connector.connect(host='localhost',user='root',password="ssiinnuu",database='library',  auth_plugin = 'mysql_native_password')
    cur = con.cursor() 

    top = Toplevel()
    top.title("Library")
    top.geometry("800x700")

    num = IntVar()
    name = StringVar()

    img = ImageTk.PhotoImage(Image.open("/Users/sinu/Documents/MUHASINA/my project/python/lib.jpeg"))

    canvas1 = Canvas(top,width=800,height=700)
    canvas1.pack(fill="both",expand=True)

    canvas1.create_image(0,0,image=img,anchor="nw")
    canvas1.create_text( 400, 80, text = "Issue Book",fill='red',font=('times',40))

    canvas1.create_text( 180, 210, text = "Book ID",fill='red',font=('times',20))    
    id_entry = Entry(top,width=40,textvariable= num)
    id_entry.place(y=200,x=280)

    canvas1.create_text( 180, 240, text = "Issued to",fill='red',font=('times',20))    
    title_entry = Entry(top,width=40, textvariable = name)
    title_entry.place(y=230,x=280)


    submit = Button(top,text='SUBMIT',fg='red',bg='black',font=('times',14),command=issue)
    submit.place(y=340,x=380)

    top.mainloop()