SINGLE_SPACE = " "


class Queue:
    """Queue with fixed capacity"""

    def __init__(self, capacity: int) -> None:
        self.__items = capacity * [None]
        self.__capacity = capacity
        self.__start = -1
        self.__end = -1

    def __str__(self) -> str:
        return SINGLE_SPACE.join([str(x) for x in self.__array])


if __name__ == "__main__":
    queue = Queue()

    queue.enqueue(123)
    queue.enqueue(34)
    queue.enqueue(45)
    queue.enqueue(34)

    while not queue.is_empty():
        print(queue.dequeue())
