num_hundreds = -1


def sum_numbers(numbers: list) -> int:
    """Sums passed in numbers returning the total, also
       update the global variable num_hundreds with the amount
       of times 100 fits in total"""
    global num_hundreds
    numbers_sum = sum(numbers)
    num_hundreds += numbers_sum // 100
    return numbers_sum
