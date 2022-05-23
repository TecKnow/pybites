from collections import Counter


def freq_digit(num: int) -> int:
    digit_counter = Counter(str(num))
    return int(digit_counter.most_common(1)[0][0])
