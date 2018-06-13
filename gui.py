from tkinter import *
import SohlenConnection
import Interpreter
import Heatmap
import pyautogui
import time
import winsound

OFFSET_RIGHT = [[0 for x in range(5)]for y in range(10)]
OFFSET_LEFT = [[0 for x in range(5)]for y in range(10)]
RECHTS_VORN_SCHWELLE = 9000000
rechts_hintenSchwelle = 9000000
rechtsSeiteSchwelle = 9000000
linksVorneSchwelle = 9000000
linksHintenSchwelle = 9000000
linksSeiteSchwelle = 9000000
indexofWidget = 1
auswahl = False
mark_listbox=False
indexoflistbox = 0
activate = False
act_var = 0 

# man kann mit indexofWidget ueber alle Widgets iterieren. Das aktuell makierte Widget wird GELB
# hinterlegt. Beim Betätigen des Widgets (Klick) wird dieses kurzzeitig ROT hinterlegt.
# Unter Umstaenden muss noch eine case-Abfrage nach dem Typ des Widgets gemacht werden,
# da sich z.B. Listbox ein wenig anders verhaelt als die anderen Widgets
# (isinstance(all_widgets[indexofWidget % len(all_widgets)], Tkinter.Listbox)
#
# Steuerung:
#       Rechter Fuß vorn    -->     verringert Index -> man geht nach oben zum nächsten Widget
#       Rechter Fuß hinten  -->     erhöht Index -> man geht nach unten zum nächsten Widget
#       Linker Fuß vorn     -->     man simuliert einen "MAUS-KLICK"  auf dem angewählten Widget


def createUI():
    global indexofWidget
    top = Tk()
    top.geometry('300x500')
    top_menu = Menu(top)

    # Menuleiste mit den Set-Funktionen zur Steuerung
    top.config(menu=top_menu)
    optionsmenu = Menu(top_menu)
    top_menu.add_cascade(label="Options", menu=optionsmenu)
    optionsmenu.add_command(label="Normalize", command=setOffset)
    optionsmenu.add_command(
        label="Rechts Vorne Schwellenwert", command=setVorneRSchwelle)
    optionsmenu.add_command(
        label="Rechts Hinten Schwellenwert", command=setHintenRSchwelle)
    optionsmenu.add_command(
        label="Rechts Seite Schwellenwert", command=setSeiteRSchwelle)
    optionsmenu.add_command(
        label="Links Vorne Schwellenwert", command=setVorneLSchwelle)
    optionsmenu.add_command(
        label="Links Hinten Schwellenwert", command=setHintenLSchwelle)
    optionsmenu.add_command(
        label="Links Seite Schwellenwert", command=setSeiteLSchwelle)

    test_button1 = Button(
        top, text="Hello", activebackground="green", command=clickbutton1)
    test_button1.pack(padx=10, pady=10)

    test_listbox1 = Listbox(top)
    test_listbox1.insert(0, "Hello")
    test_listbox1.insert(1, "Bye")
    test_listbox1.pack(padx=10, pady=10)

    test_checkbox1 = Checkbutton(
        top, text="Arr! This be a Checkbox")
    test_checkbox2 = Checkbutton(
        top, text="Shiver me timbers!")
    test_checkbox1.pack(padx=10, pady=10)
    test_checkbox2.pack(padx=10, pady=10)

    var = IntVar()

    radiobutton1 = Radiobutton(
        top, text="Option 1", variable=var, value=1)
    radiobutton1.pack(anchor=W, padx=10, pady=10)

    radiobutton2 = Radiobutton(
        top, text="Option 2", variable=var, value=2)
    radiobutton2.pack(anchor=W, padx=10, pady=10)

    radiobutton3 = Radiobutton(
        top, text="Option 3", variable=var, value=3)
    radiobutton3.pack(anchor=W, padx=10, pady=10)

    run = True
    while run:
        top.after(0, read(top))
        top.after(0, iterate_gui(top))
    top.mainloop()


