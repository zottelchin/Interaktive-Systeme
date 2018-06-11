from tkinter import *
import SohlenConnection
import Interpreter
import Heatmap
import pyautogui
import time

offsetRight = [[0 for x in range(5)]for y in range(10)]
offsetLeft = [[0 for x in range(5)]for y in range(10)]
rechtsVorneSchwelle = 9000000
rechtsHintenSchwelle = 9000000
rechtsSeiteSchwelle = 9000000
linksVorneSchwelle = 9000000
linksHintenSchwelle = 9000000
linksSeiteSchwelle = 9000000
indexofWidget = 1
auswahl=False


def createUI():
    global indexofWidget
    top = Tk()
    top.geometry('300x500')
    top_menu = Menu(top)
    top.config(menu=top_menu)
    OptionsMenu = Menu(top_menu)
    top_menu.add_cascade(label="Options", menu=OptionsMenu)
    OptionsMenu.add_command(label="Normalize", command=setOffset)
    OptionsMenu.add_command(
        label="Rechts Vorne Schwellenwert", command=setVorneRSchwelle)
    OptionsMenu.add_command(
        label="Rechts Hinten Schwellenwert", command=setHintenRSchwelle)
    OptionsMenu.add_command(
        label="Rechts Seite Schwellenwert", command=setSeiteRSchwelle)
    OptionsMenu.add_command(
        label="Links Vorne Schwellenwert", command=setVorneLSchwelle)
    OptionsMenu.add_command(
        label="Links Hinten Schwellenwert", command=setHintenLSchwelle)
    OptionsMenu.add_command(
        label="Links Seite Schwellenwert", command=setSeiteLSchwelle)

    # indexofWidget = 1 # das hier veraendern, um ueber Widgets zu iterieren

    testButton1 = Button(top, text="Hello", activebackground="green",highlightcolor="green",command=clickbutton1)
    testButton1.pack(padx=10,pady=10)

    testListbox1 = Listbox(top, highlightcolor="green")
    testListbox1.insert(1, "Hello")
    testListbox1.insert(2, "Bye")
    testListbox1.pack(padx=10,pady=10)

    testCheckBox1 = Checkbutton(
        top, text="Arr! This be a Checkbox", activebackground="green")
    testCheckBox2 = Checkbutton(
        top, text="Shiver me timbers!", activebackground="green")
    testCheckBox1.pack(padx=10,pady=10)
    testCheckBox2.pack(padx=10,pady=10)

    var = IntVar()

    R1 = Radiobutton(top, text="Option 1", variable=var,
                     value=1, activebackground="green")
    R1.pack(anchor=W,padx=10,pady=10)
    R2 = Radiobutton(top, text="Option 2", variable=var,
                     value=2, activebackground="green")
    R2.pack(anchor=W,padx=10,pady=10)
    R3 = Radiobutton(top, text="Option 3", variable=var,
                     value=3, activebackground="green")
    R3.pack(anchor=W,padx=10,pady=10)

    #allWidgets = top.winfo_children()
    #print(allWidgets[indexofWidget % len(allWidgets)])
    # print(allWidgets)
    #allWidgets[indexofWidget % len(allWidgets)].config(bg = "yellow")
    #allWidgets[indexofWidget % len(allWidgets)].config(state = "active")

    # man kann mit indexofWidget ueber alle Widgets interieren. Allgemein muss man dann den State des letzten auf NORMAL
    # und den state des aktuellen auf ACTIVE setzen, damit der aktuelle mit der eingestellten Farbe hervorgehoben wird.
    # Unter Umstaenden muss noch eine case-Abfrage nach dem Typ des Widgets gemacht werden, da sich z.B. Listbox ein wenig
    # anders verhaelt als die anderen Widgets (isinstance(allWidgets[indexofWidget % len(allWidgets)], Tkinter.Listbox)
    run=True
    while run:
        top.after(0, read())
        top.after(0, iterate_gui(top))
    top.mainloop()


def iterate_gui(top):
    global indexofWidget
    global auswahl
    #print("test")
    allWidgets = top.winfo_children()
    #print(allWidgets[indexofWidget % len(allWidgets)])
    #print(allWidgets)
    if (indexofWidget % len(allWidgets)) != 0:
        for i in range(len(allWidgets)-1):
            allWidgets[i+1].config(bg=top.cget("bg"))
            
        allWidgets[indexofWidget % len(allWidgets)].config(bg="yellow")
        allWidgets[indexofWidget % len(allWidgets)].config(state="normal")
    if auswahl==True:
        allWidgets[indexofWidget % len(allWidgets)].config(bg="red")
        x=allWidgets[indexofWidget % len(allWidgets)].winfo_rootx()
        y=allWidgets[indexofWidget % len(allWidgets)].winfo_rooty()
        pyautogui.mouseDown(x+10,y+10)
        time.sleep(0.5)
        pyautogui.mouseUp(x+10,y+10)


