from tkinter import *
from ac import *
from dc import *
from uc import *
from sc import *
def oone():
  root=Tk()
  root.geometry("400x400")
  add=Button(root,text="Add Order",command=adddcustomerr)
  add.pack()
  add.place(x=150,y=100)
  delete=Button(root,text="Delete Order",command=cu)
  delete.pack()
  delete.place(x=150,y=150)
  update=Button(root,text="Update Order",command=ann)
  update.pack()
  update.place(x=150,y=200)
  show=Button(root,text="Show Order",command=showfunction)
  show.pack()
  show.place(x=150,y=250)
  root.mainloop()