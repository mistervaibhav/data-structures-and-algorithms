def factorial(num):

    if num == 0:
        return 1

    return num * factorial(num - 1)


if __name__ == "__main__":
    print(factorial(4))
    print(factorial(10))
    print(factorial(15))
    print(factorial(20))
