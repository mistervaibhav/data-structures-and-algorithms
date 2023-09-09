# https://www.codingninjas.com/studio/problems/linear-search_6922070


def linearSearch(n: int, num: int, arr: [int]) -> int:
    if num in arr:
        return arr.index(num)

    return -1
