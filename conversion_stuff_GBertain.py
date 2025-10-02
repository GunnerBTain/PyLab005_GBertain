"""
this function takes a decimal number and converts it into a binary
n is the number passed to be converted
gets the quotient and the remainder of the number until n == 0, then it stops.
the function call prints the converted binary number
"""
def decimal_to_binary(n:int) -> str:
    if n == 0:
        return 'Binary: '
    q, r = divmod(n, 2)
    return decimal_to_binary(q) + str(r)

"""
this function takes a binary number and converts it into a decimal
b is the binary number passed to be converted
it reoccurs until the string 'b' is empty, then it stops
each time it loops it removes the prefix and moves on to the next string character
"""
def binary_to_decimal(b:str) -> int:
    if b == '':
        return 0
    n = len(b) - 1
    pv = 2 ** n
    d = int(b[0])
    v = pv * d
    return v + binary_to_decimal(b.removeprefix(b[0]))

print(decimal_to_binary(10))
print(decimal_to_binary(10))   # "1010"
print(decimal_to_binary(255))  # "11111111"
print(decimal_to_binary(1))    # "1"
print()
print(binary_to_decimal('1010'))

