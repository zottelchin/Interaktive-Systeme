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

    testButton1 = Button(top, text = "Hello", activebackground = "green")
    testButton1.pack()

    testListbox1 = Listbox(top)
    testListbox1.insert(1, "Hello")
    testListbox1.insert(2, "Bye")
    testListbox1.pack()

    testCheckBox1 = Checkbutton(top, text = "Arr! This be a Checkbox")
    testCheckBox2 = Checkbutton(top, text = "Shiver me timbers!")
    testCheckBox1.pack()
    testCheckBox2.pack()

    var = IntVar()

    R1 = Radiobutton(top, text="Option 1", variable=var, value=1)
    R1.pack( anchor = W )
    R2 = Radiobutton(top, text="Option 2", variable=var, value=2)
    R2.pack( anchor = W )
    R3 = Radiobutton(top, text="Option 3", variable=var, value=3)
    R3.pack( anchor = W)

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
    