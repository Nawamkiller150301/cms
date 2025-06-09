from tkinter import *
from ekk import one
import mysql.connector





root=Tk()
root.geometry("500x500")
root.title('Project1 product')


def logininnitiation():
  conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
  Mycur=conn.cursor()
  querry=f"select * from loginpage WHERE username='{freespace0.get()}' and password='{freespace1.get()}';"
  Mycur.execute(querry)

  for x in Mycur:
   print(x)
  print(Mycur.rowcount)


  if (Mycur.rowcount>0):
    print("Login sucessful")
    one()
  else:
    print("Incorrect username or password!")
    result.config(text="Login Unsucessful")
  

def cancelinnitiation():
     freespace0.delete(0,END)
     freespace1.delete(0,END)

    

Username=Label(root,text="Username")
Username.pack()
Username.place(x=110,y=155)

freespace0=Entry(root)
freespace0.pack()
freespace0.place(x=175,y=155)

password=Label(root,text="Password")
password.pack()
password.place(x=110,y=190)
freespace1=Entry(root)
freespace1.pack()
freespace1.place(x=175,y=190)

Login=Button(root,text="Login",command=logininnitiation)
Login.pack()
Login.place(x=160,y=220)

Cancel=Button(root,text="Cancel",command=cancelinnitiation)
Cancel.pack()
Cancel.place(x=220,y=220)


result=Label(root)
result.pack()
result.place(x=175,y=250)

root.mainloop()


