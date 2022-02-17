

####################  IMPORT LIBRARIES  #####################################

    ## import the library in a way that package name
    ## doesn't have to be typed in everytime
from tkinter import *

        ### the related library ttk contains widgets which are styled
        ### using CSS for a more modern appearance







###################  GUI METHODS ###########################################



def sayHi():
        ## this function will get what the user types into the textbox
        ## or set up a default value and then put the message on the
        ## output label
    username = txtName.get()
    if username == "":
        username = "User"
    currentStatus["text"] = "Status: Saying Hi..."
    lblGreet["text"] = "Well hello there " + username


def callSayHi(event):
        ### a keypress sends event information, such as which key was
        ### pressed, this method basically just strips the event out
        ### and calls the regular sayHi() method
    sayHi()


def showContextMenu(event):
    try:
            ## most everything here is stuff built into tkinter
            ## library and events (zero is a time delay before opening)
        contextMenu.tk_popup(event.x_root, event.y_root, 0)
    finally:
            ## only needed in tkinter 8.0.x
        contextMenu.grab_release()




#######################  THE GUI  ####################################


    ## set up window
        ## title and simple geometry object, a better one can
        ## be gotten by importing the os library and using the
        ## computer's screen for sizing
gui = Tk()
gui.title("Essentials in a GUI")
gui.iconbitmap("multisizeIcon.ico")
gui.geometry("500x300")


    ## top level menu bar
        ## this creates the main menu bar and one menu with one
        ## item inside it
            ## the "lambda" event is telling the machine to wait for a
            ## click before running the function (necessary to pass
            ## arguments to a function)
mainMenu = Menu(gui)

fileMenu = Menu(mainMenu, tearoff = 0)
fileMenu.add_command(label = "Say Hi", command = (lambda: sayHi()))
mainMenu.add_cascade(label = "File", menu = fileMenu)


    ## context menu (right click)
            ## created by other menu for organization, but the
            ## function to call it is below
contextMenu = Menu(gui, tearoff = 0)
contextMenu.add_command(label = "Say Hi", command = (lambda: sayHi()))
gui.bind("<Button-3>", showContextMenu)


    ## toolbar
        ## in our toolbars we usually have images instead of words so
        ## need an image, to size either subsample (divide) or zoom (multiply)
        ## to make it the right size
toolbar = Frame(gui, bd = 1, relief = "ridge")
wave = PhotoImage(file = "wave.png")
wave = wave.subsample(4)
btnToolbarSayHi = Button(toolbar, image = wave, command = (lambda: sayHi()))


    ## main content
mainContent = Frame(gui)

    ## prompt for userinput
        ## labels make good prompts and entry is the standard
        ## input object in tkinter
lblQuestion = Label(mainContent, text="What's your name?")
txtName = Entry(mainContent)



    ## output a greeting
        ## make a place to put the output and a button to get it
        ## lambda is needed to pass parameters through the command
        ## argument (it basically means wait for event to do stuff:
        ## with parenthesis by function name it would run as soon as
        ## button is created without lambda)
lblGreet = Label(mainContent)
btnSayHi = Button(mainContent, text="Say Hi", command=(lambda: sayHi()))


    ## create a status bar
        ## just a label to change as stuff happens and in
        ## more advanced settings a prgress bar or meter
        ## to indicate how much is left to do
statusbar = Frame(gui, bd = 1, relief = "sunken")
currentStatus = Label(statusbar, text="Status: Ready...")


    ## load the widgets on the gui
            ## pack loads stuff top to bottom
            ## grid allows placement of objects in table format
            ## I like to pack in the frames, and then do grids
            ## inside of the frames
gui.config(menu = mainMenu)
toolbar.pack(fill = "both", padx = 2, pady = 5)
mainContent.pack(fill = "both", pady = 5)
statusbar.pack(side = "bottom", fill = "both")


btnToolbarSayHi.grid(row = 0, column = 0, padx = 3, pady = 5)

lblQuestion.grid(row = 0, column = 0)
txtName.grid(row = 0, column = 1)
btnSayHi.grid(row = 1, column = 0)
lblGreet.grid(row = 1, column = 1)

currentStatus.pack(side = "left", fill = "both")

    ### this sets up the key press: ctrl+shift+H to run the method
        ### for a simple keypress event: "Keypress-H"
gui.bind("<Control-Shift-KeyPress-H>", lambda event: callSayHi(event))





    ## start the gui
mainloop()


























###########  more stuff here so it scrolls to a better spot  #################
