def sum_numbers(numbers=None):
    numbers = numbers if numbers is not None else range(1, 101)
    return sum(numbers)
