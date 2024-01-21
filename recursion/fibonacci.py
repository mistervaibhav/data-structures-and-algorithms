def fibonacci(num):

    if num == 0 or num == 1:
        return num

    return fibonacci(num - 1) + fibonacci(num - 2)


if __name__ == "__main__":
    print(fibonacci(0))
    print(fibonacci(4))
    print(fibonacci(10))
    print(fibonacci(15))
    print(fibonacci(20))
