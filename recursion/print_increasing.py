def print_increasing(number: int):

    if number == 0:
        return

    print_increasing(number - 1)
    print(number, end=" ")


if __name__ == "__main__":
    print_increasing(5)
    print()
