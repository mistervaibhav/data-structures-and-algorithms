class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def __str__(self):
        return f"[Node]: {self.data}"
