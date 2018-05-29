import Heatmap
import SohlenConnection
import Interpreter

run = True
while run:
    #raw_left_data = SohlenConnection.getData("L")
    #left_data = Interpreter.inputRawDataLeft(raw_left_data)

    raw_right_data = SohlenConnection.getData("R")
    right_data = Interpreter.inputRawDataRight(raw_right_data)

    Heatmap.drawHeatmap(right_data)