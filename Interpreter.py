import array
import sys


def normalize(matrix, offset):
    for i in range(5):
        for j in range(10):
            matrix[j][i] = matrix[j][i] - offset[j][i]
            if matrix[j][i] < 0:
                matrix[j][i] = 0
    # print(matrix)
    return matrix


def input_raw_data_left(data, offset):
    matrix = [[0 for x in range(5)]for y in range(10)]
    anzahl = convert_hex_to_int(data[4:6])
    temp_array = array.array('i')
    for i in range(0, anzahl):
        temp = umrechnung(convert_hex_to_int(data[6 + i * 2:8 + i * 2]))
        temp_array.append(temp)

    for i in range(5):
        for j in range(10):
            matrix[j][i] = temp_array[180 + (i * -16) + j]

    return normalize(matrix, offset)


def input_raw_data_right(data, offset):
    matrix = [[0 for x in range(5)] for y in range(10)]
    anzahl = convert_hex_to_int(data[4:6])
    temp_array = array.array('i')
    for i in range(0, anzahl):
        temp = umrechnung(convert_hex_to_int(data[6 + i * 2:8 + i * 2]))
        temp_array.append(temp)

    for i in range(5):
        for j in range(10):
            matrix[j][i] = temp_array[41 + i + (16 * j)]

    return normalize(matrix, offset)


def convert_hex_to_int(hexarray):
    return int.from_bytes(hexarray, byteorder='big')


def umrechnung(a_int):
    m_range0_offset = 0
    m_range1_offset = 1843
    m_range2_offset = 3502
    m_range3_offset = 5161

    if a_int > m_range3_offset:
        a_int = ((a_int - m_range3_offset) + 184) * 1000
    elif a_int > m_range2_offset:
        a_int = ((a_int - m_range2_offset) + 184) * 100
    elif a_int > m_range1_offset:
        a_int = ((a_int - m_range1_offset) + 184) * 10
    elif a_int > m_range0_offset:
        a_int = (a_int - m_range0_offset) * 1
    return a_int
