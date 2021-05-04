from tkinter import *


top = tk( )
groceryList = [ ]

def results( ):
         results = E1 . get ()
         print(result)
         print(type(results))

def addToList ( ) :
         newItem = E1 . get ( )
         groceryList.append ( newItem )

# this is a label widget
L1 = Label (top,  text = "grocery list!")
L1 . grid (column = 0, row = 1)

#this is an entry wiget
E1 = Entry( top , bd = 5)
E1. grid(column = 0, row = 2)

 # this is a button wiget
b1= button( text= "  print list     ",   bg="red" , command =  results)
b1 . grid ( column = 0, row = 3)

B2 = Button ( )
B2.grid ( )

top.mainloop ( )
