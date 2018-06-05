import array
import sys

def normalize(Matrix, offset):
    for i in range(5):
        for j in range(10):
            Matrix[j][i] = Matrix[j][i] - offset[j][i]
            if Matrix[j][i]<0:
                Matrix[j][i]=0
    #print(Matrix)
    return Matrix

def inputRawDataLeft(data, offset):
    Matrix = [[0 for x in range(5)]for y in range(10)]
    anzahl = convertHexToInt(data[4:6])
    tempArr = array.array('i')
    for i in range(0, anzahl):
        temp = umrechnung(convertHexToInt(data[6+i*2:8+i*2]))
        tempArr.append(temp)

    for i in range(5):
        for j in range(10):
            Matrix[j][i] = tempArr[180+(i*-16)+j]

    return normalize(Matrix, offset)
    

def inputRawDataRight(data, offset):
    Matrix = [[0 for x in range(5)] for y in range(10)]
    anzahl = convertHexToInt(data[4:6])
    tempArr = array.array('i')
    for i in range(0, anzahl):
        temp = umrechnung(convertHexToInt(data[6 + i * 2:8 + i * 2]))
        tempArr.append(temp)

    for i in range(5):
        for j in range(10):
            Matrix[j][i] = tempArr[41+i+(16*j)]

    return normalize(Matrix, offset)
    

def convertHexToInt(hexarray):
    return int.from_bytes(hexarray, byteorder='big')

def umrechnung(a):
    M_RANGE0_OFFSET = 0
    M_RANGE1_OFFSET = 1843
    M_RANGE2_OFFSET = 3502
    M_RANGE3_OFFSET = 5161

    if a > M_RANGE3_OFFSET:
        a = ((a - M_RANGE3_OFFSET) + 184) * 1000
    elif a > M_RANGE2_OFFSET:
        a = ((a - M_RANGE2_OFFSET) + 184) * 100
    elif a > M_RANGE1_OFFSET:
        a = ((a - M_RANGE1_OFFSET) + 184) * 10
    elif a > M_RANGE0_OFFSET:
        a = (a - M_RANGE0_OFFSET) * 1
    return a





