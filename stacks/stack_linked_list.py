from ..linked_lists.node import Node


class Stack:
    def __init__(self):
        self.__head = None
        self.__count = 0

    def is_empty(self):
        return self.size() == 0

    def size(self):
        return self.__count

    def push(self, data):
        node = Node(data)
        node.next = self.__head
        self.__count += 1
        self.__head = node

    def pop(self):

        if self.is_empty():
            print("Stack is Empty")
            return

        data = self.__head
        self.__count -= 1
        self.__head = self.__head.next
        return data

    def top(self):

        if self.is_empty():
            print("Stack is Empty")
            return

        return self.__head
