def print_decreasing(number: int):

    if number == 0:
        return

    print(number, end=" ")
    print_decreasing(number - 1)


if __name__ == "__main__":
    print_decreasing(5)
    print()
