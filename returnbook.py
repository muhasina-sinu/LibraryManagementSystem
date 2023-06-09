from tkinter import *
from PIL import ImageTk, Image  
from tkmacosx import Button
from tkinter import font
import mysql.connector
from datetime import datetime
from tkinter import messagebox

def back():
    global con,cur,num
    try:
        temp1 = num.get()
        check = "select EXISTS(select * from books_issued where book_id = %s);"% (temp1)
        cur.execute(check)
        result = cur.fetchone()

        if result[0] == 0 or temp1 == "" :
            messagebox.showerror("Error", "Please check the book id!")

        else:
            update = "UPDATE books set status='available' where book_id =%s;" %temp1
            sql = "delete from books_issued where book_id=%s;" % temp1
            try:  
                cur.execute(update)
                cur.execute(sql)
                con.commit()
                messagebox.showinfo("info", "Details added succesfully.")
                num.set("0")
            except:
                messagebox.showerror("Error", "Please check the book id!")
    except:
        messagebox.showerror("Error", "Please check the book id!")
        
    

   
def returnbook():
    global con,cur,num
        
    con = mysql.connector.connect(host='localhost',user='root',password="ssiinnuu",database='library',  auth_plugin = 'mysql_native_password')
    cur = con.cursor() 

    top = Toplevel()
    top.title("Library")
    top.geometry("800x700")

    num = IntVar()

    img = ImageTk.PhotoImage(Image.open("/Users/sinu/Documents/MUHASINA/my project/python/lib.jpeg"))

    canvas1 = Canvas(top,width=800,height=700)
    canvas1.pack(fill="both",expand=True)

    canvas1.create_image(0,0,image=img,anchor="nw")
    canvas1.create_text( 400, 80, text = "Return Book",fill='red',font=('times',40))

    canvas1.create_text( 180, 210, text = "Book ID",fill='red',font=('times',20))    
    id_entry = Entry(top,width=40,textvariable= num)
    id_entry.place(y=200,x=280)

    submit = Button(top,text='SUBMIT',fg='red',bg='black',font=('times',14),command=back)
    submit.place(y=340,x=380)

    top.mainloop()
