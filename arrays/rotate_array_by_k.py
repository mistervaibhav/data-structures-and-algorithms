
def reverse(array, start, end):

    while(start < end):
        temp = array[start]
        array[start] = array[end]
        array[end] = temp

        start += 1
        end -= 1
 
def rotateArray(array: list, k: int) -> list:
    size = len(array)
    k = k % size
    if k < 0:
        k = k + size

    reverse(array, 0, k - 1)
    reverse(array, k, size - 1)
    reverse(array, 0, size - 1)

    return array