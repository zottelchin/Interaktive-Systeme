import serial

class SohlenConnection:

    ser = serial.Serial(port='COM4',baudrate=11520,timeout=10)
    print(ser.isOpen())
    values = bytearray([0x02])
    print(values)
    print("Write {} bytes".format(values))
    print(ser.in_waiting)
    print(ser.out_waiting)
    res = ser.read(10)
    print(res)
    ser.close()