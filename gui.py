from tkinter import *

def createUI() :
    top = Tk()

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


    top.mainloop()
