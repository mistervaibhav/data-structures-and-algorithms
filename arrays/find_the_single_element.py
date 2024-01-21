# https://www.codingninjas.com/studio/problems/find-the-single-element_6680465

from typing import *


def getSingleElement(array: List[int]) -> int:
    xor = 0

    for item in array:
        xor = xor ^ item

    return xor
