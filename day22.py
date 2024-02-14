def decimal_to_octal(number: int) -> str:
    """
    decimal number to octal number (by repetition)
    :param number: integer (base dec)
    :return: string (base octal)
    """
    octal = ''
    while number > 0:
        octal = str(number % 8) + octal
        number = number // 8
    return octal


n = int(input("Input decimal number : "))
print(decimal_to_octal(n))
