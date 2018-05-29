import tkinter 

def createUI() :
    top = tkinter.Tk()

    testButton1 = tkinter.Button(top, text = "Hello")
    testButton1.pack()

    testListbox1 = tkinter.Listbox(top)
    testListbox1.insert(1, "HEllo")
    testListbox1.insert(2, "Bye")
    testListbox1.pack()

    testCheckBox1 = tkinter.Checkbutton(top, text = "Arr! This be a Checkbox")
    testCheckBox2 = tkinter.Checkbutton(top, text = "Shiver me timbers!")
    testCheckBox1.pack()
    testCheckBox2.pack()

    var = tkinter.IntVar()

    R1 = tkinter.Radiobutton(top, text="Option 1", variable=var, value=1)
    R1.pack( anchor = tkinter.W )
    R2 = tkinter.Radiobutton(top, text="Option 2", variable=var, value=2)
    R2.pack( anchor = tkinter.W )
    R3 = tkinter.Radiobutton(top, text="Option 3", variable=var, value=3)
    R3.pack( anchor = tkinter.W)

    top.mainloop()
