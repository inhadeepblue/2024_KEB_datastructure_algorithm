memo = [0 if i == 0 else 1 if i == 1 else None for i in range(100)]
def fibo_memoization(number: int) -> int:
    """
    fibonacci function by recursion with memoization.
    :param number: integer number
    :return: integer number
    """
    global memo
    if memo[number] is not None:
        return memo[number]
    result = fibo_memoization(number-1) + fibo_memoization(number-2)
    memo[number] = result
    return result

n = int(input("Input number : "))
print(f"fibonacci({n}) = {fibo_memoization(n)}")

