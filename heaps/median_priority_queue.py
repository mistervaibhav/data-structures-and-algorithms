from heapq import heapify, heappop, heappush, heappushpop, nlargest, nsmallest


class MedianPriorityQueue:
    def __init__(self):
        # max heap
        self.__left = []

        # min heap
        self.__right = []

        heapify(self.__left)
        heapify(self.__right)

    def __len__(self):
        return len(self.__left) + len(self.__right)

    def add(self, item):
        pass

    def remove(self):
        pass

    def peek(self):
        pass
