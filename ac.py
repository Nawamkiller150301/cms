from tkinter import *
import mysql.connector



def adddcustomerr():
  root=Tk()
  root.title("add")
  root.geometry("500x500")
  
  def insertcustomer():
    conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
    Mycur=conn.cursor()
    querry = f"insert into customertable values('{customernameinput.get()}','{customermobilenuminput.get()}','{customeremailinput.get()}',{customerIDinput.get()});"
    Mycur.execute(querry)
    print(querry)
    conn.commit() 	                                                                                                                                                                                        
    conn.close()
    result.config(text="CUSTOMER SUCESSFULLY ADDED")

  def cancelcustomer():
    customernameinput.delete(0,END)
    customermobilenuminput.delete(0,END)
    customeremailinput.delete(0,END)
    customerIDinput.delete(0,END)

  aad=Label(root,text="Add Customer")
  aad.pack()

  customername=Label(root,text="CUSTOMER NAME")
  customername.pack()
  customername.place(x=110,y=155)
  customernameinput=Entry(root)
  customernameinput.pack()
  customernameinput.place(x=220,y=155)


  customermobilenum=Label(root,text="CUSTOMER MOBILENUM")
  customermobilenum.pack()
  customermobilenum.place(x=110,y=185)
  customermobilenuminput=Entry(root)
  customermobilenuminput.pack()
  customermobilenuminput.place(x=220,y=185)



  customeremail=Label(root,text="CUSTOMER EMAIL")
  customeremail.pack()
  customeremail.place(x=100,y=215)
  customeremailinput=Entry(root)
  customeremailinput.pack()
  customeremailinput.place(x=220,y=215)

  
  customerID=Label(root,text="CUSTOMER ID")
  customerID.pack()
  customerID.place(x=124,y=245)
  customerIDinput=Entry(root)
  customerIDinput.pack()
  customerIDinput.place(x=220,y=245)

  
  customerdetailsbutton=Button(root,text="Add CUSTOMER DETAILS",command=insertcustomer)
  customerdetailsbutton.pack()
  customerdetailsbutton.place(x=130,y=280)
  
  cancelcustomerbutton=Button(root,text="Cancel",command=cancelcustomer)
  cancelcustomerbutton.pack()
  cancelcustomerbutton.place(x=290,y=280)


  result=Label(root)
  result.pack()
  result.place(x=200,y=320)
  

  root.mainloop()

