# https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278


def rotateArray(array: [], size: int) -> []:
    """
    Swap all the elements from left to right
    i <-> i + 1
    """

    for index in range(size - 1):
        temp = array[index]
        array[index] = array[index + 1]
        array[index + 1] = temp

    return array
