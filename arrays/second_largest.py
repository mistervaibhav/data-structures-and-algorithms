# https://www.codingninjas.com/studio/problems/ninja-and-the-second-order-elements_6581960?


def getSecondOrderElements(size: int, array: [int]) -> [int]:
    # large
    largest = array[0]
    second_largest = float("-inf")

    for index in range(1, size):
        if array[index] > largest:
            second_largest = largest
            largest = array[index]
        elif array[index] < largest and array[index] > second_largest:
            second_largest = array[index]

    # small

    smallest = array[0]
    second_smallest = float("inf")

    for index in range(1, size):
        if array[index] < smallest:
            second_smallest = smallest
            smallest = array[index]
        elif array[index] > smallest and array[index] < second_smallest:
            second_smallest = array[index]

    return [second_largest, second_smallest]
