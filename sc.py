from tkinter import *
from tkinter import ttk
import mysql.connector

def showfunction():

  conn = mysql.connector.connect(host="localhost",user="root",password="root",database="project1")
  c = conn.cursor()
  c.execute("select * from customertable")


  root=Tk()
  root.title("python guides")
  root.geometry("800x800")
  root['bg']='grey'


  columns=('CustomerName','CustomerMobileNum','CustomerEmail','CustomerID')
  tv=ttk.Treeview(root, columns=columns)

  tv.column('#0',width=0,stretch=NO)
  tv.column('CustomerName',anchor=CENTER,width=80)
  tv.column('CustomerMobileNum',anchor=CENTER,width=80)
  tv.column('CustomerEmail',anchor=CENTER,width=80)
  tv.column('CustomerID',anchor=CENTER,width=80)
  tv.heading('#0',text="",anchor=CENTER)
  tv.heading('CustomerName',text="CustomerName",anchor=CENTER)
  tv.heading('CustomerMobileNum',text="CustomerMobileNum",anchor=CENTER)
  tv.heading('CustomerEmail',text="CustomerEmail",anchor=CENTER)
  tv.heading('CustomerID',text="CustomerID",anchor=CENTER)

  for x in c:
    tv.insert(parent='',index=0,values=(x))

  tv.pack()
  root.mainloop()
