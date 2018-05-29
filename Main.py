import Heatmap
import SohlenConnection
import Interpreter

#Heatmap.drawTest()
sole_data = SohlenConnection.getData("L")
data = Interpreter.inputRawData(sole_data)

print(data)