def check_bracket(expr: str) -> bool:
    """
    check bracket in expression.
    :param expr: str
    :return: bool
    """
    stack = list()
    table = {')': '(', ']': '[', '}': '{', '>': '<'}
    for char in expr:
        #if char not in table:
        if char in table.values():  # "([{<"
            stack.append(char)  # push
        elif char in table.keys():  # ")]}>"
            if not stack or table[char] != stack.pop():  # pop
                return False
    return len(stack) == 0


if __name__ == "__main__":
    expression = input("Input expression : ")
    print(check_bracket(expression))
    