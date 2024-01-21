# https://leetcode.com/problems/missing-number/


# Brute
# use two loops : outer from 1 to N, and check for
# each item's presence in the array


def missingNumber(nums):
    """
    Better Approach
    """
    tracker = [False] * (len(nums) + 1)

    for item in nums:
        tracker[item] = True

    absent = -1

    for index, presence in enumerate(tracker):
        if presence is False:
            absent = index

    return absent


# optimal method 1
# sum of n numbers = (n*(n+1))/2, add the numbers of the array
def missingNumber(nums):
    size = len(nums)

    sum_of_n = (size * (size + 1)) / 2

    sum_of_array = 0

    for item in nums:
        sum_of_array += item

    return int(sum_of_n - sum_of_array)


# optimal method 2 = XOR
def missingNumber(nums):
    size = len(nums)

    xor_n = 0

    for i in range(1, size + 1):
        xor_n = xor_n ^ i

    xor_array = 0

    for item in nums:
        xor_array = xor_array ^ item

    return xor_n ^ xor_array


# optimal method 2 = XOR , better code
def missingNumber(nums):
    size = len(nums)

    xor_array = 0
    xor_n = 0

    for index, item in enumerate(nums):
        xor_n = xor_n ^ index
        xor_array = xor_array ^ item

    xor_n = xor_n ^ size

    return xor_n ^ xor_array