def iterate_gui(top):
    global indexofWidget
    global auswahl
    global mark_listbox
    global indexoflistbox
    all_widgets = top.winfo_children()

    if mark_listbox is False:
        # Widget mit aktuellem Index GELB färben
        if (indexofWidget % len(all_widgets)) != 0:
            for i in range(len(all_widgets) - 1):
                all_widgets[i + 1].config(bg=top.cget("bg"))
            for i in range(all_widgets[2].size()):
                all_widgets[2].itemconfig(i, bg=top.cget("bg"))
            all_widgets[indexofWidget % len(all_widgets)].config(bg="yellow")
            if (indexofWidget % len(all_widgets)) == 2:
                for i in range(all_widgets[2].size()):
                    all_widgets[2].itemconfig(i, bg="yellow")

        # Maus-KLICK auf aktuelles Widget simulieren
        if auswahl is True and (indexofWidget % len(all_widgets)) != 2:
            all_widgets[indexofWidget % len(all_widgets)].config(bg="red")
            x_koor = all_widgets[indexofWidget % len(all_widgets)].winfo_rootx()
            y_koor = all_widgets[indexofWidget % len(all_widgets)].winfo_rooty()
            pyautogui.mouseDown(x_koor + 10, y_koor + 10)
            time.sleep(0.5)
            pyautogui.mouseUp(x_koor + 10, y_koor + 10)
            #time.sleep(0.5)
            pyautogui.moveTo(top.winfo_rootx(),top.winfo_rooty())
    else:
        if (indexofWidget % len(all_widgets)) != 0:
            for i in range(len(all_widgets) - 1):
                all_widgets[i + 1].config(bg=top.cget("bg"))
        for i in range(all_widgets[indexofWidget % len(all_widgets)].size()):
            all_widgets[indexofWidget % len(all_widgets)].itemconfig(i, bg=top.cget("bg"))
        all_widgets[indexofWidget % len(all_widgets)].itemconfig((indexoflistbox % 2), bg = "yellow")

        # Maus-KLICK auf aktuelles Widget simulieren
        if auswahl is True:
            all_widgets[indexofWidget % len(all_widgets)].itemconfig((indexoflistbox % 2), bg = "red")
            koor = all_widgets[indexofWidget % len(all_widgets)].bbox(indexoflistbox % 2)
            x_koor= koor[0] + all_widgets[indexofWidget % len(all_widgets)].winfo_rootx()
            y_koor = koor[1] + all_widgets[indexofWidget % len(all_widgets)].winfo_rooty()
            pyautogui.mouseDown(x_koor + 10, y_koor + 10)
            time.sleep(0.5)
            pyautogui.mouseUp(x_koor + 10, y_koor + 10)
        



def read(top):
    global indexofWidget
    global auswahl
    global mark_listbox
    global indexoflistbox
    global activate
    global act_var
    all_widgets = top.winfo_children()
    
    raw_left_data = SohlenConnection.getdata("L")
    left_data = Interpreter.input_raw_data_left(raw_left_data, OFFSET_LEFT)

    raw_right_data = SohlenConnection.getdata("R")
    right_data = Interpreter.input_raw_data_right(raw_right_data, OFFSET_RIGHT)

    # Heatmap.drawHeatmap(right_data)
    Heatmap.drawHeatmap(left_data)

    if activate is True:
        if VorneRechts(right_data) and not HintenRechts(right_data) and not SeiteRechts(right_data) and not VorneLinks(left_data):
            print("vorne rechts")

            if mark_listbox is True:
                indexoflistbox = indexoflistbox - 1
            else:
                indexofWidget = indexofWidget - 1
                if (indexofWidget % len(all_widgets)) == 0:
                    indexofWidget = indexofWidget - 1

        if HintenRechts(right_data) and not VorneRechts(right_data) and not SeiteRechts(right_data):
            print("hinten rechts")
            if mark_listbox is True:
                indexoflistbox = indexoflistbox + 1
            else:
                indexofWidget = indexofWidget + 1
                if (indexofWidget % len(all_widgets)) == 0:
                    indexofWidget = indexofWidget + 1

        if not HintenRechts(right_data) and not VorneRechts(right_data) and SeiteRechts(right_data):
            print("seite rechts")
            auswahl = True
        else:
            auswahl = False
        
        if VorneLinks(left_data) and not HintenLinks(left_data) and not SeiteLinks(left_data) and not VorneRechts(right_data):
            print("vorne links")
            if isinstance(all_widgets[indexofWidget % len(all_widgets)], Listbox) is True:
                mark_listbox = True

        if HintenLinks(left_data) and not VorneLinks(left_data) and not SeiteLinks(left_data):
            print("hinten left")
            if isinstance(all_widgets[indexofWidget % len(all_widgets)], Listbox) is True:
                mark_listbox = False

        if not HintenLinks(left_data) and not VorneLinks(left_data) and SeiteLinks(left_data):
            print("seite links")

    if VorneLinks(left_data) and VorneRechts(right_data) and not HintenLinks(left_data) and not HintenRechts(right_data):
        if activate is False:
            if act_var < 3:
                act_var = act_var + 1
                print(act_var)
                winsound.Beep(800,200)
            else:
                activate = True
                print("ACTIVATE")
                winsound.Beep(1000,500)
                time.sleep(3)
        else: 
            if act_var > 0:
                act_var = act_var - 1
                print(act_var)
            else:
                activate = False
                print("DEACTIVATE")
                time.sleep(3)

