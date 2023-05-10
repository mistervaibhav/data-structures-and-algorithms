class Solution:

    """
    The series follows this trend  Tn=(Tn-2)2-(Tn-1) in which
    the first and the second term are 0 and 1 respectively

    https://practice.geeksforgeeks.org/problems/gf-series3535/1
    """

    cache = dict()

    def badSolution(self, n):
        if n == 1:
            return 0
        if n == 2:
            return 1

        if self.cache.get(n):
            return self.cache.get(n)

        firstPortion = self.badSolution(n - 2) ** 2
        secondPortion = self.badSolution(n - 1)

        value = firstPortion - secondPortion

        if self.cache.get(n) is None:
            self.cache[n] = value

        return value

    def gfSeries(self, n: int) -> None:
        for i in range(1, n + 1):
            print(self.badSolution(i), end=" ")

        print()
