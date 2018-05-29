import array
import sys


def inputRawData(data):
    Matrix = [[0 for x in range(10)]for y in range(5)]
    anzahl = convertHexToInt(data[4:6])
    tempArr = array.array('i')
    for i in range(0, anzahl):
        temp = umrechnung(convertHexToInt(data[6+i*2:8+i*2]))
        tempArr.append(temp)
    Matrix[0][0] = tempArr[115]
    Matrix[0][1] = tempArr[116]
    Matrix[0][2] = tempArr[117]
    Matrix[0][3] = tempArr[118]
    Matrix[0][4] = tempArr[119]
    Matrix[0][5] = tempArr[120]
    Matrix[0][6] = tempArr[121]
    Matrix[0][7] = tempArr[122]
    Matrix[0][8] = tempArr[123]
    Matrix[0][9] = tempArr[124]

    Matrix[1][0] = tempArr[131]
    Matrix[1][1] = tempArr[132]
    Matrix[1][2] = tempArr[133]
    Matrix[1][3] = tempArr[134]
    Matrix[1][4] = tempArr[135]
    Matrix[1][5] = tempArr[136]
    Matrix[1][6] = tempArr[137]
    Matrix[1][7] = tempArr[138]
    Matrix[1][8] = tempArr[139]
    Matrix[1][9] = tempArr[140]

    Matrix[2][1] = tempArr[147]
    Matrix[2][0] = tempArr[148]
    Matrix[2][2] = tempArr[149]
    Matrix[2][3] = tempArr[150]
    Matrix[2][4] = tempArr[151]
    Matrix[2][5] = tempArr[152]
    Matrix[2][6] = tempArr[153]
    Matrix[2][7] = tempArr[154]
    Matrix[2][8] = tempArr[155]
    Matrix[2][9] = tempArr[156]

    Matrix[3][0] = tempArr[163]
    Matrix[3][1] = tempArr[164]
    Matrix[3][2] = tempArr[165]
    Matrix[3][3] = tempArr[166]
    Matrix[3][4] = tempArr[167]
    Matrix[3][5] = tempArr[168]
    Matrix[3][6] = tempArr[169]
    Matrix[3][7] = tempArr[170]
    Matrix[3][8] = tempArr[171]
    Matrix[3][9] = tempArr[172]

    Matrix[4][0] = tempArr[179]
    Matrix[4][1] = tempArr[180]
    Matrix[4][2] = tempArr[181]
    Matrix[4][3] = tempArr[182]
    Matrix[4][4] = tempArr[183]
    Matrix[4][5] = tempArr[184]
    Matrix[4][6] = tempArr[185]
    Matrix[4][7] = tempArr[186]
    Matrix[4][8] = tempArr[187]
    Matrix[4][9] = tempArr[188]
    return Matrix

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





