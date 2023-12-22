class Queue:
    def __init__(self):
        self.__array = list()
        self.__count = 0
        self.__exit_index = 0

    def is_empty(self):
        return self.__count == 0

    def size(self):
        return self.__count

    def enqueue(self, data):
        self.__array.append(data)
        self.__count += 1

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        element = self.__array[self.__exit_index]
        self.__exit_index += 1
        self.__count -= 1

        return element

    def top(self):
        if self.is_empty():
            print("Queue is Empty")
            return

        return self.__array[self.__exit_index]
