from tkinter import *
import SohlenConnection, Interpreter,Heatmap

offsetRight = [[0 for x in range(5)]for y in range(10)]
offsetLeft = [[0 for x in range(5)]for y in range(10)]


def createUI() :
    top = Tk()
    top_menu = Menu(top)      
    top.config(menu = top_menu)
    OptionsMenu = Menu(top_menu)
    top_menu.add_cascade(label = "Options", menu=OptionsMenu)
    OptionsMenu.add_command(label = "Normalize", command=setOffset)

    indexofWidget = 2 # das hier veraendern, um ueber Widgets zu iterieren

    testButton1 = Button(top, text = "Hello", activebackground = "green")
    testButton1.pack()

    testListbox1 = Listbox(top, highlightcolor = "green")
    testListbox1.insert(1, "Hello")
    testListbox1.insert(2, "Bye")
    testListbox1.pack()

    testCheckBox1 = Checkbutton(top, text = "Arr! This be a Checkbox", activebackground = "green")
    testCheckBox2 = Checkbutton(top, text = "Shiver me timbers!", activebackground = "green")
    testCheckBox1.pack()
    testCheckBox2.pack()

    var = IntVar()

    R1 = Radiobutton(top, text="Option 1", variable=var, value=1, activebackground = "green")
    R1.pack( anchor = W )
    R2 = Radiobutton(top, text="Option 2", variable=var, value=2, activebackground = "green")
    R2.pack( anchor = W )
    R3 = Radiobutton(top, text="Option 3", variable=var, value=3, activebackground = "green")
    R3.pack( anchor = W)

    allWidgets = top.winfo_children()
    print(allWidgets[indexofWidget % len(allWidgets)])
    print(allWidgets)
    allWidgets[indexofWidget % len(allWidgets)].config(bg = "yellow")
    allWidgets[indexofWidget % len(allWidgets)].config(state = ACTIVE)   
    
    # man kann mit indexofWidget ueber alle Widgets interieren. Allgemein muss man dann den State des letzten auf NORMAL
    # und den state des aktuellen auf ACTIVE setzen, damit der aktuelle mit der eingestellten Farbe hervorgehoben wird.
    # Unter Umstaenden muss noch eine case-Abfrage nach dem Typ des Widgets gemacht werden, da sich z.B. Listbox ein wenig
    # anders verhaelt als die anderen Widgets (isinstance(allWidgets[indexofWidget % len(allWidgets)], Tkinter.Listbox)


    top.after(1000,read())
    top.mainloop()



def setOffset():
    global offsetRight 
    global offsetLeft
    
    offsetRight = [[0 for x in range(5)]for y in range(10)]
    offsetLeft = [[0 for x in range(5)]for y in range(10)]


    #raw_left_data = SohlenConnection.getData("L")
    #left_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)
    #offsetLeft = left_data

    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
    offsetRight = right_data
    print("hallo")

def read():
    run = True
    while run:
        #raw_left_data = SohlenConnection.getData("L")
        #left_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)

        raw_right_data = SohlenConnection.getData("R")
        right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
        #print(offsetRight)

        Heatmap.drawHeatmap(right_data)
    