from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image  
from tkmacosx import Button
from tkinter import font
import mysql.connector

def viewbook():
    con = mysql.connector.connect(host='localhost', user='root', password="ssiinnuu", database='library', auth_plugin = 'mysql_native_password')
    cur = con.cursor() 

    top = Toplevel()
    top.title("Library")
    top.geometry("800x700")

    img = ImageTk.PhotoImage(Image.open("/Users/sinu/Documents/MUHASINA/my project/python/lib.jpeg"))

    canvas1 = Canvas(top, width=800, height=700)
    canvas1.pack(fill="both", expand=True)

    canvas1.create_image(0,0,image=img, anchor="nw")
    canvas1.create_text( 400, 80, text = "View Books", fill='red', font=('times',40))

    sql = "select * from books;"
    cur.execute(sql)
    result = cur.fetchall()


    columns = ('Book_id', 'Title', 'Author', 'Status')

    tree = ttk.Treeview(top, columns=columns, show='headings')

    tree.column('Book_id', anchor=CENTER, width=60)
    tree.column('Author', width=150)
    tree.column('Title', width=300)
    tree.column('Status', width=80)
    tree.heading('Book_id', text='Book_id', anchor=CENTER)
    tree.heading('Title', text='Title', anchor=CENTER)
    tree.heading('Author', text='Author', anchor=CENTER)
    tree.heading('Status' ,text='Status', anchor=CENTER)

    for row in result:
        tree.insert("", "end", values=row)


    tree.place(y=200, x=100)


    top.mainloop(0)
