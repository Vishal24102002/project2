try:
  import mysql-connector
  import tkinter as tk
  from tkinter import messagebox
except:
  import pip
  pip.main(['install','tk'])
  pip.main(['install','mysql-connector'])
  import mysql-connector
  import tkinter as tk
  from tkinter import messagebox

def connect():
  mydb=mysql.connector.connect(host="localhost",user="root",password="vishal")
  mycursor=mydb.cursor()
  try:
    mycursor.execute("use aravalian")
  except:
    mycursor.execute("create database aravalian")
    mycursor.execute("use aravalian")
    print("connected successfully")
  Start_label.destroy()
  connection_button.destroy()

def main():
  name_label=label(pradeep,text="teacher-name",fg="white",font=('calibre',10,'normal'))
  name_entry=Entry(pradeep,textvariable=user,font=('calibre',10,'normal'))
  id_label=label(pradeep,text="Employee-ID",fg="white",font=('calibre',10,'normal'))
  id_entry=Entry(pradeep,textvariable=ID,font=('calibre',10,'normal'))
  name_label.grid()
  name_entry.grid()
  id_label.grid()
  id_entry.grid()
  search_button=Button(pradeep,text="Search",cursor="hand2")
  search_button.grid()

def alertbox():
  messagebox.askyesno("confirmation","Do you want to save the data")
  mycursor.commit()

global vishal,pradeep,mycursor,mydb

vishal=Tk()
vishal.title("ARAVALIANS")
vishal.geometry("450x400")
vishal.minsize(450,400)
vishal.configure(bg="#1b03a3")
pradeep=Frame(vishal,bg="black",height=380,width=430))
pradeep.pack()
Start_label=label(pradeep,text="welcome to Aravality",fg="white")
Start_label.place(relx=0.5,rely=1,anchor='center')
connection_button=Button(pradeep,text='connect',activebackground="blue",activeforground="red",command=connect)
connection_button.place(relx=0.5,rely=1,anchor='center')
vishal.mainloop()
