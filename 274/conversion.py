def dec_to_base(number, base):
    """
    Input: number is the number to be converted
           base is the new base  (eg. 2, 6, or 8)
    Output: the converted number in the new base without the prefix (eg. '0b')
    """
    # your code
    res = str()
    n = number
    while(n > 0):
        next_digit = n % base
        res = str(next_digit) + res
        n = n - next_digit
        n = n // base
    return int(res)
    # return n
