from tkinter import *
import mysql.connector



def addd():
  root=Tk()
  root.title("add")
  root.geometry("500x500")
  
  def insertproduct():
    conn=mysql.connector.connect(host ="localhost",user="root",passwd="root",database="project1")
    Mycur=conn.cursor()
    querry = f"insert into producttable values('{productnameinput.get()}',{productpriceinput.get()},{productquantityinput.get()},{productIDinput.get()});"
    Mycur.execute(querry)
    print(querry)
    conn.commit() 	                                                                                                                                                                                        
    conn.close()
    result.config(text="PRODUCT SUCESSFULLY ADDED")

  def canceproduct():
    productnameinput.delete(0,END)
    productpriceinput.delete(0,END)
    productquantityinput.delete(0,END)

  addproduct=Label(root,text="Add Product")
  addproduct.pack()

  productname=Label(root,text="PRODUCT NAME")
  productname.pack()
  productname.place(x=110,y=155)
  productnameinput=Entry(root)
  productnameinput.pack()
  productnameinput.place(x=220,y=155)


  productprice=Label(root,text="PRODUCT PRICE")
  productprice.pack()
  productprice.place(x=110,y=185)
  productpriceinput=Entry(root)
  productpriceinput.pack()
  productpriceinput.place(x=220,y=185)

  productquantity=Label(root,text="PRODUCT QUANTITY")
  productquantity.pack()
  productquantity.place(x=100,y=215)
  productquantityinput=Entry(root)
  productquantityinput.pack()
  productquantityinput.place(x=220,y=215)

  
  productID=Label(root,text="PRODUCT ID")
  productID.pack()
  productID.place(x=124,y=245)
  productIDinput=Entry(root)
  productIDinput.pack()
  productIDinput.place(x=220,y=245)

  

  addproductbutton=Button(root,text="Add Product",command=insertproduct)
  addproductbutton.pack()
  addproductbutton.place(x=150,y=280)
  
  cancelproductbutton=Button(root,text="Cancel",command=canceproduct)
  cancelproductbutton.pack()
  cancelproductbutton.place(x=250,y=280)


  result=Label(root)
  result.pack()
  result.place(x=200,y=320)
  

  root.mainloop()
