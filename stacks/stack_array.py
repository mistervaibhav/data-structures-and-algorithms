class Stack:
    def __init__(self):
        self.__array = list()

    def is_empty(self):
        return len(self.__array) == 0

    def size(self):
        return len(self.__array)

    def push(self, data):
        self.__array.append(data)

    def pop(self):

        if self.is_empty():
            print("Stack is Empty")
            return

        return self.__array.pop()

    def top(self):

        if self.is_empty():
            print("Stack is Empty")
            return

        return self.__array[len(self.__array) - 1]
