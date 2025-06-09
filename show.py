from tkinter import *
from tkinter import ttk
import mysql.connector

def showfunction():

  conn = mysql.connector.connect(host="localhost",user="root",password="root",database="project1")
  c = conn.cursor()
  c.execute("select * from producttable")


  root=Tk()
  root.title("python guides")
  root.geometry("500x500")
  root['bg']='grey'


  columns=('ProductName','ProductPrice','ProductQuantity','ProductID')
  tv=ttk.Treeview(root, columns=columns)

  tv.column('#0',width=0,stretch=NO)
  tv.column('ProductName',anchor=CENTER,width=80)
  tv.column('ProductPrice',anchor=CENTER,width=80)
  tv.column('ProductQuantity',anchor=CENTER,width=80)
  tv.column('ProductID',anchor=CENTER,width=80)
  tv.heading('#0',text="",anchor=CENTER)
  tv.heading('ProductName',text="ProductName",anchor=CENTER)
  tv.heading('ProductPrice',text="ProductPrice",anchor=CENTER)
  tv.heading('ProductQuantity',text="ProductQuantity",anchor=CENTER)
  tv.heading('ProductID',text="ProductID",anchor=CENTER)

  for x in c:
    tv.insert(parent='',index=0,values=(x))

  tv.pack()
  root.mainloop()


