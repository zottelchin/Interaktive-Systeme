import Heatmap
import SohlenConnection
import Interpreter

run = True
while run:
    sole_data = SohlenConnection.getData("L")
    data = Interpreter.inputRawData(sole_data)
    Heatmap.drawHeatmap(data)