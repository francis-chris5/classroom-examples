

####################  IMPORT LIBRARIES  #####################################

import tkinter as tk




### trivial change to show github branch


people = []
favFood = ["pizza", "hot wings", "cheese burgers", "tacos"]


###################  GUI METHODS ########################################################

def DisplayStatus(status):
    lblStatus["text"] = "STATUS: " + str(status)
## end DisplayStatus()


def AddPerson(event):
    
    if txtName.get() == "":
        name = "<<Person>>"
    else:
        name = txtName.get()
        
    try:
        age = int(txtAge.get())
    except:
        age = -1
        
    if txtTown.get() == "":
        town = "<<Town>>"
    else:
        town = txtTown.get()
        
        
    if omChosen.get() == "":
        favFood = "<<Food>>"
    else:
        favFood = omChosen.get()
        
        
    people.append([name, str(age), town, favFood])
    
    lstDisplay.delete(0, tk.END)
    for person in people:
        lstDisplay.insert(tk.END, person)
 
    txtName.delete(0, tk.END)
    txtAge.delete(0, tk.END)
    txtTown.delete(0, tk.END)
    omChosen.set("")
    txtName.focus_set()

    DisplayStatus("Data added successfully...")
## end AddPerson()


def EditPerson(event):
    selected = lstDisplay.curselection()
    person = people[selected[0]]
    
    dialog = tk.Toplevel(gui)
    lblTitle = tk.Label(dialog, text="Edit Data")
    txtName = tk.Entry(dialog)
    txtName.insert(0, person[0])
    txtAge = tk.Entry(dialog)
    txtAge.insert(0, person[1])
    txtTown = tk.Entry(dialog)
    txtTown.insert(0, person[2])
    strFood = tk.StringVar(dialog, value=person[3])
    
    omFood = tk.OptionMenu(dialog, strFood, *favFood)
    
    btnEdit = tk.Button(dialog, text = "Make Changes")
    btnEdit.bind("<Button-1>", lambda event: UpdateData(event, txtName.get(), int(txtAge.get()), txtTown.get(), strFood.get(), dialog))
    
    lblTitle.grid(row=0,column=0,padx=30, pady=7)
    txtName.grid(row=1,column=0,padx=30, pady=7)
    txtAge.grid(row=2,column=0,padx=30, pady=7)
    txtTown.grid(row=3,column=0,padx=30, pady=7)
    omFood.grid(row=4,column=0,padx=30, pady=7)
    btnEdit.grid(row=5,column=0,padx=30, pady=7)
    
    
## end EditPerson()


def UpdateData(event, name, age, town, favFood, dialog):
    selected = lstDisplay.curselection()
    people[selected[0]] = [name, age, town, favFood]
    
    lstDisplay.delete(0, tk.END)
    for person in people:
        lstDisplay.insert(tk.END, person)
        
    dialog.destroy()
    DisplayStatus("data edited successfully...")
## end UpdateData()
    
    

def DeletePerson(event):
    selected = lstDisplay.curselection()
    people.pop(selected[0])
    
    lstDisplay.delete(0, tk.END)
    for person in people:
        lstDisplay.insert(tk.END, person)
    
    DisplayStatus("data removed successfully...")
## end DeletePerson()




def ShowContextMenu(event):
    try:
            ## most everything here is stuff built into tkinter
            ## library and events (not sure what the zero is)
        mnContext.tk_popup(event.x_root, event.y_root, 0)
    finally:
            ## only needed in tkinter 8.0.x
        mnContext.grab_release()




#######################  THE GUI  ####################################


gui = tk.Tk()
gui.title("GUI Starter Template")
#gui.iconbitmap("multisizeIcon.ico")
gui.geometry("870x430")


mnMain = tk.Menu(gui)

mnFile = tk.Menu(mnMain, tearoff = 0)
mnFile.add_command(label = "Add Person", command = lambda: AddPerson(None))
mnMain.add_cascade(label = "File", menu = mnFile)

mnEdit = tk.Menu(mnMain, tearoff = 0)
mnEdit.add_command(label = "Edit Person", command = lambda: EditPerson(None))
mnMain.add_cascade(label = "Edit", menu = mnEdit)

mnView = tk.Menu(mnMain, tearoff = 0)
mnView.add_command(label = "Delete Person", command = lambda: DeletePerson(None))
mnMain.add_cascade(label = "View", menu = mnView)


