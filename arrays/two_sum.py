# https://www.codingninjas.com/studio/problems/reading_6845742


def read(n: int, book: [int], target: int) -> str:
    """Brute force"""
    # O(n^2)

    for i in range(n):
        for j in range(1, n):
            if book[i] + book[j] == target:
                return "YES"

    return "NO"


def read(n: int, book: [int], target: int) -> str:
    """Better approach using hashing"""
    # time = O(n * log(n))
    # space = O(n)

    store = dict()

    for item in book:
        if target - item in store:
            return "YES"

        if store.get(item) is None:
            store[item] = 1

        store[item] += 1

    return "NO"


def read(n: int, book: [int], target: int) -> str:
    """Optimal solution using 2 pointers"""
    # greedy approach
    # time = O(n * log(n))
    # space = O(n)

    left = 0
    right = n - 1

    book = sorted(book)

    while left <= right:
        addition = book[left] + book[right]
        if addition == target:
            return "YES"
        elif addition > target:
            right -= 1
        else:
            left += 1

    return "NO"
