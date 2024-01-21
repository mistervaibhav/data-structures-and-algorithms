import sys

sys.setrecursionlimit(1000000)


class Solution:
    """
    Given a floor of dimensions 2 x W and tiles of dimensions 2 x 1,
    the task is to find the number of ways the floor can be tiled.
    A tile can either be placed horizontally i.e as a 1 x 2 tile or
    vertically i.e as 2 x 1 tile. Print the answer modulo 109+7.

    https://practice.geeksforgeeks.org/problems/ways-to-tile-a-floor5836/1
    """

    cache = dict()

    def numberOfWays(self, n):
        if n < 2:
            return 1

        if self.cache.get(n):
            return self.cache.get(n)

        value = self.numberOfWays(n - 1) + self.numberOfWays(n - 2)

        self.cache[n] = value

        return value


if __name__ == "__main__":
    # t = int(input())
    # for _ in range(t):
    #     N = int(input())

    ob = Solution()
    print(ob.numberOfWays(24151))
