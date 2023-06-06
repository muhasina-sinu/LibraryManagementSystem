from tkinter import *
from PIL import ImageTk, Image  
from tkmacosx import Button
from tkinter import font
import pymysql
import mysql.connector
from addbook import *


con = mysql.connector.connect(host='localhost',user='root',password="ssiinnuu", database='library', auth_plugin = 'mysql_native_password')
cur = con.cursor() 


window = Tk()
window.title("Library")
window.geometry("800x700")


img = ImageTk.PhotoImage(Image.open("/Users/sinu/Documents/MUHASINA/my project/python/lib.jpeg"))

canvas1 = Canvas(window,width=800,height=700)
canvas1.pack(fill="both",expand=True)

canvas1.create_image(0,0,image=img,anchor="nw")
canvas1.create_text( 400, 80, text = "Welcome to the Library",fill='red',font=('times',40))

btnstyle = font.Font(family='times', size=20)

add = Button(window,text="Add book details",fg='red',bg='black',font=btnstyle, borderless=1,width=200,height=45,command=addbook).place(y=200,x=300)
add = Button(window,text="Delete book",fg='red',bg='black',font=btnstyle, borderless=1,width=200,height=45).place(y=250,x=300)
add = Button(window,text="View book list",fg='red',bg='black',font=btnstyle, borderless=1,width=200,height=45).place(y=300,x=300)
add = Button(window,text="Issue book",fg='red',bg='black',font=btnstyle, borderless=1,width=200,height=45).place(y=350,x=300)
add = Button(window,text="Return book",fg='red',bg='black',font=btnstyle, borderless=1,width=200,height=45).place(y=400,x=300)




window.mainloop()