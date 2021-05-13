from tkinter import *
import random 

top = Tk()
playlist = [ ]
myRolls = [ ]
rollTimes = 0
dieType = 0

   
def printList():
    print(playlist)

def exportList():
    with open('test.txt', 'w') as f:
        for item in playlist:
            f.write("%s\n" % item)


def clearWindow():
    for widgets in top.winfo_children():
        widgets.destroy()

def mainMenu():
    clearWindow()
    LMain = Label(top, text = "Block 5 GUI Projects")
    LMain.grid(column = 0, row = 1)
    B1Main = Button(text = "Week 1", bg = "blue", command = week1)
    B1Main.grid(column = 0, row = 2)
    B2Main = Button(text = "Week 2", bg = "blue")
    B2Main.grid(column = 0, row = 3)
    B3Main = Button(text = "Week 3", bg = "blue")
    B3Main.grid(column = 0, row = 4)
    
def week1():
    clearWindow()
    def results():
        result = E1.get()
        playlist.append(result)
        E1.delete(0, END)
        
    # This is a Label widget
    L1 = Label(top, text="Playlist Generator")
    L1.grid(column= 0, row = 1)

    # This is an Entry widget
    E1 = Entry(top, bd = 5)
    E1.grid(column= 0, row = 2)

    #This is a Button widget
    B1 = Button(text= " +  ", bg = "green", command = results)
    B1.grid(column = 1, row = 2)

    B2 = Button(text = " Print ", bg = "light blue", command = printList)
    B2.grid(column = 2, row = 2) 

    B3 = Button(text = "Export List", bg = "pink", command = exportList)
    B3.grid(column = 0, row = 3)

    Bexit = Button(text = "Clear Window", bg = "red", command = mainMenu)
    Bexit.grid(column = 1, row = 3)


def week2():
      def rollDice ( ) :
          #update variable types 
          dieType = E1W2.get( )
          rollTimes = E2W2.get( )
          #clear widow after pullig entry data
          clearWindow( )
          #calculate dice rolls
          for x in range(0, int (rollTimes)):
              myRolls.apped(random.radiant(1, itn (dieType))

          #display dice rolls  and present a exit button

            L4W2 = label(top, text "here are your rolls bruhhh")
            L4W2.grid ( column=0, row=1)
            #this one will use a .format() statment
            L5W2 = label(top,text = "{}" . format (myRolls))
            L5W2.grid(column= 0, row = 2)
                            
            B2W2 = button(text= "main menu", bg= "yellow", command = mainMenu)
            B2W2.grid(column= 0 row=3)

    
    clearWindow()
    L1Week2 = Label(top, text="dice roller program")
    l1Week2.grid(column = 0, row = 1)

     L2Week2= label( top, text "how many side ") 
     L2Week2.grid(column = 0, row = 2)


     L3Week2 = Label(top, text "how many rolls ")
     L3Week2.grid(column = 2, row = 2)


    E1Week2 = Entry(top, bd = 5)
    E1Week2.grid(column = 0, row = 3)


    E2Week2 = Entry(top, bd = 5)
    E2Week2.grid(column = 2, row = 3)


     B1Week2 = Button(text="roll!", bg= "yellow",commad=rollDice)
     B1Week2.grid(column=2, row=4)

#to add: roll function ad exit button 





if __name__ == "__main__":
    mainMenu()
    top.mainloop()

