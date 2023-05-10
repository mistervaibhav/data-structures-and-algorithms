import sys

sys.setrecursionlimit(10000000)


class Solution:

    """
    Given a positive integer N, count all possible distinct
    binary strings of length N such that there are no consecutive
    1’s. Output your answer modulo 10^9 + 7.

    https://practice.geeksforgeeks.org/problems/consecutive-1s-not-allowed1912/1
    """

    cache = dict()

    def countStrings(self, n):
        if n == 0:
            return 1

        if n == 1:
            return 2

        if self.cache.get(n):
            return self.cache.get(n)

        value = self.countStrings(n - 2) + self.countStrings(n - 1)

        value = value % (10**9 + 7)

        if self.cache.get(n) is None:
            self.cache[n] = value

        return value
