from sys import stdin, setrecursionlimit

setrecursionlimit(10**6)


def take_input():
    input_string = stdin.readline().strip()
    size = len(input_string)

    if size == 0:
        return list()

    return list(map(int, input_string.split(" ")))


def subsets(array):
    print(array)


if __name__ == "__main__":
    # 1 2 3 4 5

    array = take_input()

    subsets(array)