def setOffset():
    global offsetRight
    global offsetLeft

    offsetRight = [[0 for x in range(5)]for y in range(10)]
    offsetLeft = [[0 for x in range(5)]for y in range(10)]

    raw_left_data = SohlenConnection.getData("L")
    left_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)
    offsetLeft = left_data

    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
    offsetRight = right_data


def setVorneRSchwelle():
    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
    rechtsVorne = 0
    for i in range(3):
        for j in range(5):
            rechtsVorne += right_data[i][j]
    global rechtsVorneSchwelle
    rechtsVorneSchwelle = rechtsVorne
    time.sleep(3)


def setHintenRSchwelle():
    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
    rechtsHinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            rechtsHinten += right_data[i][j]
    global rechtsHintenSchwelle
    rechtsHintenSchwelle = rechtsHinten
    time.sleep(3)


def setSeiteRSchwelle():
    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
    rechtsSeite = 0
    for i in 4, 5, 6, 7:
        for j in 3, 4:
            rechtsSeite += right_data[i][j]
    global rechtsSeiteSchwelle
    rechtsSeiteSchwelle = rechtsSeite
    time.sleep(3)


def setVorneLSchwelle():
    raw_left_data = SohlenConnection.getData("L")
    links_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)
    linksVorne = 0
    for i in range(3):
        for j in range(5):
            linksVorne += links_data[i][j]
    global linksVorneSchwelle
    linksVorneSchwelle = linksVorne
    time.sleep(3)


def setHintenLSchwelle():
    raw_left_data = SohlenConnection.getData("L")
    left_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)
    linksHinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            linksHinten += left_data[i][j]
    global linksHintenSchwelle
    linksHintenSchwelle = linksHinten
    time.sleep(3)


def setSeiteLSchwelle():
    raw_left_data = SohlenConnection.getData("L")
    left_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)
    linksSeite = 0
    for i in 4, 5, 6, 7:
        for j in 0, 1:
            linksSeite += left_data[i][j]
    global linksSeiteSchwelle
    linksSeiteSchwelle = linksSeite
    time.sleep(3)


def read():
    global indexofWidget
    global auswahl
    #run = True
    # while run:
    raw_left_data = SohlenConnection.getData("L")
    left_data = Interpreter.inputRawDataLeft(raw_left_data, offsetLeft)

    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data, offsetRight)
    # print(indexofWidget)

    # Heatmap.drawHeatmap(right_data)
    Heatmap.drawHeatmap(left_data)

    if VorneRechts(right_data) and not HintenRechts(right_data) and not SeiteRechts(right_data):
        print("vorne rechts")
        indexofWidget = indexofWidget + 1

    if HintenRechts(right_data) and not VorneRechts(right_data) and not SeiteRechts(right_data):
        print("hinten rechts")
        indexofWidget = indexofWidget - 1

    if not HintenRechts(right_data) and not VorneRechts(right_data) and SeiteRechts(right_data):
        print("seite rechts")

    if VorneLinks(left_data) and not HintenLinks(left_data) and not SeiteLinks(left_data):
        print("vorne links")
        auswahl=True
    else:
        auswahl=False

    if HintenLinks(left_data) and not VorneLinks(left_data) and not SeiteLinks(left_data):
        print("hinten left")

    if not HintenLinks(left_data) and not VorneLinks(left_data) and SeiteLinks(left_data):
        print("seite links")


def VorneRechts(Data):
    rechtsVorne = 0
    for i in range(3):
        for j in range(5):
            rechtsVorne += Data[i][j]

    if rechtsVorne >= rechtsVorneSchwelle - 20000:
        return True
    return False


def HintenRechts(Data):
    rechtsHinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            rechtsHinten += Data[i][j]

    if rechtsHinten >= rechtsHintenSchwelle - 20000:
        return True
    return False


def SeiteRechts(Data):
    rechtsSeite = 0
    for i in 4, 5, 6, 7:
        for j in 3, 4:
            rechtsSeite += Data[i][j]

    if rechtsSeite >= rechtsSeiteSchwelle - 20000:
        return True
    return False


def VorneLinks(Data):
    linksVorne = 0
    for i in range(3):
        for j in range(5):
            linksVorne += Data[i][j]

    if linksVorne >= linksVorneSchwelle - 20000:
        return True
    return False


def HintenLinks(Data):
    linksHinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            linksHinten += Data[i][j]

    if linksHinten >= linksHintenSchwelle - 20000:
        return True
    return False


def SeiteLinks(Data):
    linksSeite = 0
    for i in 4, 5, 6, 7:
        for j in 0, 1:
            linksSeite += Data[i][j]

    if linksSeite >= linksSeiteSchwelle - 20000:
        return True
    return False

def clickbutton1():
    print("hello")