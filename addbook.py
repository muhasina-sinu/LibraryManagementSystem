from tkinter import *
from PIL import ImageTk, Image  
from tkmacosx import Button
from tkinter import font
import mysql.connector
import pymysql


def add():
    global num,title,author,status,cur,con
    temp1 = num.get()
    temp2 = title.get()
    temp3 = author.get()
    temp4 = status.get()
    #cur.execute("INSERT INTO books (book_id, title, author, status) VALUES (%s, '%s', '%s', '%s');" % (temp1,temp2,temp3,temp4))
    sql = "INSERT INTO books (book_id, title, author, status) VALUES (%s, '%s', '%s', '%s');" % (temp1,temp2,temp3,temp4)
    
    cur.execute(sql)
    con.commit()
    book_id = temp1+1  
    num.set(book_id)
    title.set("")
    author.set("")
    status.set("")
       
    
    


def addbook():
    global num,title,author,status,cur,con

    con = mysql.connector.connect(host='localhost',user='root',password="ssiinnuu",database='library',  auth_plugin = 'mysql_native_password')
    cur = con.cursor() 

    top = Toplevel()
    top.title("Library")
    top.geometry("800x700")
    
    sql = "select max(book_id) from books;"
    cur.execute(sql)
    result = cur.fetchone()
    book_id = result[0]+1
    

    num = IntVar()
    title = StringVar()
    author = StringVar()
    status = StringVar()
    
    num.set(book_id)

    img = ImageTk.PhotoImage(Image.open("/Users/sinu/Documents/MUHASINA/my project/python/lib.jpeg"))

    canvas1 = Canvas(top,width=800,height=700)
    canvas1.pack(fill="both",expand=True)

    canvas1.create_image(0,0,image=img,anchor="nw")
    canvas1.create_text( 400, 80, text = "Add book details",fill='red',font=('times',40))

    canvas1.create_text( 230, 210, text = "Book ID",fill='red',font=('times',20))    
    id_entry = Entry(top,width=40,textvariable= num)
    id_entry.place(y=200,x=300)


    canvas1.create_text( 220, 240, text = "Title",fill='red',font=('times',20))    
    title_entry = Entry(top,width=40, textvariable = title)
    title_entry.place(y=230,x=300)

    canvas1.create_text( 220, 270, text = "Author",fill='red',font=('times',20))    
    author_entry = Entry(top,width=40,textvariable=author)
    author_entry.place(y=260,x=300)
        
    canvas1.create_text( 220, 300, text = "Status",fill='red',font=('times',20))    
    status_entry = Entry(top,width=40,textvariable=status)
    status_entry.place(y=290,x=300)




    submit = Button(top,text='SUBMIT',fg='red',bg='black',font=('times',14),command=add)
    submit.place(y=340,x=420)



    top.mainloop()
        
        
