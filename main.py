import array

def inputRawData(input):
    Matrix = [[0 for x in range(10)]for y in range(5)]
    input = input.replace(" ", "")
    Anzahl = convertHex(input[8:12])
    print(Anzahl)
    tempArr = array.array('i')
    for i in range(0, Anzahl):
        temp = doStuff(convertHex(input[12+i*4:16+i*4]))
        print(temp)
        if temp > 15:
            print(temp)
            tempArr.append(temp)
    #print(tempArr.tostring())
    for x in range(5):
        for y in range(10):
            pass
            #Matrix[x][y] = tempArr[x*5+y]
    print(Matrix)
    return

def convertHex(input):
    return int(input, 16)

def doStuff(a):
    M_RANGE0_OFFSET = 0
    M_RANGE1_OFFSET = 1843
    M_RANGE2_OFFSET = 3502
    M_RANGE3_OFFSET = 5161

    if a > M_RANGE0_OFFSET:
        a = ((a - M_RANGE3_OFFSET) + 184) * 1000
    elif a > M_RANGE2_OFFSET:
        a = ((a - M_RANGE2_OFFSET) + 184) * 100
    elif a > M_RANGE1_OFFSET:
        a = ((a - M_RANGE1_OFFSET) + 184) * 10
    elif a > M_RANGE0_OFFSET:
        a = (a - M_RANGE0_OFFSET) * 1
    return a

# Main Method
print("Unbelastet 1")
inputRawData("ff ff 00 02 01 00 00 02 00 00 00 01 00 00 00 00   " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 " +
                    "    00 00 00 02 00 00 00 00 00 00 00 00 00 05 00 00  " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   " +
                    "    00 01 00 00 00 02 00 00 00 00 00 00 00 00 00 00 " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  " +
                    "    00 00 00 05 00 00 00 04 00 00 00 04 00 00 00 00   " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  " +
                    "    00 04 00 00 00 07 00 00 00 05 00 00 00 04 00 00   " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   " +
                    "    00 00 00 05 00 00 00 07 00 00 00 06 00 00 00 00  " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  " +
                    "    00 00 00 00 00 00 00 00 00 09 00 00 00 07 00 00   " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   " +
                    "    00 00 00 00 00 01 00 00 00 00 00 00 00 00 01 6a  " +
                    "    03 6d 03 17 04 0a 03 a7 04 b8 03 d8 03 15 01 28  " +
                    "    00 65 00 05 00 00 00 03 00 00 00 00 00 00 02 7d   " +
                    "    05 a0 05 76 06 d2 05 d6 06 b7 05 ec 05 57 02 04   " +
                    "    00 d4 00 00 00 04 00 00 00 04 00 00 00 01 02 b9   " +
                    "    05 66 05 61 06 34 04 df 06 67 05 92 04 34 02 60   " +
                    "    00 df 00 08 00 00 00 06 00 00 00 05 00 00 03 05   " +
                    "    05 da 05 8f 05 99 04 88 05 92 04 16 03 23 01 f5   " +
                    "    00 bd 00 00 00 08 00 00 00 06 00 00 00 06 02 cb   " +
                    "    07 2f 05 96 05 70 04 2a 04 85 03 3d 02 9e 01 88   " +
                    "    00 83 00 00 00 00 00 08 00 00 00 09 00 00 00 00   " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  " +
                    "    00 00 00 02 00 00 00 00 00 00 00 00 00 08 00 00  " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   " +
                    "    00 00 00 00 00 02 00 00 00 06 00 00 00 05 00 00   " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00   " +
                    "    00 00 00 00 00 00 00 08 00 00 00 0a 00 00 00 00  " +
                    "    00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00  " +
                    "    00 00 00 03 00 00                             ")