from .stack_array import Stack


def are_brackets_in_pairs(stack, opening):
    return not (stack.is_empty() or stack.top() != opening)


def is_balanced(expression):
    stack = Stack()

    for char in expression:
        if char in ["(", "[", "{"]:
            stack.push(char)
        elif char == ")":
            if are_brackets_in_pairs(stack, "("):
                stack.pop()
            else:
                return False
        elif char == "]":
            if are_brackets_in_pairs(stack, "["):
                stack.pop()
            else:
                return False
        elif char == "}":
            if are_brackets_in_pairs(stack, "{"):
                stack.pop()
            else:
                return False

    return stack.is_empty()


if __name__ == "__main__":

    TEST_CASES = ["(())", ")()()(", "()((())())"]

    for tc in TEST_CASES:
        print(is_balanced(tc))
        # if is_balanced(tc):
        #     print(tc, ">>>>> true")
        # else:
        #     print(tc, ">>>>> false")


# { ( [ ) ] }
# {(a + b) - (x * u) & [1, 2]}
# )()()(
