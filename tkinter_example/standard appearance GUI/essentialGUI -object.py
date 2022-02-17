

####################  IMPORT LIBRARIES  #####################################

    ## import the library in a way that package name
    ## doesn't have to be typed in everytime
from tkinter import *

        ### the related library ttk contains widgets which are styled
        ### using CSS for a more modern appearance







###################  GUI OBJECT  ###########################################

    ## create an object which encapsulates everything we want
    ## our GUI to do
class MainGUI:
    def __init__(self, root=Tk()):
            ## set up window
                ## title and simple geometry object, a better one can
                ## be gotten by importing the os library and using the
                ## computer's screen for sizing
        root.title("Essentials in a GUI")
        root.iconbitmap("multisizeIcon.ico")
        root.geometry("500x300")


            ## top level menu bar
                ## this creates the main menu bar and one menu with one
                ## item inside it
                    ## the "lambda" event is telling the machine to wait for a
                    ## click before running the function (necessary to pass
                    ## arguments to a function)
        self.mainMenu = Menu(root)

        self.fileMenu = Menu(self.mainMenu, tearoff = 0)
        self.fileMenu.add_command(label = "Say Hi", command = (lambda: self.sayHi()))
        self.mainMenu.add_cascade(label = "File", menu = self.fileMenu)


            ## context menu (right click)
                    ## created by other menu for organization, but the
                    ## function to call it is below
        self.contextMenu = Menu(root, tearoff = 0)
        self.contextMenu.add_command(label = "Say Hi", command = (lambda: self.sayHi()))
        root.bind("<Button-3>", self.showContextMenu)


            ## toolbar
                ## in our toolbars we usually have images instead of words so
                ## need an image, to size either subsample (divide) or zoom (multiply)
                ## to make it the right size
        self.toolbar = Frame(root, bd = 1, relief = "ridge")
        wave = PhotoImage(file = "wave.png")
        wave = wave.subsample(4)
        self.btnToolbarSayHi = Button(self.toolbar, image = wave, command = (lambda: self.sayHi()))


            ## main content
        self.mainContent = Frame(root)
        
            ## prompt for userinput
                ## labels make good prompts and entry is the standard
                ## input object in tkinter
        self.lblQuestion = Label(self.mainContent, text="What's your name?")
        self.txtName = Entry(self.mainContent)



            ## output a greeting
                ## make a place to put the output and a button to get it
                ## lambda is needed to pass parameters through the command
                ## argument (it basically means wait for event to do stuff:
                ## with parenthesis by function name it would run as soon as
                ## button is created without lambda)
        self.lblGreet = Label(self.mainContent)
        self.btnSayHi = Button(self.mainContent, text="Say Hi", command=(lambda: self.sayHi()))


            ## create a status bar
                ## just a label to change as stuff happens and in
                ## more advanced settings a prgress bar or meter
                ## to indicate how much is left to do
        self.statusbar = Frame(root, bd = 1, relief = "sunken")
        self.currentStatus = Label(self.statusbar, text="Status: Ready...")


            ## load the widgets on the gui
                    ## pack loads stuff top to bottom
                    ## grid allows placement of objects in table format
                    ## I like to pack in the frames, and then do grids
                    ## inside of the frames
        root.config(menu = self.mainMenu)
        self.toolbar.pack(fill = "both", padx = 2, pady = 5)
        self.mainContent.pack(fill = "both", pady = 5)
        self.statusbar.pack(side = "bottom", fill = "both")


        self.btnToolbarSayHi.grid(row = 0, column = 0, padx = 3, pady = 5)
        
        self.lblQuestion.grid(row = 0, column = 0)
        self.txtName.grid(row = 0, column = 1)
        self.btnSayHi.grid(row = 1, column = 0)
        self.lblGreet.grid(row = 1, column = 1)

        self.currentStatus.pack(side = "left", fill = "both")

            ### this sets up the key press: ctrl+shift+H to run the method
                ### for a simple keypress event: "Keypress-H"
        root.bind("<Control-Shift-KeyPress-H>", lambda event: self.callSayHi(event))


            ## start the gui
        root.mainloop()




    def sayHi(self):
            ## this function will get what the user types into the textbox
            ## or set up a default value and then put the message on the
            ## output label
        username = self.txtName.get()
        if username == "":
            username = "User"
        self.currentStatus["text"] = "Status: Saying Hi..."
        self.lblGreet["text"] = "Well hello there " + username


    def callSayHi(self, event):
            ### a keypress sends event information, such as which key was
            ### pressed, this method basically just strips the event out
            ### and calls the regular sayHi() method
        self.sayHi()


    def showContextMenu(self, event):
        try:
                ## most everything here is stuff built into tkinter
                ## library and events (not sure what the zero is)
            self.contextMenu.tk_popup(event.x_root, event.y_root, 0)
        finally:
                ## only needed in tkinter 8.0.x
            self.contextMenu.grab_release()


    


################  END OF OBJECT  ##########################################





    ## create instance of the object
myGUI = MainGUI()





















###########  more stuff here so it scrolls to a better spot  #################
