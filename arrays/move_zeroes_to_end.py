# https://www.codingninjas.com/studio/problems/ninja-and-the-zero-s_6581958


def moveZeros(size: int, array: [int]) -> [int]:
    """Extra space"""
    auxiliary = [0] * size
    i = 0

    for index in range(size):
        if array[index] != 0:
            auxiliary[i] = array[index]
            i += 1

    return auxiliary


def moveZeros(size: int, array: [int]) -> [int]:
    """In place, without extra space
    2 pointer
    """

    j = -1

    for index in range(size):
        if array[index] == 0:
            j = index
            break

    # array has no zeroes
    if j == -1:
        return array

    for index in range(j, size):
        if array[index] != 0:
            temp = array[index]
            array[index] = array[j]
            array[j] = temp

            j += 1

    return array
