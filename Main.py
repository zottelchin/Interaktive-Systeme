import Heatmap
import SohlenConnection
import Interpreter
import gui
from multiprocessing import Process
import threading


gui.createUI()

#def read():
#    run = True
#    while run:
        #raw_left_data = SohlenConnection.getData("L")
        #left_data = Interpreter.inputRawDataLeft(raw_left_data, gui.offsetLeft)

#        raw_right_data = SohlenConnection.getData("R")
#        right_data = Interpreter.inputRawDataRight(raw_right_data, gui.offsetRight)
        #print(gui.offsetRight)

#        Heatmap.drawHeatmap(right_data)
    


#if __name__ == '__main__':
#    p1 = Process(target=gui.createUI())
#    p1.start()
#    p2 = Process(target=read())
#    p2.start()
#    p1.join()
#    p2.join()
