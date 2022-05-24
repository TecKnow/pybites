def is_armstrong(n: int) -> bool:
    string_version = str(n)
    num_digits = len(string_version)
    armstrong_calc = sum(pow(int(x), num_digits) for x in string_version)
    return n == armstrong_calc
