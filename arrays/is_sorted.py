# https://www.codingninjas.com/studio/problems/ninja-and-the-sorted-check_6581957


def isSorted(size: int, array: [int]) -> int:
    for index in range(1, size):
        if array[index - 1] > array[index]:
            return 0

    return 1
