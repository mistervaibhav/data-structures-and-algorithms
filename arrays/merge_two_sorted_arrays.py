def sortedArray(first: [int], second: [int]) -> [int]:
    """Brute force"""
    return sorted(set(first + second))


def sortedArray(first: [int], second: [int]) -> [int]:
    """ "Optimal Solution using 2 pointers"""
    firstSize = len(first)
    secondSize = len(second)

    i = 0
    j = 0

    union = list()

    while i < firstSize and j < secondSize:
        if first[i] <= second[j]:
            if len(union) == 0 or union[-1] != first[i]:
                union.append(first[i])

            i += 1

        else:
            if len(union) == 0 or union[-1] != second[j]:
                union.append(second[j])

            j += 1

    while i < firstSize:
        if len(union) == 0 or union[-1] != first[i]:
            union.append(first[i])

        i += 1

    while j < secondSize:
        if len(union) == 0 or union[-1] != second[j]:
            union.append(second[j])

        j += 1

    return union
