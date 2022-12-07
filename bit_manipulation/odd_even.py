"""
𝐐 Check if a number is odd or even

➤ All the odd numbers will have the last bit as 1
➤ All the even numbers will have the last bit as 0
➤ Tne last bit decides whether a number is odd or even

ANS: & the number by 1
    if the result is 1 => number is odd
    else the number is even

"""

def is_odd(number: int):
    return number & 1 == 0

def is_even(number: int):
    return number & 1 == 1