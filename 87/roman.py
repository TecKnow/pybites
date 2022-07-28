#  Derived from my solution to the Python Morsels Roman Numeral problem, here:
#  https://github.com/TecKnow/learning/tree/master/pythonmorsels/roman_numeral
#  Which is derived from Paul Winkler's algorithm, here:
#  https://code.activestate.com/recipes/81611-roman-numerals/


def romanize(decimal_number: int) -> str:
    """Takes a decimal number int and converts its Roman Numeral str"""
    if not isinstance(decimal_number, int):
        raise ValueError("expected integer, got %s" % type(decimal_number))
    if not 0 < decimal_number < 4000:
        raise ValueError("Argument must be between 1 and 3999")
    ints = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    nums = ('M', 'CM', 'D', 'CD', 'C', 'XC',
            'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
    result = ""
    for i in range(len(ints)):
        count = int(decimal_number / ints[i])
        result += nums[i] * count
        decimal_number -= ints[i] * count
    return result
