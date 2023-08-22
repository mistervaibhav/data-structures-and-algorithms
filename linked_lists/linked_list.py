from node import Node


class LinkedList:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def __str__(self):
        return f"[LinkedList]: head -> {self.head.data}"

    def add_last(self):
        pass

    def display(self):
        head = self.head

        while head.next is not None:
            print(head.data, end=" , ")
            head = head.next
