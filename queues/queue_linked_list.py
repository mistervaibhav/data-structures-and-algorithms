from ..linked_lists.node import Node

SINGLE_SPACE = " "


class Queue:
    def __init__(self) -> None:
        self.__array = list()

    def __str__(self) -> str:
        return SINGLE_SPACE.join([str(x) for x in self.__array])

    def size(self):
        return len(self.__array)

    def is_empty(self):
        return self.size() == 0

    def enqueue(self, item: int):
        self.__array.append(item)

    def dequeue(self):
        """returns -1 if Queue is empty"""

        if self.is_empty():
            return -1

        return self.__array.pop(0)

    def front(self):
        """returns -1 if Queue is empty"""

        if self.is_empty():
            return -1

        return self.__array[0]


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(123)
    queue.enqueue(34)
    queue.enqueue(45)
    queue.enqueue(34)

    while not queue.is_empty():
        print(queue.dequeue())
