import sys

sys.setrecursionlimit(100000000)


class Solution:

    """
    Given N friends, each one can remain single or can be paired up with some
    other friend. Each friend can be paired only once. Find out the total number
    of ways in which friends can remain single or can be paired up.

    https://practice.geeksforgeeks.org/problems/friends-pairing-problem5425/1
    """

    cache = dict()

    def countFriendsPairings(self, n):
        if n == 0 or n == 1:
            return 1

        if n in self.cache:
            return self.cache[n]

        value = self.countFriendsPairings(n - 1) + (
            (n - 1) * self.countFriendsPairings(n - 2)
        )

        value = value % (10**9 + 7)

        if n not in self.cache:
            self.cache[n] = value

        return value
