import serial

def getData(side):
    if side == "L":
        port = "COM4"
    else:
        if side == "R":
            port = "COM3"
        else:
            print("Bitte L oder R")
            return 1
    ser = serial.Serial(port=port, baudrate=115200)
    ser.write(b'\x02')
    res = ser.read(518)
    return res
