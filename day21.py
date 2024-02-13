def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        if char not in table:
            stack.append(char)
        elif not stack or table[char] != stack.pop():
             return False
        else:
            pass
    return len(stack) == 0


if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))
