from tkinter import *
from add import *
from delete import *
from update import *
from show import *
def onee():
  root=Tk()
  root.geometry("400x400")
  add=Button(root,text="Add Product",command=addd)
  add.pack()
  add.place(x=150,y=100)
  delete=Button(root,text="Delete Product",command=two)
  delete.pack()
  delete.place(x=150,y=150)
  update=Button(root,text="Update Product",command=ann)
  update.pack()
  update.place(x=150,y=200)
  show=Button(root,text="Show Product",command=showfunction)
  show.pack()
  show.place(x=150,y=250)
  root.mainloop()
