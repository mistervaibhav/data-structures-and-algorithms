from ..linked_lists.node import Node

SINGLE_SPACE = " "


class Queue:

    """
    Head is at the front \n
    Tail is at the rear \n
    New elements are added to the tail / rear \n
    Elements are removed (dequeued) from the head / front \n

    Tail is only used to get the rear
    """

    def __init__(self) -> None:
        self.__head = None
        self.__tail = None
        self.__count = 0

    # def __str__(self) -> str:
    #     return SINGLE_SPACE.join([str(x) for x in self.__array])

    def __len__(self):
        return self.__count

    def is_empty(self):
        return self.__count == 0

    def enqueue(self, data):
        new_node = Node(data)

        if self.__head is None:
            self.__head = new_node
        else:
            self.__head.next = new_node
            self.__head = new_node

        self.__tail = new_node
        self.__count += 1

    def dequeue(self):
        """returns -1 if Queue is empty"""

        if self.is_empty():
            return -1

        front = self.__head.data

        self.__head = self.__head.next
        self.__count -= 1

        return front

    def front(self):
        """returns -1 if Queue is empty"""

        if self.is_empty():
            return -1

        return self.__head.data

    def rear(self):
        """returns -1 if Queue is empty"""

        if self.is_empty():
            return -1

        return self.__tail.data


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(123)
    queue.enqueue(34)
    queue.enqueue(45)
    queue.enqueue(34)

    while not queue.is_empty():
        print(queue.dequeue())
