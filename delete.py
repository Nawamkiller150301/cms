from tkinter import *
import mysql.connector

def two():
  root=Tk()
  root.title("add")
  root.geometry("500x500")

  def deletionproduct():
    conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
    Mycur=conn.cursor()
    querry= f"delete from producttable where pid ={productidinput.get()} and ProductName='{productnameinput.get()}';"
    Mycur.execute(querry)
    print(querry)
    conn.commit() 	                                                                                                                                                                                        
    conn.close()
    result.config(text="PRODUCT SUCESSFULLY REMOVED")

  def canceproduct():
     productnameinput.delete(0,END)
     productidinput.delete(0,END)
     
   




  productname=Label(root,text="PRODUCT NAME")
  productname.pack()
  productname.place(x=110,y=155)
  productnameinput=Entry(root)
  productnameinput.pack()
  productnameinput.place(x=220,y=155)


  productid=Label(root,text="PRODUCT ID")
  productid.pack()
  productid.place(x=110,y=195)
  productidinput=Entry(root)
  productidinput.pack()
  productidinput.place(x=220,y=195)

  deletebutton=Button(root,text="DELETE",command=deletionproduct)
  deletebutton.pack()
  deletebutton.place(x=200,y=235)
  
  cancelbutton=Button(root,text="CANCEL",command=canceproduct)
  cancelbutton.pack()
  cancelbutton.place(x=250,y=235)


  result=Label(root)
  result.pack()
  result.place(x=180,y=280)


  root.mainloop()




