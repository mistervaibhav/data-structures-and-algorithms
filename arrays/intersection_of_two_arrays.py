# https://www.codingninjas.com/studio/problems/intersection-of-2-arrays_1082149


def intersection_of_two_arrays(first, second):
    """Brute force method"""
    """throws TLE"""

    second_visited = [False] * len(second)
    intersection = list()

    for item in first:
        for index in range(len(second)):
            if second[index] == item and second_visited[index] is False:
                intersection.append(item)
                second_visited[index] = True
                break

            if second[index] > item:
                break

    return intersection


def intersection_of_two_arrays(first, second):
    """Optimal Solution"""
    """Using two pointers"""

    firstSize = len(first)
    secondSize = len(second)

    i = 0
    j = 0

    intersection = list()

    while i < firstSize and j < secondSize:
        if first[i] < second[j]:
            i += 1
        elif first[i] > second[j]:
            j += 1
        else:
            intersection.append(first[i])
            i += 1
            j += 1

    return intersection
