from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def reverse_stack(inputStack: list, extraStack: list):
    # Your code goes here

    if len(inputStack) <= 1:
        return

    # moving n - 1 elements from s1 to s2
    while len(inputStack) > 1:
        extraStack.append(inputStack.pop())

    last_element = inputStack.pop()

    while len(extraStack) != 0:
        inputStack.append(extraStack.pop())

    reverse_stack(inputStack, extraStack)

    inputStack.append(last_element)


# Takes a list as a stack and returns whether the stack is empty or not
def is_empty(stack):
    return len(stack) == 0


# Taking input using fast I/o method
def take_input():
    size = int(stdin.readline().strip())

    if size == 0:
        return list()

    return list(map(int, stdin.readline().strip().split(" ")))


# Main
inputStack = take_input()
emptyStack = list()
print(inputStack)
reverse_stack(inputStack, emptyStack)

while not is_empty(inputStack):
    print(inputStack.pop(), end=" ")
