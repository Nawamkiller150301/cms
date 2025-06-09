from tkinter import *
from allpu import *
from allcu import *

def one():

  root=Tk()
  root.geometry("500x500")
  root.title("Project1")

  product=Button(root,text="PRODUCT",command=onee)
  product.pack()
  product.place(x=200,y=180)

  customer=Button(root,text="CUSTOMER",command=oone)
  customer.pack()
  customer.place(x=200,y=240)

  order=Button(root,text="ORDER")
  order.pack()
  order.place(x=200,y=300)


  root.mainloop()




