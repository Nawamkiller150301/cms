from tkinter import *
import mysql.connector



def ann():
  
  root=Tk()
  root.title("add")
  root.geometry("500x500")

  def updateproduct():
    conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
    Mycur=conn.cursor()
    querry= f"UPDATE producttable set ProductName='{productnameinputt.get()}',ProductPrice={productpriceinpuut.get()},ProductQuantity={productquantityyinput.get()} WHERE pid={productidinput.get()}"
    Mycur.execute(querry)
    print(querry)
    conn.commit() 	                                                                                                                                                                                        
    conn.close()
    result.config(text="PRODUCT SUCESSFULLY UPDATED")

  def cancelllproduct():
    productnameinputt.delete(0,END)
    productpriceinpuut.delete(0,END)
    productquantityyinput.delete(0,END)
    productidinput.delete(0,END)





  
  previous=Label(root,text="ADD PREVIOUS PRODUCT ID WHERE YOU WANT TO DO CHANGES")
  previous.pack()
  previous.place(x=100,y=110)
  productid=Label(root,text="PRODUCT ID")
  productid.pack()
  productid.place(x=150,y=140)
  productidinput=Entry(root)
  productidinput.pack()
  productidinput.place(x=240,y=140)



  new=Label(root,text=" UPDATE YOUR NEW DETAILS HERE")
  new.pack()
  new.place(x=150,y=200)

  productnamee=Label(root,text="PRODUCT NAME")
  productnamee.pack()
  productnamee.place(x=150,y=245)
  productnameinputt=Entry(root)
  productnameinputt.pack()
  productnameinputt.place(x=250,y=245)
  productpricee=Label(root,text="PRODUCT PRICE")
  productpricee.pack()
  productpricee.place(x=150,y=285)
  productpriceinpuut=Entry(root)
  productpriceinpuut.pack()
  productpriceinpuut.place(x=250,y=285)
  productquantityy=Label(root,text="PRODUCT QUANTITY")
  productquantityy.pack()
  productquantityy.place(x=130,y=325)
  productquantityyinput=Entry(root)
  productquantityyinput.pack()
  productquantityyinput.place(x=250,y=325)

  updatebuttonn=Button(root,text="Update",command=updateproduct)
  updatebuttonn.pack()
  updatebuttonn.place(x=200,y=360)

  cancell=Button(root,text="Cancel",command=cancelllproduct)
  cancell.pack()
  cancell.place(x=290,y=360)

  result=Label(root)
  result.pack()
  result.place(x=180,y=400)
  
  root.mainloop()


