def reverse_letters(string: str) -> str:
    """Reverse letters in a string but keep the order of the non-letters the same"""
    reversed_characters = reversed([ch for ch in string if ch.isalpha()])
    result_list = list()
    for ch in string:
        if ch.isalpha():
            result_list.append(next(reversed_characters))
        else:
            result_list.append(ch)
    return ''.join(result_list)


if __name__ == "__main__":
    print(reverse_letters("a-bC-dEf-ghIj"))