def setOffset():
    global OFFSET_RIGHT
    global OFFSET_LEFT

    OFFSET_RIGHT = [[0 for x in range(5)]for y in range(10)]
    OFFSET_LEFT = [[0 for x in range(5)]for y in range(10)]

    raw_left_data = SohlenConnection.getdata("L")
    left_data = Interpreter.input_raw_data_left(raw_left_data, OFFSET_LEFT)
    OFFSET_LEFT = left_data

    raw_right_data = SohlenConnection.getdata("R")
    right_data = Interpreter.input_raw_data_right(raw_right_data, OFFSET_RIGHT)
    OFFSET_RIGHT = right_data


def setVorneRSchwelle():
    raw_right_data = SohlenConnection.getdata("R")
    right_data = Interpreter.input_raw_data_right(raw_right_data, OFFSET_RIGHT)
    rechts_vorn = 0
    for i in range(3):
        for j in range(5):
            rechts_vorn += right_data[i][j]
    global RECHTS_VORN_SCHWELLE
    RECHTS_VORN_SCHWELLE = rechts_vorn
    time.sleep(3)


def setHintenRSchwelle():
    raw_right_data = SohlenConnection.getdata("R")
    right_data = Interpreter.input_raw_data_right(raw_right_data, OFFSET_RIGHT)
    rechts_hinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            rechts_hinten += right_data[i][j]
    global rechts_hintenSchwelle
    rechts_hintenSchwelle = rechts_hinten
    time.sleep(3)


def setSeiteRSchwelle():
    raw_right_data = SohlenConnection.getdata("R")
    right_data = Interpreter.input_raw_data_right(raw_right_data, OFFSET_RIGHT)
    rechts_seite = 0
    for i in 4, 5, 6, 7:
        for j in 3, 4:
            rechts_seite += right_data[i][j]
    global rechtsSeiteSchwelle
    rechtsSeiteSchwelle = rechts_seite
    time.sleep(3)


def setVorneLSchwelle():
    raw_left_data = SohlenConnection.getdata("L")
    links_data = Interpreter.input_raw_data_left(raw_left_data, OFFSET_LEFT)
    links_vorne = 0
    for i in range(3):
        for j in range(5):
            links_vorne += links_data[i][j]
    global linksVorneSchwelle
    linksVorneSchwelle = links_vorne
    time.sleep(3)


def setHintenLSchwelle():
    raw_left_data = SohlenConnection.getdata("L")
    left_data = Interpreter.input_raw_data_left(raw_left_data, OFFSET_LEFT)
    links_hinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            links_hinten += left_data[i][j]
    global linksHintenSchwelle
    linksHintenSchwelle = links_hinten
    time.sleep(3)


def setSeiteLSchwelle():
    raw_left_data = SohlenConnection.getdata("L")
    left_data = Interpreter.input_raw_data_left(raw_left_data, OFFSET_LEFT)
    links_seite = 0
    for i in 4, 5, 6, 7:
        for j in 0, 1:
            links_seite += left_data[i][j]
    global linksSeiteSchwelle
    linksSeiteSchwelle = links_seite
    time.sleep(3)


def VorneRechts(Data):
    rechts_vorn = 0
    for i in range(3):
        for j in range(5):
            rechts_vorn += Data[i][j]

    if rechts_vorn >= RECHTS_VORN_SCHWELLE - 20000:
        return True
    return False


def HintenRechts(Data):
    rechts_hinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            rechts_hinten += Data[i][j]

    if rechts_hinten >= rechts_hintenSchwelle - 20000:
        return True
    return False


def SeiteRechts(Data):
    rechts_seite = 0
    for i in 4, 5, 6, 7:
        for j in 3, 4:
            rechts_seite += Data[i][j]

    if rechts_seite >= rechtsSeiteSchwelle - 20000:
        return True
    return False


def VorneLinks(Data):
    links_vorne = 0
    for i in range(3):
        for j in range(5):
            links_vorne += Data[i][j]

    if links_vorne >= linksVorneSchwelle - 20000:
        return True
    return False


def HintenLinks(Data):
    links_hinten = 0
    for i in 7, 8, 9:
        for j in range(5):
            links_hinten += Data[i][j]

    if links_hinten >= linksHintenSchwelle - 20000:
        return True
    return False


def SeiteLinks(Data):
    links_seite = 0
    for i in 4, 5, 6, 7:
        for j in 0, 1:
            links_seite += Data[i][j]

    if links_seite >= linksSeiteSchwelle - 20000:
        return True
    return False


def clickbutton1():
    print("hello")
