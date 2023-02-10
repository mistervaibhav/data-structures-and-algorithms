def power(number, raiseTo):

    if raiseTo == 0:
        return 1

    halfPower = power(number, raiseTo // 2)

    halfPowerSquare = halfPower * halfPower

    if raiseTo % 2 == 0:
        return halfPowerSquare

    return number * halfPowerSquare


if __name__ == "__main__":
    print(power(4, 2))
    print(power(10, 4))
    print(power(15, 3))
    print(power(20, 5))
