def is_array_sorted(array: list):

    size = len(array)

    if size == 0 or size == 1:
        return True

    return array[0] < array[1] and is_array_sorted(array[1:])


if __name__ == "__main__":
    print(is_array_sorted([1, 2, 3, 4, 5]))
    print(is_array_sorted([1, 5, 2, 5, 3, 7, 34, 7]))
