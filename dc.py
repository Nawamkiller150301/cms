from tkinter import *
import mysql.connector



def cu():
  root=Tk()
  root.title("add")
  root.geometry("500x500")

  def deletioncustomer():
    conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
    Mycur=conn.cursor()
    querry= f"delete from customertable where CustomerID ={customeridinput.get()} and CustomerName ='{customernameinput.get()}';"
    Mycur.execute(querry)
    print(querry)
    conn.commit() 	                                                                                                                                                                                        
    conn.close()
    result.config(text="CUSTOMER SUCESSFULLY REMOVED")

  def cancelcustomer():
    customernameinput.delete(0,END)
    customeridinput.delete(0,END)
     
   




  customername=Label(root,text="CUSTOMER NAME")
  customername.pack()
  customername.place(x=110,y=155)
  customernameinput=Entry(root)
  customernameinput.pack()
  customernameinput.place(x=220,y=155)


  customerid=Label(root,text="CUSTOMER ID")
  customerid.pack()
  customerid.place(x=110,y=195)
  customeridinput=Entry(root)
  customeridinput.pack()
  customeridinput.place(x=220,y=195)

  deletebutton=Button(root,text="DELETE",command=deletioncustomer)
  deletebutton.pack()
  deletebutton.place(x=200,y=235)
  
  cancelbutton=Button(root,text="CANCEL",command=cancelcustomer)
  cancelbutton.pack()
  cancelbutton.place(x=250,y=235)


  result=Label(root)
  result.pack()
  result.place(x=180,y=280)


  root.mainloop()

