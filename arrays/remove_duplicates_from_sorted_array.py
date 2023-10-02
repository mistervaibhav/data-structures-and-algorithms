def removeDuplicates(array, size):
    """LOL solution"""
    return list(set(array))


def removeDuplicates(array, size):
    """Optimal
    Using 2 pointers
    """
    i = 0
    j = 1

    while j < size:
        if array[j] != array[i]:
            array[i + 1] = array[j]
            i += 1
        j += 1

    return i + 1
