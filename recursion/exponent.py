def exponent(number: int, power: int):

    if power == 0 or power == 1:
        return number

    return number * exponent(number, power - 1)


def exponent_fast(number: int, power: int):

    if power == 0 or power == 1:
        return number

    # if power & 1:
    #     return 2

    return number * exponent_fast(number, power - 1)


if __name__ == "__main__":
    print(exponent_fast(2, 10))
