import sys

sys.setrecursionlimit(1000000000)


def spaceString(string):
    """
    finds all possible strings that can be made by placing spaces (zero or one) in between them.

    https://practice.geeksforgeeks.org/problems/print-all-possible-strings/1
    """

    if len(string) == 0:
        return []

    if len(string) == 1:
        return [string]

    output = list()

    smallOutput = spaceString(string[1:])

    for smallString in smallOutput:
        output.append(string[0] + smallString)
        output.append(string[0] + " " + smallString)

    output.sort()

    return output[::-1]
