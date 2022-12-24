
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
    def __str__(self):
        return f"[Node]: {self.data}"


class LinkedList:
    def __init__(self, data):
          self.head = Node(data)
          
    def __str__(self):
        return f"[LinkedList]: head -> {self.head.data}"
          
    def display(self):
        head = self.head
        
        while head.next is not None:
            print(head.data, end=" , ")
            head = head.next
            
        