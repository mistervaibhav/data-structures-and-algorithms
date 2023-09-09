# https://www.codingninjas.com/studio/problems/left-rotate-an-array-by-one_5026278


def reverse(arr, start, end):
    start_index = start
    end_index = end

    while start_index <= end_index:
        temp = arr[start_index]
        arr[start_index] = arr[end_index]
        arr[end_index] = temp

        start_index += 1
        end_index -= 1


def rotateArray(arr: [], n: int, k: int) -> []:
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)

    # for leetcode
    # reverse(nums, 0,  n - k - 1 )
    # reverse(nums, n - k  , n - 1)
    # reverse(nums, 0, n - 1 )

    return arr
