import array


def inputRawData(data):
    Matrix = [[0 for x in range(10)]for y in range(5)]
    #data = data.replace("\x", "")
    Anzahl = convertHexToInt(data[8:12])
    print(Anzahl)
    tempArr = array.array('i')
    for i in range(0, Anzahl):
        temp = umrechnung(convertHexToInt(data[12+i*4:16+i*4]))
        print(temp)
        if temp > 15:
            print(temp)
            tempArr.append(temp)
    print(tempArr)
    for x in 0,1,2,3,4:
        for y in 0,1,2,3,4,5,6,7,8,9:
            Matrix[x][y] = tempArr[x*10+y]
    print(Matrix)
    return Matrix

def convertHexToInt(hexarray):
    return int(hexarray, 16)

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