mnContext = tk.Menu(gui, tearoff = 0)
mnContext.add_command(label = "Add Person", command = lambda: AddPerson(None))
mnContext.add_command(label = "Delete Person", command = lambda: DeletePerson(None))
mnContext.add_command(label = "Edit Person", command = lambda: EditPerson(None))
gui.bind("<Button-3>", ShowContextMenu)


tbMain = tk.Frame(gui, bd = 1, relief = "ridge")
picAdd = tk.PhotoImage(file = "add_person.png")
picAdd = picAdd.subsample(16)
tbbAddPerson = tk.Button(tbMain, image = picAdd)
tbbAddPerson.bind("<Button-1>", lambda event: AddPerson(event))

picDelete = tk.PhotoImage(file = "remove_person.png")
picDelete = picDelete.subsample(16)
tbbDeletePerson = tk.Button(tbMain, image = picDelete)
tbbDeletePerson.bind("<Button-1>", lambda event: DeletePerson(event))


picEdit = tk.PhotoImage(file = "edit_person.png")
picEdit = picEdit.subsample(16)
tbbEditPerson = tk.Button(tbMain, image = picEdit)
tbbEditPerson.bind("<Button-1>", lambda event: EditPerson(event))


    ## main content
pnContent = tk.PanedWindow(gui, orient=tk.HORIZONTAL, sashrelief="raised")
frmInput = tk.Frame(pnContent, bd=3, relief="groove")
frmDisplay = tk.Frame(pnContent, bd=3, relief="groove")
pnContent.add(frmInput)
pnContent.add(frmDisplay)


    ## prompt for userinput
lblName = tk.Label(frmInput, text="Name:")
txtName = tk.Entry(frmInput)

lblAge = tk.Label(frmInput, text="Age:")
txtAge = tk.Entry(frmInput)

lblTown = tk.Label(frmInput, text="Town:")
txtTown = tk.Entry(frmInput)

lblFavFood = tk.Label(frmInput, text="Fav Food")
omChosen = tk.StringVar("")
omFavFood = tk.OptionMenu(frmInput, omChosen, *favFood)


    ## display in a listbox
lblDisplay = tk.Label(frmDisplay, text="People and Stuff About Them")
lstDisplay = tk.Listbox(frmDisplay)


    ## output a greeting
lblGreet = tk.Label(frmInput)
btnAddPerson = tk.Button(frmInput, text="Add Person")
btnAddPerson.bind("<Button-1>", lambda event: AddPerson(event))


    ## create a status bar
frmStatus = tk.Frame(gui, bd = 1, relief = "sunken")
lblStatus = tk.Label(frmStatus, text="STATUS: Ready...")


    ## load the widgets on the gui
gui.config(menu = mnMain)
tbMain.pack(fill = "both", padx = 2, pady = 5)
pnContent.pack(fill = "both", pady = 5, expand=1)
frmStatus.pack(side = "bottom", fill = "both")


tbbAddPerson.grid(row = 0, column = 0, padx = 3, pady = 5)
tbbDeletePerson.grid(row = 0, column = 1, padx = 3, pady = 5)
tbbEditPerson.grid(row = 0, column = 2, padx = 3, pady = 5)

lblName.grid(row = 0, column = 0)
txtName.grid(row = 0, column = 1)
lblAge.grid(row = 1, column = 0)
txtAge.grid(row = 1, column = 1)
lblTown.grid(row = 2, column = 0)
txtTown.grid(row = 2, column = 1)
lblFavFood.grid(row=3, column=0)
omFavFood.grid(row=3, column=1)

lblDisplay.pack()
lstDisplay.pack(fill="both", padx=7, pady=7, expand=1)


btnAddPerson.grid(row = 4, column = 0, columnspan=2, sticky="NSEW")


lblStatus.pack(side = "left", fill = "both")

    ### this sets up the key press: ctrl+shift+H to run the method
        ### for a simple keypress event: "Keypress-H"
gui.bind("<Control-Shift-KeyPress-A>", lambda event: AddPerson(event))


### trivial change to show github branch
x = 3


    ## start the gui
if __name__ == "__main__":
    gui.mainloop()


























###########  more stuff here so it scrolls to a better spot  #################
