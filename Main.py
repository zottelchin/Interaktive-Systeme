import Heatmap
import SohlenConnection
import Interpreter
import gui

offsetRight = [[0 for x in range(5)]for y in range(10)]
offsetLeft = [[0 for x in range(5)]for y in range(10)]

def setOffset():
    raw_left_data = SohlenConnection.getData("L")
    left_data = Interpreter.inputRawDataLeft(raw_left_data)
    offsetLeft = left_data

    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data)
    offsetRight = right_data

run = True
while run:
    #raw_left_data = SohlenConnection.getData("L")
    #left_data = Interpreter.inputRawDataLeft(raw_left_data)

    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data)

    Heatmap.drawHeatmap(right_data)

    gui.createUI()