from tkinter import *
import mysql.connector



def ann():
  
  root=Tk()
  root.title("add")
  root.geometry("500x500")

  def updatecustomerrrr():
    conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
    Mycur=conn.cursor()
    querry= f"UPDATE customertable set CustomerName='{customernameinput.get()}', CustomerMobileNum={customermobilenuminput.get()}, CustomerEmail='{customeremailinput.get()}' WHERE CustomerID={customeridinput.get()}"
    Mycur.execute(querry)
    print(querry)
    conn.commit() 	                                                                                                                                                                                        
    conn.close()
    result.config(text="CUSTOMER SUCESSFULLY UPDATED")

  def cancelllcustomer():
    customernameinput.delete(0,END)
    customermobilenuminput.delete(0,END)
    customeremailinput.delete(0,END)
    customeridinput.delete(0,END)





  
  previous=Label(root,text="ADD PREVIOUS CUSTOMER ID WHERE YOU WANT TO DO CHANGES")
  previous.pack()
  previous.place(x=100,y=110)
  customerid=Label(root,text="CUSTOMER ID")
  customerid.pack()
  customerid.place(x=150,y=140)
  customeridinput=Entry(root)
  customeridinput.pack()
  customeridinput.place(x=240,y=140)



  new=Label(root,text=" UPDATE YOUR NEW DETAILS HERE")
  new.pack()
  new.place(x=150,y=200)

  customernamee=Label(root,text="CUSTOMER NAME")
  customernamee.pack()
  customernamee.place(x=140,y=245)
  customernameinput=Entry(root)
  customernameinput.pack()
  customernameinput.place(x=250,y=245)

  customermobilenum=Label(root,text="CUSTOMER MOBILE NUMBER")
  customermobilenum.pack()
  customermobilenum.place(x=85,y=285)
  customermobilenuminput=Entry(root)
  customermobilenuminput.pack()
  customermobilenuminput.place(x=250,y=285)
  
  customeremail=Label(root,text="CUSTOMER EMAIL")
  customeremail.pack()
  customeremail.place(x=140,y=325)
  customeremailinput=Entry(root)
  customeremailinput.pack()
  customeremailinput.place(x=250,y=325)

  updatebuttonn=Button(root,text="Update",command=updatecustomerrrr)
  updatebuttonn.pack()
  updatebuttonn.place(x=200,y=360)

  cancell=Button(root,text="Cancel",command=cancelllcustomer)
  cancell.pack()
  cancell.place(x=290,y=360)

  result=Label(root)
  result.pack()
  result.place(x=180,y=400)
  
  root.mainloop()

